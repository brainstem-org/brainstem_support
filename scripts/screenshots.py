#!/usr/bin/env python3
"""Take the screenshots the documentation uses, from a BrainSTEM instance with the demo dataset.

The pages mark where a screenshot goes with ``<!-- screenshot: <slug> | <what to capture> -->``; this script
produces ``docs/assets/images/screenshots/<slug>.png`` for every slug in TARGETS, logging in as a demo user and
driving the private portal with a headless browser. Rerun it after a BrainSTEM release so the pictures show the
current interface.

Requirements: Playwright for Python with Chromium (``pip install playwright && playwright install chromium``),
a BrainSTEM server with the demo dataset (``manage.py generate_demo_project --user-email <demo user>``) and,
when the demo user has two-factor authentication, either a TOTP secret or a checkout to read the token from.

Environment:
    BRAINSTEM_URL                 server, default http://localhost:8000
    BRAINSTEM_SCREENSHOT_USER     demo user's email
    BRAINSTEM_SCREENSHOT_PASSWORD demo user's password
    BRAINSTEM_CHECKOUT            BrainSTEM checkout; its virtualenv computes the TOTP code for the login wizard
    BRAINSTEM_SCREENSHOT_ALLOW_EMAILS  comma-separated emails a picture may show besides the demo user's
    BRAINSTEM_SCREENSHOT_ASSISTANT     1 on a server whose AI assistant answers: ai-assistant-drawer-results shows results

Most pictures only look; a few write as the demo user: deleted-entries-recover-page deletes a session kept for it,
user-profile-sessions ends the demo user's other sessions, and user-profile-token-created creates an API token and
revokes it once the picture is taken.

    python scripts/screenshots.py                 # every screenshot and walkthrough
    python scripts/screenshots.py forms-materials-editor dashboard-manage-widgets
    python scripts/screenshots.py walkthroughs    # the recorded walkthroughs only
    python scripts/screenshots.py tour            # the landing-page tour only
    python scripts/screenshots.py tour:ai         # one chapter of the tour
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
OUT = REPO_ROOT / "docs" / "assets" / "images" / "screenshots"
BASE = os.environ.get("BRAINSTEM_URL", "http://localhost:8000").rstrip("/")
USER = os.environ.get("BRAINSTEM_SCREENSHOT_USER", "docs-screens@brainstem.org")
PASSWORD = os.environ.get("BRAINSTEM_SCREENSHOT_PASSWORD", "")
CHECKOUT = os.environ.get("BRAINSTEM_CHECKOUT", "")
VIEWPORT = {"width": 1440, "height": 900}
HIDE_CSS = "#djDebug,#djDebugToolbarHandle{display:none!important}"  # the debug toolbar of a development server
# A desktop Chrome rather than "HeadlessChrome", which the active-sessions page would show as the device.
USER_AGENT = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/141.0.0.0 Safari/537.36")
LOCALE = "en-US"  # not the machine's: a Danish locale writes coordinates as "-3,6"
# Chrome on macOS draws number fields in the system's region format ("-3,6" on a Danish Mac) whatever the page or
# browser language; as text fields they show the stored value ("-3.6"). Fields added later (type-specific editors)
# are caught as they appear.
NUMBER_FIELDS_JS = """(() => {
    const fix = root => { if (root.querySelectorAll) root.querySelectorAll('input[type=number]').forEach(i => { i.type = 'text'; }); };
    document.addEventListener('DOMContentLoaded', () => {
        fix(document);
        new MutationObserver(changes => changes.forEach(c => c.addedNodes.forEach(n => { if (n.nodeType === 1) fix(n.parentNode || n); })))
            .observe(document.documentElement, {childList: true, subtree: true});
    });
})();"""
DEMO_EMAILS = {"alex.sample@brainstem.org"}  # the demo dataset's other member
ALLOWED_EMAILS = DEMO_EMAILS | {e.strip().lower() for e in os.environ.get("BRAINSTEM_SCREENSHOT_ALLOW_EMAILS", "").split(",") if e.strip()}
EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")


def totp_token() -> str:
    """The current one-time code of the demo user's TOTP device, computed inside the checkout."""
    code = (
        "from django.contrib.auth import get_user_model\n"
        "from django_otp.plugins.otp_totp.models import TOTPDevice\n"
        "from django_otp.oath import totp\n"
        f"u=get_user_model().objects.get(email='{USER}')\n"
        "d=TOTPDevice.objects.filter(user=u, confirmed=True).first()\n"
        "print(str(totp(d.bin_key, d.step, d.t0, d.digits, d.drift)).zfill(d.digits))"
    )
    python = Path(CHECKOUT) / ".venv" / "bin" / "python"
    out = subprocess.run([str(python), "manage.py", "shell", "-c", code], cwd=CHECKOUT, capture_output=True, text=True)
    return out.stdout.strip().splitlines()[-1]


def login(page):
    page.goto(BASE + "/login/", wait_until="networkidle")
    page.fill("#id_auth-username", USER)
    page.fill("#id_auth-password", PASSWORD)
    page.press("#id_auth-password", "Enter")
    page.wait_for_load_state("networkidle")
    visible = page.locator("input:visible").evaluate_all("els => els.map(e => [e.type, e.name, e.id])")
    otp = [i for i in visible if i[0] in ("text", "number", "tel") and any(k in i[1] for k in ("otp", "token", "code"))]
    if otp:
        if not CHECKOUT:
            raise SystemExit("the demo user has two-factor authentication: set BRAINSTEM_CHECKOUT")
        sel = "#" + otp[0][2] if otp[0][2] else f"input[name='{otp[0][1]}']"
        page.fill(sel, totp_token())
        page.press(sel, "Enter")
        page.wait_for_load_state("networkidle")
    if "/login" in page.url:
        raise SystemExit(f"login failed: {page.url}")


def logout_other_sessions(page):
    """End the sessions earlier runs left behind, so the active-sessions picture shows one session."""
    form = page.locator("form[action$='/sessions/logout-others/']")
    if not form.count():
        return
    # Submit the form itself: its button asks for confirmation through a page script.
    with page.expect_navigation():
        form.first.evaluate("f => f.submit()")
    page.wait_for_load_state("networkidle")
    page.goto(BASE + "/private/users/sessions/", wait_until="networkidle")
    page.add_style_tag(content=HIDE_CSS)


def open_row_menu(page):
    """Open the More actions menu of the first row. Its actions appear once the row's permissions have loaded, which
    hovering the row starts."""
    name = page.locator("#result_list tbody tr .name_container").first
    name.hover()
    page.wait_for_timeout(1200)
    button = name.locator(".row-action--menu").first
    if button.is_visible():
        button.click(timeout=4000)
    else:
        button.evaluate("b => b.click()")


def check_no_foreign_email(page):
    """Refuse a picture that shows anyone's email address but the demo user's: the demo dataset must be owned and
    performed by the demo user (manage.py generate_demo_project --user-email <demo user>), never a real account."""
    # Text a reader can see anywhere on the page: not the options of a closed <select> (the "Performed by" list names
    # every account) nor hidden elements.
    text = page.evaluate("""() => { if (!document.body) return '';
        const out = [], walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
        for (let n; (n = walker.nextNode());) { const el = n.parentElement;
            if (el && n.textContent.trim() && !el.closest('option, script, style, template, noscript') && el.checkVisibility()) out.push(n.textContent); }
        return out.join('\\n'); }""")
    found = {e.lower() for e in EMAIL.findall(text)} - {USER.lower()} - ALLOWED_EMAILS
    if found:
        raise RuntimeError(f"the page shows another account's email ({', '.join(sorted(found))}); "
                           "re-seed the demo dataset as the demo user")


def first_row_link(page, list_path: str, query: str) -> str:
    """The change-page path of the first entry a list search finds."""
    page.goto(f"{BASE}{list_path}?q={query}", wait_until="networkidle")
    links = page.locator("table tbody tr a").evaluate_all(
        "els => els.map(e => e.getAttribute('href')).filter(h => h && h.includes('/change/'))"
    )
    if not links:
        raise LookupError(f"no entry for {query!r} under {list_path}")
    return links[0].split("?")[0]  # drop the list's _changelist_filters, or appended queries break


# One target per documentation placeholder. `go` is a path or a callable(page) -> path; `steps` run after the
# page loaded: ("click", text), ("click_sel", css), ("click_force", css), ("wait", ms), ("fill", css, text),
# ("press", css, key), ("js", script), ("select", css, label) for a native <select>, ("select2", select_css,
# text) to pick in a Select2 widget, ("open_select2", select_css, text) to leave it open after typing,
# ("scroll_to", css), ("wait_gone", [texts], max_ms) to wait until loading messages disappear, and
# ("call", function) to run a function(page). `clip` limits the picture to a CSS selector, `around` to the box
# round a list of elements (each a selector or its fallbacks), `full` takes the whole page. `css` is a style added
# once the page has loaded, `after` steps run once the picture is taken, `cleanup` steps run whether or not it was,
# and `"no_save": True` refuses every write the page attempts (for a change form whose fields a target changes; forms
# autosave).


def entry(list_path: str, query: str = "", suffix: str = "change/"):
    """A `go` callable: the first entry a list search finds, as its change page (or details page with suffix="")."""
    def go(page):
        return first_row_link(page, list_path, query).replace("/change/", "/" + suffix if suffix else "/")
    return go


def entry_id(page, list_path: str, query: str) -> str:
    return first_row_link(page, list_path, query).rstrip("/").split("/")[-2]


VIEWER_LOADING = ["Preparing coordinate viewer", "Loading atlas anatomy"]
RAT_IMPLANT = entry("/private/modules/procedure/", "Silicon+probe+implant+R06")
RAT_IMPLANT_DETAILS = entry("/private/modules/procedure/", "Silicon+probe+implant+R06", "")


def select_by_text(select, text: str):
    labels = select.locator("option").all_text_contents()
    # An exact label first: "Male" is also inside "Female".
    match = next((label for label in labels if label.strip().lower() == text.lower()), None) \
        or next((label for label in labels if text.lower() in label.lower()), None)
    if match:
        select.select_option(label=match)


def fill_import_grid(page):
    """Three subject rows in the batch-entry grid, then validate: one new, one existing, one with a problem."""
    fill_import_rows(page)
    page.get_by_text("Validate current tab", exact=True).first.click()
    page.wait_for_timeout(2500)


def fill_import_rows(page):
    """The three subject rows of fill_import_grid, not yet validated."""
    page.locator("button:has-text('Subjects')").first.click()
    page.wait_for_timeout(700)
    rows = [
        ("Neural dynamics", "SAMPLE Mouse M10 - Bruno II", "Male", "Mus musculus", "Active"),
        ("Neural dynamics", "SAMPLE Mouse M09 - Antonio", "Male", "Mus musculus", "Active"),
        ("Neural dynamics", "SAMPLE Mouse M11 - Lola", "Female", "", "Active"),
    ]
    grid = page.locator("table:visible").first
    for _ in range(len(rows) - grid.locator("tbody tr").count()):
        page.get_by_text("Add row", exact=True).first.click()
        page.wait_for_timeout(200)
    for index, (project, name, sex, species, status) in enumerate(rows):
        cells = grid.locator("tbody tr").nth(index).locator("td")
        select_by_text(cells.nth(1).locator("select"), project)
        cells.nth(2).locator("input").fill(name)
        select_by_text(cells.nth(3).locator("select"), sex)
        if species:
            select_by_text(cells.nth(4).locator("select"), species)
            page.wait_for_timeout(500)
            select_by_text(cells.nth(5).locator("select"), "C57BL/6J")
        select_by_text(cells.nth(6).locator("select"), status)


def field(name: str) -> list[str]:
    """A form or details field by name: its half of a two-column row, else its whole row."""
    return [f".field-box.field-{name}", f".form-row.field-{name}"]


def second_session(page):
    """Sign in once more from another browser, so the active-sessions page lists a second session to log out."""
    other = page.context.browser.new_context(user_agent=USER_AGENT.replace("Macintosh; Intel Mac OS X 10_15_7", "Windows NT 10.0; Win64; x64"),
                                             locale=LOCALE)
    try:
        login(other.new_page())
    finally:
        other.close()


def guard_writes(route):
    """For a picture that changes a form without saving it (`"no_save": True`): change forms autosave as fields
    change, so every write to the API is refused; an autosave is answered as if it succeeded, so the form shows no
    error."""
    request = route.request
    writes = request.method not in ("GET", "HEAD", "OPTIONS") and any(k in request.url for k in ("/api/", "/ajax/", "_method="))
    if not writes:
        route.continue_()
    elif request.method == "PATCH" or "_method=PATCH" in request.url:
        route.fulfill(status=200, content_type="application/json", body="{}")
    else:
        route.abort()


def confirm_identity(page):
    """The step-up page sensitive actions ask for when the sign-in is older than a few minutes: the two-factor code
    (when the demo user has a device), then the password."""
    otp = page.locator("input[name=otp_token]")
    if otp.count() and otp.first.is_visible():
        if not CHECKOUT:
            raise SystemExit("creating a token asks for the two-factor code again: set BRAINSTEM_CHECKOUT")
        for attempt in range(2):
            otp.first.fill(totp_token())
            with page.expect_navigation():
                page.locator("button[name=_verify_mfa]").first.click()
            page.wait_for_load_state("networkidle")
            if not (otp.count() and otp.first.is_visible()):
                break
            page.wait_for_timeout(31000)  # the code of the sign-in cannot be used twice: wait for the next one
    password = page.locator("#id_current_password")
    if password.count():
        password.fill(PASSWORD)
        with page.expect_navigation():
            password.press("Enter")
        page.wait_for_load_state("networkidle")


DOCS_TOKEN = "Docs example token"  # created for user-profile-token-created and revoked right after the picture


def revoke_docs_token(page) -> bool:
    """Revoke the token user-profile-token-created made (its value is in the picture); True if there was one."""
    page.goto(BASE + "/private/users/tokens/", wait_until="networkidle")
    found = page.evaluate("""name => {
        const form = [...document.querySelectorAll("form[action^='delete/']")].find(f => {
            for (let n = f.parentElement, i = 0; n && i < 8; n = n.parentElement, i++) {
                if (n.querySelectorAll("form[action^='delete/']").length > 1) return false;
                if (n.textContent.includes(name)) return true;
            }
            return false;
        });
        if (form) { form.setAttribute('data-docs-revoke', ''); return true; }
        return false;
    }""", DOCS_TOKEN)
    if found:
        # Submit the form itself: its button asks for confirmation through a page script.
        with page.expect_navigation():
            page.locator("form[data-docs-revoke]").first.evaluate("f => f.submit()")
        page.wait_for_load_state("networkidle")
    return found


def create_docs_token(page):
    """Create a personal access token, confirming the identity when the page asks, so the page that shows the new
    token once is open."""
    for _ in range(3):
        page.fill("#token_name", DOCS_TOKEN)
        with page.expect_navigation():
            page.locator("form[action='create/'] [type=submit]").first.click()
        page.wait_for_load_state("networkidle")
        if page.locator("#access_token").count():
            return
        if page.locator("#id_current_password, input[name=otp_token]").count():
            confirm_identity(page)
        elif not revoke_docs_token(page):  # left active by an earlier run that failed before revoking it
            break
        page.goto(BASE + "/private/users/tokens/", wait_until="networkidle")
    raise RuntimeError(f"no token was created (ended on {page.url})")


GET_STARTED_PROJECT = "Hippocampal place cells 2026"  # the project get-started-project-form fills in


def stand_in_project(page):
    """Show the project the getting-started guide creates in the Projects field, which lists the demo project: the
    picked option is relabelled for the picture only (Select2 redraws it; the form's own scripts are not told)."""
    page.locator("#id_projects").first.evaluate("""(s, label) => {
        const o = [...s.options].find(o => o.selected);
        if (!o) return;
        o.textContent = label;
        for (const $ of [window.jQuery, window.django && django.jQuery]) {
            if ($ && $(s).data('select2')) { $(s).trigger('change.select2'); return; }
        }
    }""", GET_STARTED_PROJECT)


def acquisition_entry(kind: str) -> list[str]:
    """`around` for one entry of a session's Data acquisition tab: its header and its details."""
    header = f"fieldset.selected .field-dataacquisitions > .detail-view__inline__header:has-text('{kind}')"
    return [header, header + " + .field-content__wrapper"]


def scroll_to_top(selector: str, offset: int = 90):
    """A `call` step: scroll the page so the element sits just under the fixed top bar."""
    return lambda page: page.locator(selector).first.evaluate(
        "(e, offset) => window.scrollTo(0, e.getBoundingClientRect().top + window.scrollY - offset)", offset)


def fill_new_behavior(page):
    """The behavior Add Behavior opened on the session's change form, filled in as the tutorial's step says (never
    saved: the target refuses writes)."""
    form = page.locator("#behaviors-group .inline-related:not(.empty-form)").last
    prefix = form.get_attribute("id") or ""
    for name, text in (("subjects", "R02"), ("setup", "Rat Electrophysiology"), ("behavioralassay", "Rat Delayed")):
        css = f"#id_{prefix}-{name}"
        if not page.locator(css).count():
            continue
        try:
            do_step(page, ("select2", css, text))
            page.wait_for_timeout(700)
        except Exception as error:  # noqa: BLE001 - the notice is the point of the picture, not every field
            print(f"        (left {name} empty: {str(error).splitlines()[0][:80]})")


def show_brain_regions(page):
    """Switch on the coloured brain-region overlay of the coordinate viewer, once the atlas labels have loaded."""
    toggle = page.locator("[data-coordinate-show-regions]").first
    for _ in range(60):
        if toggle.count() and toggle.is_enabled():
            break
        page.wait_for_timeout(500)
    if toggle.count() and toggle.is_enabled() and not toggle.is_checked():
        page.locator("label[for=coordinate-preview-show-regions]").first.click()
        page.wait_for_timeout(2500)
    elif not (toggle.count() and toggle.is_enabled()):
        print("        (no brain-region overlay for this atlas)")


# The 3D view at a lower brain opacity, so the implant's track shows through the brain.
BRAIN_OPACITY_JS = ("const r = document.querySelector('[data-coordinate-brain-opacity]');"
                    " if (r) { r.value = 25; r.dispatchEvent(new Event('input', {bubbles: true})); }")
# The CKEditor description box as tall as its text, not its 300-pixel default.
SHORT_EDITOR_CSS = (".ck.ck-editor__main > .ck-editor__editable, .ck-editor__editable_inline"
                    "{min-height: 0 !important; height: auto !important}")
# The AI assistant answers only on a server with a working provider; set BRAINSTEM_SCREENSHOT_ASSISTANT=1 there and
# ai-assistant-drawer-results shows the answer (result cards, Show all and the link to the list).
ASSISTANT_ANSWERS = os.environ.get("BRAINSTEM_SCREENSHOT_ASSISTANT") == "1"
ASSISTANT_QUESTION = [("click_sel", ".brainstem-assistant__launcher"), ("wait", 1200),
                      ("fill", "[class*=brainstem-assistant] textarea", "Reversal sessions of mouse M09"), ("wait", 600)]


TAB = "fieldset.module.selected"  # the open tab of a details or change page
FORM_CARD = [field("name"), "button[name=_continue]"]  # an add form from its name field down to its buttons
TARGETS: list[dict] = [
    # Dashboard (with the navigation sidebar, which the page explains)
    {"slug": "dashboard-overview", "go": "/private/", "sidebar": True},
    # Every step of the checklist, the completed ones included (they sit in a collapsed <details>).
    {"slug": "dashboard-getting-started", "go": "/private/", "clip": ".dashboard-item:has-text('Getting started')",
     "steps": [("js", "document.querySelectorAll('details.dashboard-onboarding-completed').forEach(d => d.open = true)"), ("wait", 500)]},
    {"slug": "dashboard-recent-activity", "go": "/private/", "steps": [("call", lambda p: p.locator(".header__action__button").filter(has=p.locator("[class*=history], [class*=clock]")).first.click() if p.locator(".header__action__button").filter(has=p.locator("[class*=history], [class*=clock]")).count() else p.locator(".header__action__button").nth(6).click()), ("wait", 1500)]},
    # List view
    {"slug": "list-view-procedures", "go": "/private/modules/procedure/", "viewport": {"width": 1440, "height": 680}},
    {"slug": "list-view-sessions", "go": "/private/stem/session/", "viewport": {"width": 1440, "height": 680}},
    # A search and what it found: the list's search box with the query typed, the result count, and the first matching
    # rows (the sidebar has a search box of its own, left alone).
    {"slug": "list-view-manage-filters", "go": "/private/modules/procedure/", "steps": [("click", "Filters"), ("wait", 800)]},
    {"slug": "list-view-region-filter-dialog", "go": "/private/modules/procedure/", "steps": [
        ("click_sel", ".anatomical-region-filter__trigger"), ("wait", 1500), ("wait_gone", ["Loading"], 8000)]},
    {"slug": "list-view-manage-columns", "go": "/private/modules/procedure/", "steps": [("click", "Columns"), ("wait", 800)]},
    # The last three rows ticked, the actions bar under them and its action list opened downwards in full (room is
    # added under the table, so the list does not open over the rows); the toolbar that follows the scroll is hidden.
    {"slug": "list-view-bulk-actions", "go": "/private/stem/subject/", "viewport": {"width": 1440, "height": 1000},
     "css": ("body{padding-bottom:520px!important} .list-view__header__actions .object-tools.sticky{visibility:hidden!important}"
             " .select2-results > .select2-results__options{max-height:none!important}"),
     "around": ["#result_list tbody tr:nth-last-child(3)", ".changelist-footer .actions", ".select2-container--open .select2-dropdown"],
     "steps": [
        ("js", "[...document.querySelectorAll('input.action-select')].slice(-3).forEach(c => c.click())"),
        ("js", "document.querySelector('.changelist-footer .actions').scrollIntoView({block: 'center'})"), ("wait", 400),
        ("open_select2", "select[name=action]", ""), ("wait", 600)]},
    # Procedures have the fullest row menu (Create template among others).
    {"slug": "list-view-row-actions", "go": "/private/modules/procedure/", "steps": [("call", open_row_menu), ("wait", 600)]},
    # The dialog with the demo project ticked (not saved, so the lists stay unfiltered for the other pictures).
    {"slug": "list-view-active-projects", "go": "/private/stem/subject/", "steps": [
        ("click", "Manage active projects"), ("wait", 1000),
        ("js", "const c = document.querySelector('.active-projects-modal__project__list [id^=unique_checkbox_id_]'); if (c && !c.checked) c.click();"),
        ("wait", 600)],
     "after": [("click_sel", ".active-projects-modal__cancel")]},
    # Forms: change pages of demo entries, so the fields are filled
    {"slug": "forms-procedure-general", "go": entry("/private/modules/procedure/", "Cranial+window")},
    {"slug": "forms-add-material-menu", "go": entry("/private/modules/procedure/", "Cranial+window"),
     "steps": [("click", "Materials ("), ("wait", 500), ("click", "Add material"), ("wait", 800)]},
    {"slug": "forms-templates-picker", "go": entry("/private/modules/procedure/", "Cranial+window"),
     "steps": [("click", "Materials ("), ("wait", 500), ("click", "Use template"), ("wait", 1000)]},
    {"slug": "forms-chained-selector", "go": entry("/private/stem/subject/", "M09+Antonio"), "viewport": {"width": 1440, "height": 640},
     "steps": [("open_select2", "#id_strain", "C57"), ("wait", 600)]},
    # The coordinate system, View coordinates and the coordinate fields of the implant.
    # The implant's coordinates: the window centred on the View coordinates button, the coordinate fields around it.
    {"slug": "forms-coordinates", "go": RAT_IMPLANT, "viewport": {"width": 1440, "height": 760}, "steps": [
        ("wait", 800), ("call", lambda p: p.locator("[data-coordinate-preview-button]").first.evaluate("e => e.scrollIntoView({block: 'center'})")),
        ("wait", 600)]},
    # The server's own messages: the browser's required-field check is switched off, so the form is submitted empty.
    # The guided duplicate page of a subject (Duplicate in the header of its details page), with two kinds ticked.
    {"slug": "forms-duplication-page", "go": entry("/private/stem/subject/", "SAMPLE+Mouse+M09", "duplicate/"),
     "steps": [("js", "[...document.querySelectorAll('input[type=checkbox]')].filter(c => /^\\s*(Procedures|Subject logs)/.test("
                      "(c.closest('label') || c.parentElement).textContent)).forEach(c => { if (!c.checked) c.click(); })"), ("wait", 400)]},
    # Single entry view: the details page of an entry
    {"slug": "single-entry-view-session", "go": entry("/private/stem/session/", "R02+Steve+Reversal+01", ""), "viewport": {"width": 1440, "height": 640}},
    {"slug": "single-entry-view-session-epochs", "go": entry("/private/stem/session/", "R02+Steve+Reversal+01", ""), "steps": [("click", "Epochs ("), ("wait", 1000)]},
    {"slug": "single-entry-view-subject-procedures", "go": entry("/private/stem/subject/", "M09+Antonio", ""), "steps": [("click", "Procedures ("), ("wait", 1000)]},
    # The header with its open Export menu, not the whole page.
    # The project's Export menu: the record exports and the project's own, STAR Methods and Download project data.
    {"slug": "exports-project-export-menu", "go": entry("/private/stem/project/", "Neural+dynamics", ""),
     "around": [".exportlink--with-dropdown", ".exportlink__dropdown", "h1"], "pad": 24,
     "steps": [("click_sel", ".exportlink--with-dropdown"), ("wait", 600)]},
    # An entry that was edited after it was created: R02's implantation episode, whose severity and description were
    # changed (the history of the demo's sessions holds only the dataset's own revisions).
    {"slug": "single-entry-view-history", "go": entry("/private/modules/procedureepisode/", "R02+Steve+Electrophysiology", "history/"),
     "viewport": {"width": 1440, "height": 560}},
    {"slug": "single-entry-view-data-graph", "go": lambda p: "/private/datamodel/?view=overview&record=stem.session:" + entry_id(p, "/private/stem/session/", "R02+Steve+Reversal+01"),
     "steps": [("wait", 4000)]},
    # Each Data acquisition tab cropped to the modality's own entry (not the video tracking above it, which records
    # through no interface): its header, setup, equipment, experimental interface and details.
    {"slug": "ephys-session-data-acquisition", "go": entry("/private/stem/session/", "R02+Steve+Reversal+01", ""),
     "viewport": {"width": 1440, "height": 1100}, "around": acquisition_entry("Extracellular Electrophysiology"),
     "steps": [("click", "Data acquisition ("), ("wait", 800),
               ("call", scroll_to_top(acquisition_entry("Extracellular Electrophysiology")[0])), ("wait", 400)]},
    {"slug": "2p-data-acquisition-tab", "go": entry("/private/stem/session/", "M03+Mirabel+Acquisition+01", ""),
     "viewport": {"width": 1440, "height": 1100}, "around": acquisition_entry("Two-Photon Microscopy"),
     "steps": [("click", "Data acquisition ("), ("wait", 800),
               ("call", scroll_to_top(acquisition_entry("Two-Photon Microscopy")[0])), ("wait", 400)]},
    # The behavior Add Behavior opens on the session's change form, filled in, with its notice that the setup and the
    # behavioral assay must share the setup type (nothing is saved).
    {"slug": "ephys-behavior-tab", "go": entry("/private/stem/session/", "R02+Steve+Reversal+01"), "no_save": True,
     "viewport": {"width": 1440, "height": 1000}, "clip": "#behaviors-group",
     "steps": [("click_sel", ".changeform-tabs-item a:has-text('Behaviors')"), ("wait", 800),
               ("click_sel", "#behaviors-group .add-row a >> visible=true"), ("wait", 1000),
               ("call", fill_new_behavior), ("wait", 500)]},
    # The rat implant of the electrophysiology tutorial: the experimental interface it created, on its own tab.
    {"slug": "ephys-subject-procedures", "go": RAT_IMPLANT_DETAILS, "viewport": {"width": 1440, "height": 760},
     "steps": [("click_sel", ".changeform-tabs-item a:has-text('Experimental interfaces')"), ("wait", 800)]},
    # Planning
    {"slug": "planning-planned-form", "go": entry("/private/stem/session/", "Reversal+03+(planned)"), "viewport": {"width": 1440, "height": 640}},
    # Import tool and SoftMouse
    {"slug": "import-tool-batch-grid", "go": "/private/import-tool/", "steps": [("call", fill_import_grid)]},
    # The page in full: the intro and the Projects, Subjects and Sessions sections with their templates.
    {"slug": "import-tool-csv", "go": "/private/import-tool/", "full": True, "steps": [("click", "CSV import"), ("wait", 800)]},
    # The credentials form a user without saved SoftMouse credentials sees. (softmouse-import-preview, the Import
    # Configuration preview, needs saved credentials, an uploaded SoftMouse export and subjects linked to earlier
    # SoftMouse imports for its Update and Skip rows, which the demo dataset does not have.)
    {"slug": "softmouse-credentials", "go": "/private/softmouse/credentials/"},
    # Exports
    {"slug": "exports-print-preview", "go": entry("/private/stem/project/", "Neural+dynamics", "export/?format=html&mode=full")},
    {"slug": "exports-star-methods-preview", "go": entry("/private/stem/project/", "Neural+dynamics", "export/?format=html&mode=star_methods")},
    # The page title and the whole form under it: File format and Contents, the parts list and the JSON options (a
    # window tall enough for all of it, so the crop is not scrolled under the top bar).
    {"slug": "exports-download-project-data", "go": entry("/private/stem/project/", "Neural+dynamics", "download/"),
     "viewport": {"width": 1440, "height": 1500}, "around": ["h1.custom-content__title", ".form__wrapper"], "pad": 20},
    # CSV chosen, not the empty format.
    # Probe catalog
    # The schematic is an SVG image of its own; capture the drawing rather than the page around it.
    {"slug": "probe-catalog-schematic", "go": entry("/private/resources/consumable/", "A16x8-5mm-berg-200-160", "schematic.svg"),
     "viewport": {"width": 1100, "height": 760}, "steps": [("wait", 1000)]},
    {"slug": "probe-catalog-ecog", "go": entry("/private/resources/consumable/", "EcogArrayDesign", "schematic.svg"),
     "viewport": {"width": 1100, "height": 760}, "steps": [("wait", 1000)]},
    # The top of the details page (name, type, supplier and the design's details); the schematic has its own pictures.
    {"slug": "probe-catalog-page", "go": entry("/private/resources/consumable/", "A16x8-5mm-berg-200-160", "")},
    # The design's form at its type-specific details: the geometry.
    # Atlases and coordinates
    # The brain at a quarter of its opacity, so the probe's track shows through it.
    {"slug": "atlases-viewer-rat-3d", "go": RAT_IMPLANT, "steps": [("click", "View coordinates"), ("wait_gone", VIEWER_LOADING, 90000),
     ("wait", 1500), ("js", BRAIN_OPACITY_JS), ("wait", 2000)]},
    # The three planes with the coloured brain-region overlay on.
    {"slug": "atlases-viewer-rat-all-planes", "go": RAT_IMPLANT, "steps": [("click", "View coordinates"), ("wait_gone", VIEWER_LOADING, 90000),
     ("click", "All planes"), ("wait", 2500), ("call", show_brain_regions)]},
    # The Atlas and Target regions fields with the region list open.
    {"slug": "atlases-region-picker", "go": RAT_IMPLANT, "around": [field("target_regions_atlas"), field("target_regions"), ".select2-container--open .select2-dropdown"],
     "pad": 24, "steps": [("open_select2", "#id_target_regions", "CA1"), ("wait", 1000)]},
    # Account
    {"slug": "user-profile-page", "go": "/private/users/user/63/"},
    {"slug": "user-profile-api-token-management", "go": "/private/users/tokens/"},
    # A token just created, shown once. It is a real token of the demo user, so it is revoked as soon as the picture
    # is taken, also when the capture fails (`cleanup`); creating it may ask for the password and two-factor code
    # again (BRAINSTEM_CHECKOUT).
    {"slug": "user-profile-token-created", "go": "/private/users/tokens/", "viewport": {"width": 1440, "height": 1100},
     "around": [".login-signup__form__header", "#access_token", "#copy_btn", "a.link-element--arrow-back"], "pad": 24,
     "steps": [("call", create_docs_token), ("wait", 500)], "cleanup": [("call", revoke_docs_token)]},
    # Earlier runs' sessions ended, then one more sign-in from another browser: a second row with its Log out button.
    {"slug": "user-profile-sessions", "go": "/private/users/sessions/", "viewport": {"width": 1440, "height": 700},
     "steps": [("call", logout_other_sessions), ("call", second_session), ("call", lambda p: p.reload(wait_until="networkidle")),
               ("wait", 600)]},
    {"slug": "two-factor-active-methods", "go": "/account/two_factor/", "viewport": {"width": 1100, "height": 700}},
    # The settings page in full, down to the form for one's own provider key.
    {"slug": "ai-assistant-settings", "go": "/private/llm-assistant-settings/", "full": True},
    # With BRAINSTEM_SCREENSHOT_ASSISTANT=1 (a server whose assistant answers): the drawer with the answer, its result
    # cards, Show all and the link to the list. Otherwise the question box: examples, the question, Page context, AI
    # summary and Search.
    {"slug": "ai-assistant-drawer-results", "go": "/private/stem/subject/",
     "steps": ASSISTANT_QUESTION + [
         ("click_sel", ".brainstem-assistant__submit"),
         ("call", lambda p: p.wait_for_selector(".brainstem-assistant__drawer .llm-assistant__results", timeout=120000)),
         ("wait_gone", ["Searching"], 30000), ("wait", 1500)],
     "clip": ".brainstem-assistant__drawer",
     "after": [("click_sel", ".brainstem-assistant__close")]} if ASSISTANT_ANSWERS else
    {"slug": "ai-assistant-drawer-results", "go": "/private/stem/subject/",
     "around": [".brainstem-assistant__examples", ".brainstem-assistant__submit"], "pad": 24, "steps": ASSISTANT_QUESTION,
     "after": [("click_sel", ".brainstem-assistant__close")]},
    {"slug": "project-public-access-dialog", "go": entry("/private/stem/project/", "Neural+dynamics"),
     "steps": [("js", "document.querySelector('#id_is_public_1').click()"), ("wait", 1200)], "after": [("press", "body", "Escape")]},
    # The whole page, down to Save and Return to project under the tables.
    {"slug": "project-permissions", "go": entry("/private/stem/project/", "Neural+dynamics", "manage/"), "full": True},
    # Deleted entries
    {"slug": "deleted-entries-recover-page", "go": lambda p: recover_page(p)},
    # Forms used by the tutorials: change pages of demo entries, so the fields are filled
    {"slug": "project-add-form", "go": entry("/private/stem/project/", "Neural+dynamics"), "viewport": {"width": 1440, "height": 620}},
    {"slug": "subject-add-form", "go": entry("/private/stem/subject/", "M09+Antonio")},
    {"slug": "session-add-form", "go": entry("/private/stem/session/", "R02+Steve+Reversal+01"), "viewport": {"width": 1440, "height": 700}},
    {"slug": "cohort-add-form", "go": entry("/private/stem/cohort/", "Active+Rat"), "viewport": {"width": 1440, "height": 620}},
    {"slug": "procedure-add-form", "go": RAT_IMPLANT},
    {"slug": "specimenset-add-form", "go": entry("/private/stem/specimenset/", "Coronal+Section+Series"), "full": True, "clip": "#content-main, main"},
    # The section series' form at its lineage: type and status, subject and source specimen set, the starting
    # conditions, quality and item count.
    {"slug": "specimen-set-form", "go": entry("/private/stem/specimenset/", "Coronal+Section+Series"), "pad": 18,
     "around": [field("type"), field("status"), field("subject"), field("source_specimen_set"), field("baseline_conditions"),
                field("quality"), field("item_count")]},
    {"slug": "specimen-session-form", "go": entry("/private/stem/session/", "Coronal+sections+-+Confocal"), "viewport": {"width": 1440, "height": 620}},
    {"slug": "experimentalinterface-add-form", "go": entry("/private/modules/experimentalinterface/", "Silicon")},
    # A fixation, the step the tutorial illustrates here.
    {"slug": "specimen-procedure-materials", "go": entry("/private/modules/specimenprocedure/", "immersion"), "clip": "section.inline-group.selected",
     "steps": [("click", "Materials ("), ("wait", 800)]},
    {"slug": "equipment-list", "go": "/private/modules/equipment/"},
    # The rat session's auditory stimulation (the tutorial's rat, with its interface filled).
    # Both forms in full, the description box as tall as its one line of text.
    {"slug": "data-storage-form", "go": entry("/private/personal_attributes/datastorage/", "Primary+Working"), "full": True, "css": SHORT_EDITOR_CSS},
    {"slug": "setup-form", "go": entry("/private/personal_attributes/setup/", "Rat+Electrophysiology+Rig"), "full": True, "css": SHORT_EDITOR_CSS},
    {"slug": "equipment-form", "go": entry("/private/modules/equipment/", "SmartBox")},
    # A silicon probe in stock, the tutorial's example.
    {"slug": "consumable-stock-form", "go": entry("/private/modules/consumablestock/", "Silicon")},
    {"slug": "behavioral-assay-form", "go": entry("/private/personal_attributes/behavioralassay/", "Novel+Object"), "viewport": {"width": 1440, "height": 640}},
    {"slug": "web-api-session-list", "go": "/api/private/stem/session/?per_page=3", "viewport": {"width": 1100, "height": 760}},
    {"slug": "2p-virus-injection-materials", "go": entry("/private/modules/procedure/", "Virus+injection+M08"), "clip": "section.inline-group.selected",
     "steps": [("click", "Materials ("), ("wait", 800)]},
    {"slug": "2p-cranial-window-interface", "go": entry("/private/modules/experimentalinterface/", "Cranial")},
    # Tutorial subjects and sessions: the add forms the steps describe, filled with each tutorial's example (not saved;
    # lists pick the demo project and its animals, which stand in for the tutorial's).
    # Getting started: the add forms the steps describe, filled in as the step says (not saved).
    {"slug": "get-started-project-form", "go": "/private/stem/project/add/", "around": FORM_CARD, "pad": 24,
     "steps": [("wait", 600), ("fill", "#id_name", "Hippocampal place cells 2026"), ("select2", "#id_authgroups", "SAMPLE"), ("wait", 500)]},
    # The project the guide's first step creates is not in the demo dataset: the demo project is picked (so the
    # subjects list loads) and shown under that project's name (stand_in_project).
    {"slug": "get-started-subject-form", "go": "/private/stem/subject/add/", "around": FORM_CARD, "pad": 24,
     "steps": [("wait", 600), ("fill", "#id_name", "SAMPLE Mouse M10 - Bruno"), ("select2", "#id_projects", "Neural dynamics"),
               ("select2", "#id_sex", "Male"), ("select2", "#id_species", "Mus musculus"), ("wait", 600),
               ("select2", "#id_strain", "C57BL/6J"), ("wait", 500), ("call", stand_in_project), ("wait", 300)]},
    {"slug": "get-started-session-form", "go": "/private/stem/session/add/", "around": FORM_CARD, "pad": 24,
     "steps": [("wait", 600), ("fill", "#id_name", "SAMPLE M09 Antonio - Shaping 02"), ("select2", "#id_projects", "Neural dynamics"),
               ("select2", "#id_subjects", "M09"), ("wait", 500), ("call", stand_in_project), ("wait", 300)]},
]


# Walkthroughs: short silent recordings of one step of a tutorial, recorded like the tour (see TOUR below): the
# camera starts framed on the form, a pointer works the controls, nothing is saved, and the clip ends on the
# button the step ends with. Each is written to docs/assets/images/walkthroughs/<slug>.webm with a poster .jpg.
WALKTHROUGHS: list[dict] = [
    # The form is taller than the screen: the camera glides down to the taxonomy once the top fields are done.
    {"slug": "get-started-create-subject", "go": "/private/stem/subject/add/", "steps": [
        ("frame", {"union": True, "targets": [field("name"), field("sex")]}, None, {"below": 160}), ("wait", 500),
        ("type", "#id_name", "SAMPLE Mouse M10 - Bruno"), ("select2", "#id_projects", "Neural dynamics"),
        ("select2", "#id_sex", "Male"), ("wait", 300),
        ("move", {"union": True, "targets": [field("species"), "button[name=_continue]"]}, None, {"ms": 900, "below": 40}),
        ("pick", "#id_species", "Mus musculus"), ("wait", 900),
        ("pick", "#id_strain", "C57BL/6J"), ("wait", 600), ("point", "button[name=_continue]"), ("wait", 1400)]},
    {"slug": "get-started-create-session", "go": "/private/stem/session/add/", "steps": [
        ("frame", {"union": True, "targets": FORM_CARD}, None, {"maxh": 700}), ("wait", 500),
        ("type", "#id_name", "SAMPLE M09 Antonio - Shaping 02"), ("select2", "#id_projects", "Neural dynamics"),
        ("select2", "#id_subjects", "M09"), ("wait", 600), ("point", "button[name=_continue]"), ("wait", 1400)]},
    # The rat's silicon probe implant, the procedure of the electrophysiology tutorial: its materials and the roles
    # Add material offers.
    {"slug": "ephys-procedure-materials", "go": RAT_IMPLANT, "prepare": [("click", "Materials ("), ("wait", 1200)], "steps": [
        ("frame", "#material_usages-group", None, {"maxh": 520}), ("wait", 900), ("point", "#material_usages-0"), ("wait", 900),
        ("click", "Add material"), ("wait", 1800), ("press", "body", "Escape"), ("wait", 900)]},
    {"slug": "specimen-create-set", "go": "/private/stem/specimenset/add/", "steps": [
        ("frame", {"union": True, "targets": FORM_CARD}, None, {"maxh": 700}), ("wait", 500),
        ("type", "#id_name", "M09 coronal hippocampal slices"), ("select2", "#id_projects", "Neural dynamics"),
        ("select2", "#id_subject", "M09"), ("wait", 600), ("point", "button[name=_continue]"), ("wait", 1400)]},
]
WALKTHROUGH_OUT = REPO_ROOT / "docs" / "assets" / "images" / "walkthroughs"


def do_step(page, step):
    if step[0] == "click":
        page.get_by_text(step[1], exact=False).first.click(timeout=8000)
    elif step[0] == "click_sel":
        page.locator(step[1]).first.click(timeout=8000)
    elif step[0] == "click_force":
        page.locator(step[1]).first.click(timeout=8000, force=True)
    elif step[0] == "js":
        page.evaluate(step[1])
    elif step[0] == "wait":
        page.wait_for_timeout(step[1])
    elif step[0] == "fill":
        page.fill(step[1], step[2])
    elif step[0] == "type":
        page.click(step[1])
        page.type(step[1], step[2], delay=45)
    elif step[0] == "press":
        page.keyboard.press(step[2])
    elif step[0] == "hover":
        page.locator(f"button:has-text('{step[1]}'), input[type=submit][value='{step[1]}'], a.button:has-text('{step[1]}')").last.hover(timeout=8000)
    elif step[0] == "scroll":
        page.mouse.wheel(0, step[1])
    elif step[0] == "select":
        page.locator(step[1]).first.select_option(label=step[2])
    elif step[0] == "call":
        step[1](page)
    elif step[0] == "scroll_to":
        page.locator(step[1]).first.scroll_into_view_if_needed(timeout=8000)
        page.mouse.wheel(0, -150)
    elif step[0] == "wait_gone":
        remaining = step[2]
        while remaining > 0:
            visible = [t for t in step[1] if page.locator(f"text={t}").count() and page.locator(f"text={t}").first.is_visible()]
            if not visible:
                break
            page.wait_for_timeout(500)
            remaining -= 500
    elif step[0] == "open_select2":
        page.locator(f"{step[1]} + .select2").first.click(timeout=8000)
        page.wait_for_timeout(300)
        field = page.locator(".select2-container--open .select2-search__field").first
        if field.count():
            field.type(step[2], delay=60)
        page.wait_for_timeout(1200)
    elif step[0] == "select2":
        page.locator(f"{step[1]} + .select2").first.click(timeout=8000)
        page.wait_for_timeout(300)
        # Typed into the list's search box when it has one (a short list has none).
        search = page.locator(".select2-container--open .select2-search:not(.select2-search--hide) .select2-search__field").first
        if search.count() and search.is_visible():
            search.type(step[2], delay=60)
        page.wait_for_timeout(900)
        # The option itself: the exact label, else the first starting with the text, else the first containing it
        # ("Male" is also inside "Female"); scrolled to in the list, highlighted and taken with Enter.
        options = page.locator(".select2-container--open .select2-results__option")
        text = re.escape(step[2])
        for pattern in (rf"^\s*{text}\s*$", rf"^\s*{text}", text):
            match = options.filter(has_text=re.compile(pattern, re.I))
            if match.count():
                match.first.scroll_into_view_if_needed()
                match.first.hover()
                page.wait_for_timeout(150)
                break
        page.keyboard.press("Enter")
        # A list still open after the pick (one that takes several values) is closed; its highlighted option is the
        # one just picked, so closing changes nothing.
        page.wait_for_timeout(250)
        if page.locator(f"{step[1]} + .select2.select2-container--open").count():
            page.keyboard.press("Escape")


def recording_context(browser):
    """A browser context for the tour and the walkthroughs: the tour's viewport and pixel density, the sidebar
    collapsed, the debug toolbar hidden from the first paint, number fields as text, and every request that would
    change a record refused (forms autosave as fields change; a recording only shows)."""
    context = browser.new_context(viewport=TOUR_VIEWPORT, device_scale_factor=TOUR_SCALE, user_agent=USER_AGENT, locale=LOCALE)
    context.add_init_script(NUMBER_FIELDS_JS)
    # The interface stores "true" for a collapsed sidebar.
    context.add_init_script("try { localStorage.setItem('django.admin.navSidebarIsOpen', 'true'); } catch (e) {}"
                            " document.addEventListener('DOMContentLoaded', () => { if (!document.head) return;"
                            " const s = document.createElement('style'); s.textContent = '" + HIDE_CSS + "';"
                            " document.head.appendChild(s); });")
    page = context.new_page()
    login(page)
    page.close()
    context.route("**/*", lambda route: route.abort() if route.request.method in ("PATCH", "PUT", "DELETE")
                  or "_method=" in route.request.url else route.continue_())
    return context


def record_walkthroughs(p, slugs: list[str]) -> tuple[list, list]:
    done, failed = [], []
    wanted = [w for w in WALKTHROUGHS if not slugs or w["slug"] in slugs]
    if not wanted:
        return done, failed
    ffmpeg = find_ffmpeg()
    if not ffmpeg:
        return done, [("walkthroughs", "no ffmpeg to encode the clips")]
    WALKTHROUGH_OUT.mkdir(parents=True, exist_ok=True)
    browser = p.chromium.launch()
    context = recording_context(browser)
    for walk in wanted:
        page = context.new_page()
        try:
            record_chapter(page, {"shots": [walk]}, ffmpeg, WALKTHROUGH_OUT / f"{walk['slug']}.webm")
            done.append(walk["slug"])
            print(f"ok      {walk['slug']} (walkthrough)")
        except Exception as error:  # noqa: BLE001
            failed.append((walk["slug"], str(error).splitlines()[0][:140]))
            print(f"FAILED  {walk['slug']} (walkthrough): {str(error).splitlines()[0][:140]}")
        finally:
            page.close()
    context.close()
    browser.close()
    return done, failed


# The tour on the landing page: one short clip per key feature, played in sequence above the feature list. A chapter
# is a list of shots; a shot opens a screen (`go`, a path or callable(page) -> path; none stays on a blank page),
# readies it unrecorded (`prepare`) and runs its `steps`, then its `after` steps unrecorded. Only what follows a
# ("frame", targets, caption[, options]) step is recorded, so every shot starts with one: it points the camera at the
# targets at once, never zooming in from the whole page, and the clip cuts from the previous framing to it. Targets
# are a selector, a list of fallbacks (the first with a visible match) or, with {"union": True}, a list whose every
# entry (a selector or its fallbacks) is framed together; None frames the whole screen. Options: max zoom, pad (screen
# pixels kept around the targets) and maxh (CSS pixels of a tall target to keep). More tour steps: ("mark", selector
# or fallbacks, tag[, ms]) outlines one element with a short tag beside it, replacing the previous mark, and ("pause",)
# stops recording until the next frame, for a wait the viewer need not watch. A mark's tag goes above the element, left of
# a table cell, or where a fifth item says ("below", "left", "right", "inset"). Captions are not drawn into the clip:
# each frame's caption is a cue in docs/_data/tour.yml, shown under the video from that moment. Clips go to
# docs/assets/images/walkthroughs/tour/<nn>-<slug>.webm with a poster <nn>-<slug>.jpg (the end of the first shot).
# "doc" is the documentation page the player links to under the clip, with "link" as the link text.
TOUR_VIEWPORT = {"width": 1200, "height": 750}  # smaller than the screenshots', so the interface reads at less zoom
TOUR_SCALE = 2  # device pixels per CSS pixel: zoomed text stays sharp


def choose(page, css: str, text: str):
    """Pick the first option of a <select> whose label contains `text`, also when Select2 hides the select."""
    page.locator(css).first.evaluate("""(s, text) => {
        const o = [...s.options].find(o => o.textContent.toLowerCase().includes(text.toLowerCase()));
        if (!o) return;
        s.value = o.value;
        // Select2 may be bound through the page's jQuery or Django's; a jQuery trigger also fires native listeners.
        const $ = window.jQuery || (window.django && django.jQuery);
        if ($) { $(s).trigger('change'); } else { s.dispatchEvent(new Event('change', {bubbles: true})); }
    }""", text)


def open_assistant(page):
    """Open the assistant drawer, once its launcher is back after a drawer left open was closed."""
    if not page.locator(".brainstem-assistant__drawer.is-open").count():
        page.locator(".brainstem-assistant__launcher").first.click(timeout=15000)
    page.locator(".brainstem-assistant__drawer.is-open textarea").first.wait_for(state="visible", timeout=8000)


CODE_SNIPPET = ('from brainstem_api_tools import BrainstemClient\n\n'
                'client = BrainstemClient()\n'
                'response = client.load("session", filters={"name.icontains": "Reversal"})\n'
                'response.json()["sessions"][0]')
SESSION_QUERY = "/api/private/stem/session/?per_page=1&filter%7Bname.icontains%7D=Reversal"
CODE_CARD = """<!doctype html><html><head><meta charset="utf-8"><style>
html, body { margin: 0; height: 100%; background: #f4f1f8; font-family: """ + 'Inter,"Segoe UI",Helvetica,Arial,sans-serif' + """; }
.wrap { box-sizing: border-box; height: 100%; padding: 44px 64px; display: grid; grid-template-rows: auto 1fr; gap: 24px; }
.card { background: #1d1430; border-radius: 16px; box-shadow: 0 12px 32px rgba(38, 22, 58, .25); overflow: hidden; }
.bar { padding: 12px 22px; color: #cbb8e4; font-weight: 600; font-size: 17px; border-bottom: 1px solid #33264d; }
pre { margin: 0; padding: 18px 24px; font: 20px/1.5 "SFMono-Regular", Menlo, Consolas, monospace; color: #f2ecfa; white-space: pre-wrap; }
.out { opacity: 0; transition: opacity .5s ease; } .out.on { opacity: 1; }
</style></head><body><div class="wrap">
<div class="card"><div class="bar">Python</div><pre id="code"> </pre></div>
<div class="card out" id="out"><div class="bar">Response (excerpt)</div><pre>__JSON__</pre></div>
</div><script>
const code = __CODE__;
window.tourType = () => {
    const el = document.getElementById('code'); let i = 0;
    const tick = () => { el.textContent = code.slice(0, ++i);
        if (i < code.length) { setTimeout(tick, 18); } else { setTimeout(() => document.getElementById('out').classList.add('on'), 350); } };
    tick();
};
</script></body></html>"""


def code_card(page):
    """A Python call to the REST API and an excerpt of what the server returns for it, from the demo dataset."""
    import html
    import json
    data = page.request.get(BASE + SESSION_QUERY, headers={"Accept": "application/json"}).json()
    record = data["sessions"][0]
    keys = ["id", "name", "session_type", "date_time", "subjects", "projects", "dataacquisition", "behaviors", "epochs"]
    excerpt = {k: (record[k][:2] if isinstance(record[k], list) else record[k]) for k in keys if k in record}
    text = json.dumps(excerpt, indent=2, ensure_ascii=False)
    found = set(EMAIL.findall(text)) - {USER} - ALLOWED_EMAILS
    if found:
        raise RuntimeError(f"the API response shows another account's email ({', '.join(sorted(found))})")
    page.goto("about:blank")  # not over a BrainSTEM page, whose content security policy blocks the card's script
    page.set_content(CODE_CARD.replace("__JSON__", html.escape(text)).replace("__CODE__", json.dumps(CODE_SNIPPET)))


SESSION_R02 = entry("/private/stem/session/", "R02+Steve+Reversal+01", "")
PROJECT = "Neural+dynamics"
ROLE_CELL = "table:has(th:has-text('Contributor')) tr:has(td) >> nth=0 >> td >> nth={}"
IMPORT_STATUS = "table:visible tbody tr >> nth={} >> .guided-import-editor__row-status"
GRID = "table:visible tbody tr >> nth={} >> td >> nth={} >> {}"  # row, column, control of the import grid
DIALOG = ["dialog[open]", "[role=dialog]:visible", ".modal-content:visible", "text=Make this project public?"]
LAST_CANCEL = "button:has-text('Cancel') >> visible=true >> nth=-1"


def import_grid_rows(page):
    """The batch-entry grid of subjects with two empty rows, each with the status Active (a column off the screen)."""
    page.locator("button:has-text('Subjects')").first.click()
    page.wait_for_timeout(700)
    grid = page.locator("table:visible").first
    for _ in range(2 - grid.locator("tbody tr").count()):
        page.get_by_text("Add row", exact=True).first.click()
        page.wait_for_timeout(200)
    for index in range(2):
        select_by_text(grid.locator("tbody tr").nth(index).locator("td").nth(6).locator("select"), "Active")


def click_public(page):
    """Flip the project's visibility switch to Public, with the pointer: its label, else the radio button itself."""
    label = page.locator("label[for=id_is_public_1]").locator("visible=true").first
    target = label if label.count() else page.locator("#id_is_public_1").first
    point(page, target, click=True)
    if label.count():
        label.click()
    else:
        target.evaluate("e => e.click()")


# The card the tour opens on, before the first feature: what BrainSTEM is, not yet any feature.
TOUR_INTRO = {"title": "BrainSTEM at a glance",
              "text": "An electronic lab notebook for experimental neuroscience. A short tour of its key features follows."}
TOUR = [
    {"slug": "records", "link": "See the data model", "title": "Complete experimental records",
     "text": "A procedure filled in field by field, placed in the atlas, and the sessions that follow", "doc": "/datamodel/",
     "shots": [
         # A new silicon probe implant filled in field by field, down to its coordinates (nothing is saved).
         {"go": "/private/modules/procedure/add/", "prepare": [("wait", 600)],
          "steps": [("frame", field("type"), "Every procedure, recording and log has a type", {"below": 240, "max": 1.8}),
                    ("wait", 400), ("select2", "#id_type", "Silicon probe"), ("wait", 1200),
                    ("move", {"union": True, "targets": [field("subject"), field("target_regions")]},
                     "Link it to its subject, setup, atlas and target brain region", {"ms": 1000, "below": 200}),
                    ("select2", "#id_subject", "R06"), ("wait", 300),
                    ("select2", "#id_equipment_setup", "Rat Electrophysiology"), ("wait", 300),
                    ("select2", "#id_target_regions_atlas", "Waxholm"), ("wait", 900),
                    # Target regions takes several values, so its list stays open after a pick.
                    ("optional", ("select2", "#id_target_regions", "CA1")), ("wait", 700), ("press", "body", "Escape"), ("wait", 500),
                    ("move", {"union": True, "targets": ["#id_coordinates + .select2", 'input[name="root.depth[value]"]']},
                     "Each type adds its own fields: here the implant's stereotaxic coordinates", {"ms": 1400, "below": 30}),
                    # The default system (Bregma-based surface coordinates with depth) is the implant's.
                    ("point", "#id_coordinates + .select2"), ("wait", 600),
                    ("type", 'input[name="root.apCoordinate[value]"]', "-3.6"),
                    ("type", 'input[name="root.mlCoordinate[value]"]', "2.4"),
                    ("type", 'input[name="root.depth[value]"]', "2.7"), ("wait", 1000)]},
         # The saved implant with the same coordinates, in the atlas (which loads unrecorded).
         {"go": RAT_IMPLANT, "prepare": [("click_sel", "[data-coordinate-preview-button]"), ("wait_gone", VIEWER_LOADING, 120000), ("wait", 800)],
          "steps": [("frame", ".coordinate-preview-modal__modal", "Its coordinates place the implant in the rat brain atlas"),
                    ("wait", 1000), ("click", "Coronal"), ("wait", 2800)]},
         {"go": SESSION_R02, "prepare": [("click", "Epochs ("), ("wait", 1200)],
          "steps": [("frame", ".epochs-timeline", "Sessions with the implanted rat line up their epochs, behavior and recordings",
                     {"maxh": 520}), ("wait", 800),
                    ("click_sel", ".epoch-timeline__mode[data-mode=kind]"), ("wait", 2000),
                    ("click_sel", ".epoch-timeline__mode[data-mode=epoch]"), ("wait", 1300)]}]},
    {"slug": "compliance", "link": "Learn about permissions", "title": "Collaboration and compliance",
     "text": "Roles for people and groups, procedure episodes with severity and licenses", "doc": "/datamodel/permissions/",
     "shots": [
         {"go": entry("/private/stem/project/", PROJECT, "manage/"),
          "steps": [("frame", "table:has(th:has-text('Contributor'))", "Projects share their records with people and groups, by role",
                     {"pad": 70, "below": 60}), ("wait", 600),
                    # The group's checkbox under each role, tagged below it, where the table ends.
                    ("mark", ROLE_CELL.format(1), "Add and edit", 1800, "below"),
                    ("mark", ROLE_CELL.format(2), "Manage members", 1800, "below"),
                    ("mark", ROLE_CELL.format(3), "Full control", 2000, "below")]},
         # No list is opened here: closing a Select2 list picks its highlighted option, which would show (and,
         # without the guard in record_tour, autosave) a severity the episode does not have.
         {"go": entry("/private/modules/procedureepisode/", "R02+Steve+Electrophysiology"),
          "steps": [("frame", {"union": True, "targets": [field("intervention_class"), field("severity"), field("licenses")]},
                     "Procedure episodes record their severity and licenses"), ("wait", 600),
                    ("mark", field("intervention_class"), "Intervention class", 1700),
                    ("mark", field("severity"), "Severity", 1800), ("mark", field("licenses"), "Licenses", 1900)]}]},
    {"slug": "resources", "link": "More about the probe catalog", "title": "Shared resources and taxonomies",
     "text": "A shared catalog of probe designs, devices and reagents, and taxonomies of species and strains",
     "doc": "/webinterface/probe-catalog/",
     "shots": [
         {"go": "/private/resources/consumable/?q=Buzsaki",
          "steps": [("frame", "#result_list", "A shared catalog of consumables, with hundreds of probe designs", {"maxh": 420}),
                    ("wait", 600), ("mark", "#result_list tbody tr:first-child", "One probe design", 1800)]},
         {"go": entry("/private/resources/consumable/", "A16x8-5mm-berg-200-160", "schematic.svg"), "prepare": [("wait", 800)],
          "steps": [("frame", None, "Each design is drawn from its geometry"), ("wait", 2600)]},
         # The strain list opens filtered to the species, and closes unchanged.
         {"go": entry("/private/stem/subject/", "M09+Antonio"),
          "steps": [("frame", {"union": True, "targets": [field("species"), field("strain")]},
                     "Species and strains come from shared taxonomies", {"below": 200}), ("wait", 500),
                    ("open_select2", "#id_strain", "C57"), ("wait", 1500), ("press", "body", "Escape"), ("wait", 400)]}]},
    {"slug": "open-science", "link": "How to share a project publicly", "title": "Open science",
     "text": "Public projects, JSON exports for NWB conversion, and STAR Methods reports",
     "doc": "/tutorials/sharing-project-publicly/",
     "shots": [
         # Cancel closes the dialog: the project stays private (Escape in `after` in case it is still open).
         {"go": entry("/private/stem/project/", PROJECT),
          "steps": [("frame", field("is_public"), "Make a project public in one step", {"pad": 70}), ("wait", 500),
                    ("call", click_public), ("wait", 1000),
                    ("frame", DIALOG, "Its records then appear on the public portal and API"), ("wait", 1600),
                    ("click_sel", LAST_CANCEL), ("wait", 700)],
          "after": [("press", "body", "Escape")]},
         {"go": entry("/private/stem/project/", PROJECT, "download/"), "viewport": {"width": 960, "height": 600},
          "steps": [("frame", ".form__wrapper", "Download a whole project, or one session to convert to NWB", {"maxh": 420}),
                    ("wait", 500), ("mark", field("export_format"), "JSON", 1700, "inset"),
                    ("pick", "#session", "Reversal 01"), ("wait", 500),
                    ("mark", field("session"), "One session, one NWB file", 2000, "inset")]},
         {"go": entry("/private/stem/project/", PROJECT, "export/?format=html&mode=star_methods"),
          "steps": [("frame", "table:has(th:has-text('Identifier'))", "A STAR Methods draft with the RRIDs for your paper",
                     {"maxh": 360}), ("wait", 600), ("mark", "th:has-text('Identifier')", "RRIDs", 1700),
                    ("optional", ("move", "table:has(th:has-text('Identifier')) tbody tr >> nth=5", None, {"ms": 2600})),
                    ("wait", 800)]}]},
    {"slug": "programmable", "link": "Explore the API", "title": "Programmable and AI ready",
     "text": "Every record through the REST API, and plain-language search with the AI assistant", "doc": "/api/",
     "shots": [
         {"prepare": [("call", code_card)],
          "steps": [("frame", None, "Every record through the REST API, from Python or MATLAB"),
                    ("js", "window.tourType()"), ("wait", 6000)]},
         # The question box with its examples and Search button, not the whole drawer, which is taller than the screen.
         # The shot stops before the search: on the development server the assistant's searches still fail or come
         # back empty. Where they work, add after the typing, so the wait for the answer is cut:
         #   ("click_sel", ".brainstem-assistant__submit"), ("pause",),
         #   ("call", lambda p: p.wait_for_selector(".brainstem-assistant__loading", state="hidden", timeout=90000)),
         #   ("frame", ".brainstem-assistant__drawer", "It answers with the matching records"), ("wait", 3400)
         # Over the subjects list: the dashboard's activity widgets name other people.
         {"go": "/private/stem/subject/", "prepare": [("call", open_assistant), ("wait", 1000)],
          "steps": [("frame", {"union": True, "targets": [".brainstem-assistant__examples", ".brainstem-assistant__submit"]},
                     "The AI assistant offers plain-language, semantic search of your records", {"max": 1.7}),
                    ("wait", 400), ("type", "[class*=brainstem-assistant] textarea", "Reversal sessions of mouse M09"),
                    ("wait", 1800)],
          "after": [("click_sel", ".brainstem-assistant__close")]}]},
    {"slug": "integrations", "link": "Learn about the import tool", "title": "Integrations",
     "text": "Batch entry and CSV import, every row checked before anything is created", "doc": "/webinterface/import-tool/",
     "shots": [
         # Two rows entered field by field: one complete (new), one without species (blocked).
         {"go": "/private/import-tool/", "prepare": [("wait", 600), ("call", import_grid_rows), ("wait", 400)],
          "steps": [("frame", "table:visible", "Enter rows one field at a time, or paste them from a spreadsheet",
                     {"below": 40}), ("wait", 400),
                    ("pick", GRID.format(0, 1, "select"), "Neural dynamics"),
                    ("type", GRID.format(0, 2, "input"), "SAMPLE Mouse M10 - Bruno II"),
                    ("pick", GRID.format(0, 3, "select"), "Male"),
                    ("pick", GRID.format(0, 4, "select"), "Mus musculus"), ("wait", 400),
                    ("pick", GRID.format(0, 5, "select"), "C57BL/6J"),
                    ("pick", GRID.format(1, 1, "select"), "Neural dynamics"),
                    ("type", GRID.format(1, 2, "input"), "SAMPLE Mouse M11 - Lola"),
                    ("pick", GRID.format(1, 3, "select"), "Female"), ("wait", 300),
                    ("click", "Validate current tab"), ("wait", 1600),
                    # Validation adds a summary above the grid: the camera follows the grid down.
                    ("move", "table:visible", "Each row is checked before anything is imported", {"ms": 700, "below": 40}),
                    ("mark", IMPORT_STATUS.format(0), "Ready to create", 1900, "right"),
                    ("mark", IMPORT_STATUS.format(1), "Needs a fix", 2100, "right")]}]},
]
# Where the link under the video points while a shot plays (by the shot's caption); the chapter's own `doc` otherwise.
SHOT_LINKS = {
    "Every procedure, recording and log has a type": ("/datamodel/modules/procedure/", "About procedures"),
    "Link it to its subject, setup, atlas and target brain region": ("/webinterface/forms/", "How forms work"),
    "Each type adds its own fields: here the implant's stereotaxic coordinates": ("/webinterface/atlases-and-coordinates/", "More about coordinates"),
    "Its coordinates place the implant in the rat brain atlas": ("/webinterface/atlases-and-coordinates/", "More about atlases and coordinates"),
    "Sessions with the implanted rat line up their epochs, behavior and recordings": ("/datamodel/stem/epoch/", "About epochs"),
    "Projects share their records with people and groups, by role": ("/datamodel/permissions/", "Learn about permissions"),
    "Procedure episodes record their severity and licenses": ("/datamodel/modules/procedureepisode/", "About procedure episodes"),
    "A shared catalog of consumables, with hundreds of probe designs": ("/webinterface/probe-catalog/", "More about the probe catalog"),
    "Each design is drawn from its geometry": ("/webinterface/probe-catalog/", "More about the probe catalog"),
    "Species and strains come from shared taxonomies": ("/datamodel/taxonomies/", "About taxonomies"),
    "Make a project public in one step": ("/tutorials/sharing-project-publicly/", "How to share a project publicly"),
    "Its records then appear on the public portal and API": ("/tutorials/sharing-project-publicly/", "How to share a project publicly"),
    "Download a whole project, or one session to convert to NWB": ("/tutorials/exporting-to-nwb/", "How to export to NWB"),
    "A STAR Methods draft with the RRIDs for your paper": ("/webinterface/exports-and-reports/", "More about exports and reports"),
    "Every record through the REST API, from Python or MATLAB": ("/api/", "Explore the API"),
    "The AI assistant offers plain-language, semantic search of your records": ("/webinterface/ai-assistant/", "About the AI assistant"),
    "Enter rows one field at a time, or paste them from a spreadsheet": ("/webinterface/import-tool/", "Learn about the import tool"),
    "Each row is checked before anything is imported": ("/webinterface/import-tool/", "Learn about the import tool"),
}
TOUR_OUT = WALKTHROUGH_OUT / "tour"
TOUR_DATA = REPO_ROOT / "docs" / "_data" / "tour.yml"
FFMPEG_GLOB = "~/Library/Caches/ms-playwright/ffmpeg-*/ffmpeg-*"  # Playwright's own ffmpeg, which encodes VP8
TOUR_FONT = 'Inter,"Segoe UI",Helvetica,Arial,sans-serif'
# The camera: scale and move the page so the targets fill the screen around their centre, at once or (ms) gliding
# from where it was. Across, the shot widens to the whole card, panel, dialog or table the targets sit in, so the
# screen's edges never cut through a neighbouring field or column; down, it keeps to the targets (plus `below` pixels,
# room for a list that opens under a field). The camera moves <body> rather than scrolling, so it can glide anywhere
# in the page; a target inside a fixed element (a drawer, a dialog) moves with that element instead. The page is never
# zoomed out, and <body> keeps covering the screen. Positions are measured without the current framing, which the
# reader never sees, as nothing is drawn while the script runs.
TOUR_CAMERA_JS = """({els, max, pad, maxh, below, ms}) => {
    if (!document.body) return;
    const vw = innerWidth, vh = innerHeight;
    const zoomed = [...document.querySelectorAll('[data-docs-tour-zoom]')];
    const was = new Map(zoomed.map(z => [z, z.style.transform]));
    zoomed.forEach(z => { z.style.transition = 'none'; z.style.transform = z.dataset.docsTourZoom; });
    let el = document.body, goal = null;
    window.__docsTourCam = null;
    if (els.length) {
        let fixed = null;
        for (let n = els[0]; n && n !== document.body; n = n.parentElement) { if (getComputedStyle(n).position === 'fixed') fixed = n; }
        el = fixed || document.body;
        const rects = els.map(e => e.getBoundingClientRect());
        const x0 = Math.min(...rects.map(r => r.left)), x1 = Math.max(...rects.map(r => r.right));
        const y0 = Math.min(...rects.map(r => r.top));
        const y1 = Math.min(Math.max(...rects.map(r => r.bottom)) + below, y0 + maxh);
        // The enclosing box: the nearest ancestor spanning the targets that is drawn as a box (a border on both
        // sides, a shadow or a background) and tall enough not to be a single input; none, and the shot spans the
        // screen.
        const boxed = n => { const c = getComputedStyle(n), r = n.getBoundingClientRect();
            if (r.height < 120 && !['TABLE', 'DIALOG'].includes(n.tagName)) return false;
            return ['TABLE', 'DIALOG', 'FIELDSET'].includes(n.tagName) || c.boxShadow !== 'none' || c.position === 'fixed'
                || (parseFloat(c.borderLeftWidth) > 0 && parseFloat(c.borderRightWidth) > 0)
                || !['rgba(0, 0, 0, 0)', 'transparent'].includes(c.backgroundColor); };
        let left = 0, right = vw;
        for (let n = els[0]; n && n !== document.body && n !== document.documentElement; n = n.parentElement) {
            const r = n.getBoundingClientRect();
            if (r.left <= x0 + 1 && r.right >= x1 - 1 && r.width <= vw && boxed(n)) { left = r.left; right = r.right; break; }
        }
        const s = Math.max(1, Math.min(max, (vw - 2 * pad) / (right - left), (vh - 2 * pad) / (y1 - y0)));
        let tx = vw / 2 - s * (left + right) / 2, ty = vh / 2 - s * (y0 + y1) / 2;
        if (!fixed) {
            const doc = document.documentElement;
            tx = Math.min(s * scrollX, Math.max(vw - s * (doc.scrollWidth - scrollX), tx));
            ty = Math.min(s * scrollY, Math.max(vh - s * (doc.scrollHeight - scrollY), ty));
            window.__docsTourCam = {s, tx, ty, ox: scrollX, oy: scrollY};
        }
        if (s > 1.001 || Math.abs(tx) > 0.5 || Math.abs(ty) > 0.5) {
            const own = el.getBoundingClientRect();
            if (el.dataset.docsTourZoom === undefined) el.dataset.docsTourZoom = el.style.transform;
            // Origin at the screen's top-left corner, so a screen point p lands on s * p + t.
            el.style.transformOrigin = (-own.left) + 'px ' + (-own.top) + 'px';
            goal = 'translate(' + tx + 'px,' + ty + 'px) scale(' + s + ')';
        }
    }
    zoomed.forEach(z => { if (z !== el) { delete z.dataset.docsTourZoom; } });
    const rest = el.dataset.docsTourZoom || '';
    if (ms) {
        el.style.transform = was.has(el) ? was.get(el) : rest;
        el.getBoundingClientRect();
        el.style.transition = 'transform ' + ms + 'ms cubic-bezier(.45,0,.2,1)';
    }
    el.style.transform = goal || rest;
    if (!goal) delete el.dataset.docsTourZoom;
}"""
# Select2 places its open list in <body> at the field's screen position, which a zoomed <body> scales a second time:
# while the camera has moved <body>, the list is put back under its field every frame.
TOUR_SELECT2_JS = """() => {
    if (window.__docsTourSelect2) return;
    window.__docsTourSelect2 = true;
    const step = () => {
        const cam = window.__docsTourCam, drop = document.querySelector('body > .select2-container--open');
        const anchor = drop && [...document.querySelectorAll('.select2-container--open')].find(c => c.parentElement !== document.body);
        if (cam && anchor) {
            const r = anchor.getBoundingClientRect(), list = drop.querySelector('.select2-dropdown');
            drop.style.left = (cam.ox + (r.left - cam.tx) / cam.s) + 'px';
            drop.style.top = (cam.oy + (r.bottom - cam.ty) / cam.s) + 'px';
            if (list) list.style.width = (r.width / cam.s) + 'px';
        }
        requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
}"""
# The pointer: an arrow that glides to the control about to be used, with a ripple where it clicks. It hangs off
# <html>, so the camera does not move it.
TOUR_POINTER_JS = """({x, y, ms, click}) => {
    let c = document.getElementById('docs-tour-pointer');
    if (!c) {
        c = document.createElement('div'); c.id = 'docs-tour-pointer';
        c.innerHTML = '<svg width="30" height="30" viewBox="0 0 24 24"><path d="M5 2.5l14 10.2-6.1 1.1-3.4 5.7z" '
            + 'fill="#1d1430" stroke="#fff" stroke-width="1.6" stroke-linejoin="round"/></svg>';
        c.style.cssText = 'position:fixed;left:0;top:0;z-index:2147483647;pointer-events:none;'
            + 'filter:drop-shadow(0 2px 3px rgba(0,0,0,.35));transform:translate(' + (innerWidth * .55) + 'px,' + (innerHeight * .9) + 'px)';
        document.documentElement.appendChild(c);
        c.getBoundingClientRect();
    }
    c.style.transition = 'transform ' + ms + 'ms cubic-bezier(.45,0,.2,1)';
    c.style.transform = 'translate(' + (x - 6) + 'px,' + (y - 3) + 'px)';
    if (!click) return;
    setTimeout(() => {
        const r = document.createElement('div');
        r.style.cssText = 'position:fixed;z-index:2147483646;pointer-events:none;left:' + (x - 20) + 'px;top:' + (y - 20) + 'px;'
            + 'width:40px;height:40px;border-radius:50%;background:rgba(129,34,161,.35);transform:scale(.3);'
            + 'transition:transform .45s ease-out,opacity .45s ease-out';
        document.documentElement.appendChild(r);
        r.getBoundingClientRect();
        r.style.transform = 'scale(1.4)'; r.style.opacity = '0';
        setTimeout(() => r.remove(), 500);
    }, ms);
}"""
# A mark: an outline round one element and a tag beside it, never over the element: above it (below when there is no
# room, or "below"), beside a table cell ("left" or "right"), or inside the top right corner of a wide form row
# ("inset"). Both fade in; a new mark replaces the previous one.
TOUR_MARK_JS = """({box, tag, place}) => {
    document.querySelectorAll('.docs-tour-mark').forEach(el => el.remove());
    const show = el => { el.style.opacity = '0'; el.style.transition = 'opacity .3s ease, transform .3s ease';
        document.documentElement.appendChild(el); return el; };
    const ring = document.createElement('div'); ring.className = 'docs-tour-mark';
    ring.style.cssText = 'position:fixed;z-index:2147483645;pointer-events:none;border:3px solid #ffc43d;border-radius:10px;'
        + 'box-shadow:0 0 0 4px rgba(255,196,61,.25);left:' + (box.x - 6) + 'px;top:' + (box.y - 6) + 'px;width:'
        + (box.width + 12) + 'px;height:' + (box.height + 12) + 'px';
    show(ring).style.transform = 'scale(1.06)';
    let label = null;
    if (tag) {
        label = document.createElement('div'); label.className = 'docs-tour-mark'; label.textContent = tag;
        label.style.cssText = 'position:fixed;z-index:2147483646;pointer-events:none;padding:5px 12px;border-radius:8px;'
            + 'background:#ffc43d;color:#2a1a00;font:700 20px/1.2 """ + TOUR_FONT.replace('"', '\\"') + """;white-space:nowrap;'
            + 'box-shadow:0 4px 12px rgba(0,0,0,.18)';
        show(label);
        if (place === 'inset') {
            label.style.left = (box.x + box.width - label.offsetWidth - 4) + 'px';
            label.style.top = (box.y + 2) + 'px';
        } else if (place === 'left' || place === 'right') {
            // The side asked for, else the other one when it would run off the screen.
            const before = box.x - 6 - 10 - label.offsetWidth, after = box.x + box.width + 6 + 10;
            const fits = after + label.offsetWidth < innerWidth - 8;
            label.style.left = ((place === 'left' && before > 8) || !fits ? before : after) + 'px';
            label.style.top = (box.y + box.height / 2 - label.offsetHeight / 2) + 'px';
        } else {
            const above = box.y - 6 - 8 - label.offsetHeight;
            label.style.top = (place !== 'below' && above > 6 ? above : box.y + box.height + 6 + 8) + 'px';
            label.style.left = Math.max(8, Math.min(innerWidth - label.offsetWidth - 8, box.x - 6)) + 'px';
        }
    }
    ring.getBoundingClientRect();
    ring.style.opacity = '1'; ring.style.transform = 'scale(1)';
    if (label) label.style.opacity = '1';
}"""
TOUR_UNMARK_JS = "() => document.querySelectorAll('.docs-tour-mark').forEach(el => el.remove())"

# The text a viewer can read: text in the viewport that nothing covers (a dialog's backdrop hides the page under it),
# and the values of visible fields. The options of a closed <select> are not drawn.
ON_SCREEN_TEXT_JS = """() => {
    const out = [], walker = document.createTreeWalker(document.body || document.documentElement, NodeFilter.SHOW_TEXT);
    for (let node; (node = walker.nextNode());) {
        const el = node.parentElement;
        if (!el || !node.textContent.trim() || el.closest('option, script, style, template, noscript')) continue;
        const range = document.createRange(); range.selectNodeContents(node);
        for (const r of range.getClientRects()) {
            const x = r.left + r.width / 2, y = r.top + r.height / 2;
            if (x < 0 || y < 0 || x > innerWidth || y > innerHeight) continue;
            const hit = document.elementFromPoint(x, y);
            if (hit && (el.contains(hit) || hit.contains(el))) { out.push(node.textContent); break; }
        }
    }
    document.querySelectorAll('input, textarea').forEach(f => {
        const r = f.getBoundingClientRect();
        if (f.type !== 'hidden' && r.width && r.bottom > 0 && r.top < innerHeight) out.push(f.value || '');
    });
    return out.join('\\n');
}"""


def check_no_foreign_email_on_screen(page):
    """check_no_foreign_email for what is on the screen of a tour shot, rather than the whole page."""
    found = {e.lower() for e in EMAIL.findall(page.evaluate(ON_SCREEN_TEXT_JS))} - {USER.lower()} - ALLOWED_EMAILS
    if found:
        raise RuntimeError(f"the shot shows another account's email ({', '.join(sorted(found))})")


def find_ffmpeg() -> str:
    import glob
    import shutil
    return shutil.which("ffmpeg") or next(iter(sorted(glob.glob(os.path.expanduser(FFMPEG_GLOB)))), "")


def first_visible(page, selectors):
    """The first visible match of a selector or of a list of fallbacks, or None."""
    for selector in ([selectors] if isinstance(selectors, str) else selectors):
        match = page.locator(selector).locator("visible=true").first
        if match.count():
            return match
    return None


def frame(page, targets, options: dict, ms: int = 0):
    """Point the camera at `targets` (see TOUR): at once, or gliding there over `ms`."""
    page.evaluate(TOUR_UNMARK_JS)
    if isinstance(targets, dict):
        matches = [first_visible(page, t) for t in targets["targets"]]
    else:
        matches = [first_visible(page, targets)] if targets else []
    matches = [m for m in matches if m]
    if targets and not matches:
        raise LookupError(f"nothing to frame for {targets!r}")
    page.evaluate(TOUR_SELECT2_JS)
    page.evaluate(TOUR_CAMERA_JS, {"els": [m.element_handle() for m in matches], "max": options.get("max", 2.0),
                                   "pad": options.get("pad", 40), "maxh": options.get("maxh", 560),
                                   "below": options.get("below", 0), "ms": ms})


def point(page, target, click: bool = False, ms: int = 600):
    """Glide the pointer to a locator (or the first visible match of selectors), with a ripple when it clicks; return
    the locator."""
    match = target if hasattr(target, "bounding_box") else first_visible(page, target)
    # A target that is not there is not waited for (the recording would show the wait).
    box = match.bounding_box(timeout=2000) if match is not None and match.count() else None
    if box:
        x, y = box["x"] + min(box["width"] / 2, 90), box["y"] + box["height"] / 2
        page.evaluate(TOUR_POINTER_JS, {"x": x, "y": y, "ms": ms, "click": click})
        page.wait_for_timeout(ms + (220 if click else 100))
    return match


class Screencast:
    """A page's frames from Chrome's screencast, as high-quality JPEGs, and the stretches of time to keep from them.
    Playwright's own video recorder compresses too hard for clips that zoom into the interface."""

    def __init__(self, page, size: dict):
        self.frames: list[tuple[float, float, bytes]] = []  # (frame time, arrival time, JPEG)
        self.segments: list[list[float]] = []
        self.size = size
        self.cdp = page.context.new_cdp_session(page)
        self.cdp.on("Page.screencastFrame", self._frame)

    def _frame(self, event):
        import base64
        import time
        self.frames.append((event["metadata"]["timestamp"], time.monotonic(), base64.b64decode(event["data"])))
        try:
            self.cdp.send("Page.screencastFrameAck", {"sessionId": event["sessionId"]})
        except Exception:  # noqa: BLE001 - a frame that arrives as the page closes
            pass

    def start(self):
        self.cdp.send("Page.startScreencast", {"format": "jpeg", "quality": 92,
                                               "maxWidth": self.size["width"], "maxHeight": self.size["height"]})

    def stop(self):
        self.cdp.send("Page.stopScreencast")

    def cut(self):
        """Start keeping frames (a new shot of the clip)."""
        import time
        self.segments.append([time.monotonic(), None])

    def pause(self):
        """Stop keeping frames until the next cut."""
        import time
        if self.segments and self.segments[-1][1] is None:
            self.segments[-1][1] = time.monotonic()

    def timeline(self, fps: int = 30, fade: int = 8) -> tuple[list[bytes], list[int]]:
        """The kept frames at a constant rate, each the last screencast frame shown before it, and the number of
        frames of each segment. A cut between segments crossfades over its first `fade` frames."""
        # Frame times are Chrome's clock; the segments are ours. The frame that arrived soonest after it was drawn
        # aligns the two.
        offset = min(arrival - shown for shown, arrival, _ in self.frames)
        frames = sorted((shown + offset, data) for shown, _, data in self.frames)
        out, counts, index = [], [], 0
        for start, end in self.segments:
            counts.append(int((end - start) * fps))
            for k in range(counts[-1]):
                moment = start + k / fps
                while index + 1 < len(frames) and frames[index + 1][0] <= moment:
                    index += 1
                while index > 0 and frames[index][0] > moment:
                    index -= 1
                out.append(frames[index][1])
        try:
            import io
            from PIL import Image
        except ImportError:
            return out, counts
        decode = lambda data: Image.open(io.BytesIO(data)).convert("RGB")  # noqa: E731
        # Frames of a shot in a narrower window are scaled up to the clip's size (both have the same proportions).
        size = (self.size["width"], self.size["height"])
        for k, data in enumerate(out):
            if Image.open(io.BytesIO(data)).size != size:
                scaled = io.BytesIO()
                decode(data).resize(size, Image.Resampling.LANCZOS).save(scaled, "JPEG", quality=92)
                out[k] = scaled.getvalue()
        for number in range(1, len(counts)):
            first = sum(counts[:number])
            if not first or not counts[number]:
                continue
            before = decode(out[first - 1])
            for k in range(min(fade, counts[number])):
                after = decode(out[first + k])
                if after.size != before.size:
                    break
                blended = io.BytesIO()
                Image.blend(before, after, (k + 1) / (fade + 1)).save(blended, "JPEG", quality=92)
                out[first + k] = blended.getvalue()
        return out, counts

    def clip_time(self, moment: float, counts: list[int], fps: int = 30) -> float:
        """Seconds into the clip of a moment of the recording (in a pause: the start of the next segment)."""
        elapsed = 0.0
        for (start, end), count in zip(self.segments, counts):
            if moment < start:
                return elapsed
            if moment <= end:
                return elapsed + min(moment - start, count / fps)
            elapsed += count / fps
        return elapsed

    def encode(self, ffmpeg: str, out: Path, fps: int = 30) -> tuple[list[int], bytes]:
        """Write the kept frames as a VP8 clip; return the number of frames of each segment and the last frame of the
        first segment, for a poster."""
        if not self.frames:
            raise RuntimeError("the screencast produced no frames")
        timeline, counts = self.timeline(fps)
        if not timeline:
            raise RuntimeError("the chapter recorded nothing: does every shot start with a frame step?")
        poster = timeline[max(0, counts[0] - 1)]
        # Playwright's minimal ffmpeg reads no pipes, so the constant-rate JPEG stream goes through a temporary file.
        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".mjpeg", delete=False) as stream:
            for data in timeline:
                stream.write(data)
        try:
            subprocess.run(
                [ffmpeg, "-y", "-loglevel", "error", "-f", "image2pipe", "-c:v", "mjpeg", "-framerate", str(fps),
                 "-i", stream.name, "-an", "-vf", "scale=1280:-2:flags=lanczos", "-c:v", "libvpx", "-b:v", "1200k",
                 "-crf", "10", "-qmin", "0", "-qmax", "30",
                 "-deadline", "good", "-cpu-used", "4", "-threads", "4", "-pix_fmt", "yuv420p", str(out)], check=True)
        finally:
            os.unlink(stream.name)
        return counts, poster


def save_poster(data: bytes, file: Path):
    """The poster as a 1280-pixel JPEG (the screencast frame itself when Pillow is missing)."""
    try:
        import io
        from PIL import Image
    except ImportError:
        file.write_bytes(data)
        return
    image = Image.open(io.BytesIO(data)).convert("RGB")
    image.thumbnail((1280, 1280), Image.Resampling.LANCZOS)
    image.save(file, quality=82, optimize=True)


def record_chapter(page, chapter: dict, ffmpeg: str, clip: Path) -> list[dict]:
    """Record one chapter to `clip` and its poster; return its caption cues."""
    import time
    cast = Screencast(page, {k: v * TOUR_SCALE for k, v in TOUR_VIEWPORT.items()})
    cast.start()
    captions = []  # (moment, sentence)

    def run(step):
        kind = step[0]
        if kind == "frame":
            cast.pause()
            frame(page, step[1], step[3] if len(step) > 3 else {})
            check_no_foreign_email_on_screen(page)
            page.wait_for_timeout(600)  # the framed screen is drawn before the shot starts
            cast.cut()
            captions.append((time.monotonic(), step[2]))
        elif kind == "move":
            options = step[3] if len(step) > 3 else {}
            if step[2]:
                captions.append((time.monotonic(), step[2]))
            frame(page, step[1], options, ms=options.get("ms", 1200))
            page.wait_for_timeout(options.get("ms", 1200) + 250)
            check_no_foreign_email_on_screen(page)
        elif kind == "pause":
            cast.pause()
        elif kind == "optional":
            try:
                run(step[1])
            except Exception as error:  # noqa: BLE001
                print(f"        (skipped {step[1][:2]}: {str(error).splitlines()[0][:80]})")
        elif kind == "mark":
            match = point(page, step[1])
            if not match:
                print(f"        (no mark: nothing matches {step[1]!r})")
            else:
                place = step[4] if len(step) > 4 else ("left" if match.evaluate("e => !!e.closest('td, th')") else "above")
                page.evaluate(TOUR_MARK_JS, {"box": match.bounding_box(), "tag": step[2], "place": place})
                page.wait_for_timeout(step[3] if len(step) > 3 else 2000)
        elif kind == "point":
            point(page, step[1])
        elif kind == "pick":
            # A dropdown: the pointer clicks it and the option is chosen (a native list does not show in a recording).
            point(page, [f"{step[1]} + .select2", step[1]], click=True)
            native = page.locator(step[1]).first
            if native.is_visible():
                select_by_text(native, step[2])
            else:
                choose(page, step[1], step[2])
            page.wait_for_timeout(350)
        else:
            # Steps that use a control: the pointer goes there first.
            target = {"click": lambda: page.get_by_text(step[1], exact=False).first,
                      "click_sel": lambda: page.locator(step[1]).first,
                      "type": lambda: page.locator(step[1]).first,
                      "select2": lambda: page.locator(f"{step[1]} + .select2").first,
                      "open_select2": lambda: page.locator(f"{step[1]} + .select2").first}.get(kind)
            if target:
                point(page, target(), click=True)
            do_step(page, step)

    for shot in chapter["shots"]:
        # A narrower window for this shot (same proportions): a wide form is laid out narrower and reads larger.
        page.set_viewport_size(shot.get("viewport", TOUR_VIEWPORT))
        if shot.get("go"):
            path = shot["go"](page) if callable(shot["go"]) else shot["go"]
            page.goto(BASE + path, wait_until="networkidle")
            if not path.endswith(".svg"):  # a bare SVG document has no <head> to style
                page.add_style_tag(content=HIDE_CSS)
            # The assistant drawer remembers that it was open; a shot that wants it opens it in `prepare`.
            if page.locator(".brainstem-assistant__close:visible").count():
                page.locator(".brainstem-assistant__close").first.click()
        for step in shot.get("prepare", []):
            do_step(page, step)
        for step in shot["steps"]:
            run(step)
        cast.pause()
        frame(page, None, {})  # zoomed, the controls of `after` can be off the screen
        for step in shot.get("after", []):
            do_step(page, step)
    cast.stop()
    counts, poster = cast.encode(ffmpeg, clip)
    save_poster(poster, clip.with_suffix(".jpg"))
    cues = [{"t": round(cast.clip_time(moment, counts), 2), "text": text} for moment, text in captions]
    for cue in cues:
        if cue["text"] in SHOT_LINKS:
            cue["doc"], cue["link"] = SHOT_LINKS[cue["text"]]
    return cues


def record_tour(p, only: list[str] | None = None) -> bool:
    """Record the landing-page tour, one clip per chapter (or only the chapters named in `only`); returns True
    when every chapter was written."""
    import json
    ffmpeg = find_ffmpeg()
    if not ffmpeg:
        print("FAILED  tour: no ffmpeg to encode the clips (install ffmpeg, or run `playwright install ffmpeg`)")
        return False
    browser = p.chromium.launch()
    context = recording_context(browser)
    ok = True
    try:
        TOUR_OUT.mkdir(parents=True, exist_ok=True)
        if not only:
            for old in [*TOUR_OUT.glob("*.webm"), *TOUR_OUT.glob("*.jpg")]:
                old.unlink()
        # Chapters not recorded this time keep the cues they have.
        previous = {}
        if TOUR_DATA.exists():
            import yaml
            previous = {c["file"]: c.get("cues", []) for c in (yaml.safe_load(TOUR_DATA.read_text()) or {}).get("chapters", [])}
        lines = ["# Written by scripts/screenshots.py (tour): the opening card and the chapters of the landing-page tour.",
                 "intro:", f'  title: {json.dumps(TOUR_INTRO["title"])}', f'  text: {json.dumps(TOUR_INTRO["text"])}', "chapters:"]
        for number, chapter in enumerate(TOUR, start=1):
            name = f"{number:02d}-{chapter['slug']}.webm"
            cues = previous.get(name, [])
            if not only or chapter["slug"] in only:
                page = context.new_page()
                try:
                    cues = record_chapter(page, chapter, ffmpeg, TOUR_OUT / name)
                    print(f"ok      tour {name}")
                except Exception as error:  # noqa: BLE001
                    ok = False
                    print(f"FAILED  tour {chapter['slug']}: {str(error).splitlines()[0][:160]}")
                finally:
                    page.close()
            lines += [f'  - file: "{name}"', f'    poster: "{name[:-5]}.jpg"', f'    title: "{chapter["title"]}"',
                      f'    text: "{chapter["text"]}"', f'    doc: "{chapter["doc"]}"', f'    link: "{chapter["link"]}"']
            lines += ["    cues:" + ("" if cues else " []")] + ["      - {" + ", ".join(f"{k}: {json.dumps(c[k]) if k != 't' else c[k]}"
                                                                     for k in ("t", "text", "doc", "link") if k in c) + "}"
                                                           for c in cues]
        TOUR_DATA.parent.mkdir(parents=True, exist_ok=True)
        TOUR_DATA.write_text("\n".join(lines) + "\n")
        return ok
    finally:
        context.close()
        browser.close()


# Placeholders that reuse another target's capture.
ALIASES = {
    "ephys-procedure-form": "procedure-add-form",
    "ephys-epochs-tab": "single-entry-view-session-epochs",
    "project-manage-members": "project-permissions",
}


def recover_page(page) -> str:
    """Delete the demo session kept for this purpose (if it still exists and none is waiting to be recovered yet), then
    open its Recover page."""
    page.goto(BASE + "/private/stem/session/recover/", wait_until="networkidle")
    waiting = page.locator("table tbody tr a").evaluate_all(
        "els => els.map(e => e.getAttribute('href')).filter(h => h && /^\\d+\\/$/.test(h))")
    try:
        if waiting:
            raise LookupError("already deleted")
        path = first_row_link(page, "/private/stem/session/", "Habituation+00")
        page.goto(BASE + path, wait_until="networkidle")
        page.once("dialog", lambda dialog: dialog.accept())  # "Delete this session?" confirm box
        page.locator("a.button--delete-object[href*='delete']").first.click(timeout=8000, force=True)
        page.wait_for_load_state("networkidle")
        confirm = page.get_by_text("Yes, I", exact=False)
        if confirm.count():
            confirm.first.click(timeout=8000)
            page.wait_for_load_state("networkidle")
    except LookupError:
        pass  # already deleted on an earlier run
    page.goto(BASE + "/private/stem/session/recover/", wait_until="networkidle")
    links = page.locator("table tbody tr a").evaluate_all(
        "els => els.map(e => e.getAttribute('href')).filter(h => h && /^\\d+\\/$/.test(h))"
    )
    if not links:
        raise LookupError("nothing to recover")
    return "/private/stem/session/recover/" + links[0]


def compress(file: Path):
    """Store the picture as a 256-colour PNG: a third of the size, no visible loss for interface screenshots."""
    try:
        from PIL import Image
    except ImportError:
        return
    if not file.exists():
        return
    image = Image.open(file).convert("RGBA")
    image.quantize(colors=256, method=Image.Quantize.FASTOCTREE).save(file, optimize=True)


def run(slugs: list[str]):
    from playwright.sync_api import sync_playwright

    OUT.mkdir(parents=True, exist_ok=True)
    wanted = [t for t in TARGETS if not slugs or t["slug"] in slugs]
    done, failed = [], []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport=VIEWPORT, device_scale_factor=1, user_agent=USER_AGENT, locale=LOCALE)
        context.add_init_script(NUMBER_FIELDS_JS)
        # The debug toolbar hidden from the first paint, also on pages a step opens (a submitted form, a reload).
        context.add_init_script("document.addEventListener('DOMContentLoaded', () => { if (!document.head) return;"
                                " const s = document.createElement('style'); s.textContent = '" + HIDE_CSS + "';"
                                " document.head.appendChild(s); });")
        page = context.new_page()
        login(page)
        for target in wanted:
            slug = target["slug"]
            index, step = -1, ("",)
            if target.get("no_save"):
                page.route("**/*", guard_writes)
            try:
                path = target["go"](page) if callable(target["go"]) else target["go"]
                page.set_viewport_size(target.get("viewport", VIEWPORT))
                # The navigation sidebar folded away unless the picture is about it (the interface stores "true" for
                # a collapsed sidebar).
                page.evaluate("v => { try { localStorage.setItem('django.admin.navSidebarIsOpen', v); } catch (e) {} }",
                              "false" if target.get("sidebar") else "true")
                page.goto(BASE + path, wait_until="networkidle")
                if not path.endswith(".svg"):  # a bare SVG document has no <head> to style
                    page.add_style_tag(content=HIDE_CSS)
                    if "brainstem-assistant" not in str(target.get("steps")):
                        page.add_style_tag(content=".brainstem-assistant__launcher{display:none!important}")
                    if target.get("css"):
                        page.add_style_tag(content=target["css"])
                page.wait_for_timeout(500)
                # The assistant drawer remembers that it was open; keep it out of unrelated pictures.
                if page.locator(".brainstem-assistant__close:visible").count():
                    page.locator(".brainstem-assistant__close").first.click()
                    page.wait_for_timeout(300)
                for step in target.get("steps", []):
                    do_step(page, step)
                page.wait_for_load_state("networkidle")
                check_no_foreign_email(page)
                file = OUT / f"{slug}.png"
                if target.get("around"):
                    # The smallest box around the listed elements (each a selector or its fallbacks), padded.
                    boxes = [m.bounding_box() for m in (first_visible(page, t) for t in target["around"]) if m]
                    if not boxes:
                        raise LookupError(f"nothing to crop around for {target['around']!r}")
                    pad, size = target.get("pad", 16), page.viewport_size
                    x0, y0 = max(0, min(b["x"] for b in boxes) - pad), max(0, min(b["y"] for b in boxes) - pad)
                    x1 = min(size["width"], max(b["x"] + b["width"] for b in boxes) + pad)
                    y1 = min(size["height"], max(b["y"] + b["height"] for b in boxes) + pad)
                    page.screenshot(path=str(file), clip={"x": x0, "y": y0, "width": x1 - x0, "height": y1 - y0})
                elif target.get("crop"):
                    page.screenshot(path=str(file), clip=target["crop"])
                elif target.get("clip"):
                    page.locator(target["clip"]).first.screenshot(path=str(file), timeout=8000)
                else:
                    page.screenshot(path=str(file), full_page=target.get("full", False))
                for step in target.get("after", []):
                    if step[0] == "click_sel":
                        page.locator(step[1]).first.click(timeout=4000)
                    else:
                        do_step(page, step)
                done.append(slug)
                print(f"ok      {slug}")
            except Exception as error:  # noqa: BLE001
                where = f" at step {index + 1} {step[:2]}" if target.get("steps") and "index" in locals() else ""
                failed.append((slug, str(error).splitlines()[0][:140]))
                print(f"FAILED  {slug}{where}: {str(error).splitlines()[0][:140]}")
            finally:
                for step in target.get("cleanup", []):
                    try:
                        do_step(page, step)
                    except Exception as error:  # noqa: BLE001
                        print(f"        (cleanup of {slug} failed: {str(error).splitlines()[0][:120]})")
                if target.get("no_save"):
                    # Leave the page while writes are still refused: an autosave fires as the page unloads.
                    page.goto("about:blank")
                    page.unroute("**/*", guard_writes)
        browser.close()
        if not slugs or any(w["slug"] in slugs for w in WALKTHROUGHS) or "walkthroughs" in slugs:
            walk_done, walk_failed = record_walkthroughs(p, [] if "walkthroughs" in slugs else slugs)
            failed.extend(walk_failed)
            print(f"{len(walk_done)} walkthroughs written to {WALKTHROUGH_OUT}")
        only = [slug.split(":", 1)[1] for slug in slugs if slug.startswith("tour:")]
        if not slugs or "tour" in slugs or only:
            if not record_tour(p, only):
                failed.append(("tour", "a tour chapter failed"))
    import shutil
    for slug in list(done):
        compress(OUT / f"{slug}.png")
    for alias, base in ALIASES.items():
        if (not slugs or alias in slugs) and (OUT / f"{base}.png").exists():
            shutil.copyfile(OUT / f"{base}.png", OUT / f"{alias}.png")
            done.append(alias)
    print(f"{len(done)} screenshots written to {OUT}; {len(failed)} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(run(sys.argv[1:]))
