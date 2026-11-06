#!/usr/bin/env python3
"""Draw the conceptual figures of the support site as SVG, into docs/assets/images/diagrams/.

    python scripts/render_diagrams.py            # every figure
    python scripts/render_diagrams.py session-kinds what-brainstem-records

Colours come from diagram_style.py, which follows the app colours of the interactive data model. The main
records of a figure are drawn solid (``strong=True``); supporting models are faint tints of their app colour.
The example figure of the data model page has its own script, render_example_figure.py."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from diagram_style import (FONT, STEM, MOD, PA, CAT, TAX, DIS, USR, APP, APP_LABEL, EDGE, LABEL, INK,  # noqa: E402
                           NOTE_FILL, NOTE_STROKE, tint, outline, dark)

OUT = Path(__file__).resolve().parents[1] / "docs" / "assets" / "images" / "diagrams"

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

class SVG:
    def __init__(self, w, h, title):
        self.w, self.h, self.title = w, h, title
        self.parts = []
    def add(self, s):
        self.parts.append(s)
    def box(self, x, y, w, h, color, lines, title_size=17, size=15, strong=False):
        """A model: solid in its app colour when it is a main record of the figure, else a faint tint.
        lines: the first is the bold title."""
        if strong:
            fill, stroke, title_ink, ink = color, dark(color), "#fff", "#fff"
        else:
            fill, stroke, title_ink, ink = tint(color), outline(color), dark(color), INK
        self.add(f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>')
        n = len(lines)
        step = size + 7
        total = title_size + (n - 1) * step
        y0 = y + (h - total) / 2 + title_size - 3
        cx = x + w / 2
        for i, ln in enumerate(lines):
            if i == 0:
                self.add(f'  <text x="{cx:g}" y="{y0:g}" font-size="{title_size}" font-weight="600" fill="{title_ink}" text-anchor="middle">{esc(ln)}</text>')
            else:
                self.add(f'  <text x="{cx:g}" y="{y0 + i * step:g}" font-size="{size}" fill="{ink}" text-anchor="middle">{esc(ln)}</text>')
        return (x, y, w, h)
    def note(self, x, y, w, h, lines, size=15, title=False):
        """A note; with ``title`` its first line is bold."""
        self.add(f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{NOTE_FILL}" stroke="{NOTE_STROKE}" stroke-width="1"/>')
        step = size + 7
        total = size + (len(lines) - 1) * step
        y0 = y + (h - total) / 2 + size - 3
        for i, ln in enumerate(lines):
            bold = ' font-weight="600"' if title and i == 0 else ""
            ink = INK if title and i == 0 else LABEL
            self.add(f'  <text x="{x + 14}" y="{y0 + i * step:g}" font-size="{size}" fill="{ink}"{bold}>{esc(ln)}</text>')
    def plain(self, x, y, w, h, lines, title_size=17, size=15, align="middle", dashed=False):
        """A concept that is not a model (a state, a place, a file): neutral grey. lines: the first is the bold title."""
        dash = ' stroke-dasharray="5 4"' if dashed else ""
        self.add(f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="#f4f3f8" stroke="#c9c6d6" stroke-width="1.2"{dash}/>')
        step = size + 7
        total = title_size + (len(lines) - 1) * step
        y0 = y + (h - total) / 2 + title_size - 3
        tx = x + w / 2 if align == "middle" else x + 16
        for i, ln in enumerate(lines):
            if i == 0:
                self.add(f'  <text x="{tx:g}" y="{y0:g}" font-size="{title_size}" font-weight="600" fill="{INK}" text-anchor="{align}">{esc(ln)}</text>')
            else:
                self.add(f'  <text x="{tx:g}" y="{y0 + i * step:g}" font-size="{size}" fill="{LABEL}" text-anchor="{align}">{esc(ln)}</text>')
        return (x, y, w, h)
    def legend(self, x, y, keys, strong=()):
        """App colour swatches: solid for the keys in ``strong``, faint for the others."""
        for key in keys:
            color = APP[key]
            fill, stroke = (color, dark(color)) if key in strong else (tint(color), outline(color))
            self.add(f'  <rect x="{x}" y="{y}" width="20" height="20" rx="4" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>')
            self.add(f'  <text x="{x + 30}" y="{y + 15}" font-size="15" fill="{INK}">{esc(APP_LABEL[key])}</text>')
            x += 30 + len(APP_LABEL[key]) * 7.6 + 34
        return x
    def band(self, x, y, w, h, color, label, size=16, notes=()):
        """A group of models with its title and, directly under the title, one or more lines of notes."""
        self.add(f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{color}" fill-opacity="0.07" stroke="{color}" stroke-opacity="0.6" stroke-width="1" stroke-dasharray="6 4"/>')
        self.add(f'  <text x="{x + 14}" y="{y + 24}" font-size="{size}" font-weight="600" fill="{color}">{esc(label)}</text>')
        for i, line in enumerate(notes):
            self.add(f'  <text x="{x + 14}" y="{y + 45 + 18 * i}" font-size="14" fill="{LABEL}">{esc(line)}</text>')
    def arrow(self, pts, dashed=False, marker=True):
        d = "M" + " L".join(f"{p[0]:g} {p[1]:g}" for p in pts)
        dash = ' stroke-dasharray="6 4"' if dashed else ""
        mk = ' marker-end="url(#arrow)"' if marker else ""
        self.add(f'  <path d="{d}" fill="none" stroke="{EDGE}" stroke-width="1.6"{dash}{mk}/>')
    def label(self, x, y, s, anchor="middle", size=15, color=LABEL, bg=False):
        if bg:
            w = len(s) * (size * 0.5) + 8
            if anchor == "middle":
                bx = x - w / 2
            elif anchor == "start":
                bx = x - 5
            else:
                bx = x - w + 5
            self.add(f'  <rect x="{bx:g}" y="{y - size + 2}" width="{w:g}" height="{size + 6}" fill="#fff"/>')
        self.add(f'  <text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}">{esc(s)}</text>')
    def heading(self, s, x=40, y=40):
        self.add(f'  <text x="{x}" y="{y}" font-size="18" font-weight="600" fill="{INK}">{esc(s)}</text>')
    def write(self, name):
        head = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" height="{self.h}" font-family="{FONT}" role="img" aria-labelledby="t">',
                f'  <title id="t">{esc(self.title)}</title>',
                '  <defs>',
                '    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">',
                f'      <path d="M0 0 L10 5 L0 10 z" fill="{EDGE}"/>',
                '    </marker>',
                '  </defs>',
                f'  <rect width="{self.w}" height="{self.h}" fill="#fff"/>']
        with open(OUT / name, "w") as f:
            f.write("\n".join(head + self.parts + ["</svg>"]) + "\n")
        print(name, self.w, self.h)

# ---------------------------------------------------------------- 1 material chain
def material_chain():
    s = SVG(1500, 520, "Material chain: catalog consumable, inventory stock, material usage, parent record")
    s.heading("Where a material comes from, and where it is used")
    s.box(60, 110, 320, 100, CAT, ["Consumable", "Shared catalog entry", "e.g. ASSY-156 silicon probe", "nominal value, supplier"])
    s.box(470, 108, 320, 112, MOD, ["Consumable stock", "Lot or item in an inventory", "e.g. ASSY-156, lot 2024-11", "as-received value, lot, expiry"])
    s.note(470, 290, 320, 70, ["Manual entry", "name and free text only, no catalog link"])
    s.box(880, 120, 320, 170, MOD, strong=True, lines=["Material usage", "Role: Silicon probe", "in a silicon probe implant", "Source: stock, catalog or manual", "Applied value: dose, volume, conc.", "Stage (optional), frozen snapshot"])
    s.box(1260, 110, 220, 64, MOD, ["Procedure", "in-vivo event"])
    s.box(1260, 205, 220, 64, MOD, ["Specimen procedure", "ex-vivo processing"])
    s.box(1260, 300, 220, 64, MOD, ["Experimental interface", "what a device is made of"])
    s.note(60, 420, 740, 70, ["Material usage templates plan the role, product and details of a row;",
                               "the stock item is chosen when the template is applied to a real procedure."])
    s.arrow([(380, 160), (470, 160)]); s.label(425, 150, "stocked as")
    s.arrow([(790, 168), (880, 168)]); s.label(838, 158, "from stock")
    s.arrow([(220, 210), (220, 250), (880, 250)]); s.label(560, 242, "from catalog (no stock entry)")
    s.arrow([(790, 325), (835, 325), (835, 275), (880, 275)]); s.label(800, 350, "manual entry", anchor="start")
    s.arrow([(1200, 205), (1230, 205), (1230, 142), (1260, 142)])
    s.arrow([(1230, 205), (1260, 205)])
    s.arrow([(1230, 205), (1230, 332), (1260, 332)])
    s.label(1230, 392, "one row in the"); s.label(1230, 412, "material list of")
    s.write("material-chain.svg")

# ---------------------------------------------------------------- 2 procedure → interface → session
def procedure_interface_session():
    s = SVG(1400, 640, "Procedure creates an experimental interface; sessions record through it")
    s.heading("From implant procedure to experimental interface to session")
    s.box(60, 250, 240, 80, STEM, ["Subject", "Mouse_01"], strong=True)
    s.box(400, 100, 300, 120, MOD, ["Procedure", "Silicon probe implant", "target region, coordinates", "materials: probe, cement, screws"])
    s.box(400, 340, 300, 140, MOD, strong=True, lines=["Experimental interface", "Implanted silicon probe (chronic)", "target region: CA1", "coordinates and device materials", "copied from the procedure"])
    s.box(880, 100, 240, 90, STEM, ["Session", "Mouse_01, 2026-03-14", "subject-based"], strong=True)
    s.box(880, 270, 240, 90, MOD, ["Data acquisition", "Extracellular ephys", "interfaces: silicon probe"])
    s.box(880, 420, 240, 90, MOD, ["Manipulation", "Electrical stimulation", "interfaces: silicon probe"])
    s.note(60, 540, 640, 70, ["Where and with what a recording was made is read from its interfaces:",
                              "target regions, coordinates and materials travel with the interface, not the session."])
    s.arrow([(300, 275), (350, 275), (350, 160), (400, 160)]); s.label(345, 140, "performed on", anchor="middle")
    s.arrow([(300, 305), (350, 305), (350, 410), (400, 410)]); s.label(350, 445, "installed on", anchor="middle")
    s.arrow([(550, 220), (550, 340)]); s.label(565, 285, "saving the implant creates", anchor="start")
    s.arrow([(1120, 145), (1160, 145), (1160, 465), (1120, 465)])
    s.arrow([(1160, 315), (1120, 315)]); s.label(1170, 240, "contains", anchor="start")
    s.arrow([(880, 325), (760, 325), (760, 390), (700, 390)]); s.label(872, 318, "records through", anchor="end")
    s.arrow([(880, 455), (760, 455), (760, 430), (700, 430)]); s.label(872, 476, "delivers through", anchor="end")
    s.write("procedure-interface-session.svg")

# ---------------------------------------------------------------- 3 specimen lineage
def specimen_lineage():
    s = SVG(1400, 720, "Specimen lineage: subject, specimen set, specimens, specimen procedures, derived sets")
    s.heading("From subject to specimen set to specimens")
    s.box(60, 80, 240, 80, STEM, ["Subject", "Mouse_01"], strong=True)
    s.box(60, 250, 240, 90, MOD, ["Procedure", "Perfusion and sectioning", "on the subject"])
    s.box(400, 240, 300, 110, STEM, strong=True, lines=["Specimen set", "Slice series, coronal 50 µm", "Subject: Mouse_01", "status Available, conditions Fixed"])
    s.box(400, 440, 300, 90, STEM, ["Specimens", "Slice 01 … Slice 24", "individual sections or wells"])
    s.box(800, 120, 280, 90, MOD, ["Specimen procedure", "Immunostaining, fixation", "stages, materials, conditions"])
    s.box(800, 250, 280, 76, MOD, ["Specimen log", "storage and state changes"])
    s.box(800, 370, 280, 90, STEM, ["Derived specimen set", "Mounted slides, slices 1–12", "Source specimen set: Slice series"])
    s.box(800, 500, 280, 90, MOD, ["Experimental interface", "Patch pipette, MEA, perfusion", "target: the specimen set"])
    s.box(1160, 500, 200, 90, STEM, ["Session", "specimen-based", "data acquisitions"], strong=True)
    s.note(60, 620, 740, 70, ["Specimen procedures and logs act on the set (or on selected specimens).",
                              "A set can be derived from a subject or from another set; lineage stays acyclic."])
    s.arrow([(180, 160), (180, 250)]); s.label(195, 210, "undergoes", anchor="start")
    s.arrow([(300, 120), (550, 120), (550, 240)]); s.label(550, 195, "derived from", anchor="middle")
    s.arrow([(300, 295), (400, 295)]); s.label(350, 285, "produces")
    s.arrow([(550, 350), (550, 440)]); s.label(565, 400, "contains", anchor="start")
    s.arrow([(700, 295), (750, 295), (750, 165), (800, 165)])
    s.arrow([(750, 288), (800, 288)])
    s.arrow([(750, 295), (750, 415), (800, 415)])
    s.arrow([(750, 415), (750, 545), (800, 545)])
    s.label(750, 225, "acts on", anchor="middle"); s.label(750, 355, "source of", anchor="middle"); s.label(750, 480, "target", anchor="middle")
    s.arrow([(1160, 545), (1080, 545)]); s.label(1120, 480, "records", anchor="middle"); s.label(1120, 498, "through", anchor="middle")
    s.write("specimen-lineage.svg")

# ---------------------------------------------------------------- 4 templates
def templates():
    s = SVG(1400, 660, "Templates: a procedure template prefills a new procedure; the user adds subject, date and stock")
    s.heading("What a template fills in, and what you still enter")
    s.box(60, 100, 340, 190, MOD, strong=True, lines=["Procedure template", "Silicon probe implant", "type and type-specific fields", "coordinates: AP, ML, DV, angles", "material rows: probe, cement, screws", "(role and product, no stock)"])
    s.box(560, 100, 340, 190, MOD, strong=True, lines=["Procedure", "Mouse_01, 2026-03-14", "copied from the template:", "type, fields, coordinates,", "material rows", "+ your entries →"])
    s.note(1000, 100, 340, 190, ["You still enter:", "• subject", "• date and time", "• notes", "• the stock item for each material row", "   (from your inventory)"])
    s.box(60, 400, 340, 90, MOD, ["Material usage template", "role Silicon probe, product ASSY-156", "stage and details prefilled"])
    s.box(1000, 400, 340, 90, MOD, ["Consumable stock", "ASSY-156, lot 2024-11", "from your Inventory"])
    s.note(560, 540, 780, 70, ["Same pattern for templates of procedure episodes, specimen procedures,",
                               "experimental interfaces, material usages, data acquisitions and manipulations."])
    s.arrow([(400, 195), (560, 195)]); s.label(480, 168, "apply to a"); s.label(480, 186, "new procedure")
    s.arrow([(1000, 195), (900, 195)], dashed=True); s.label(950, 218, "entered"); s.label(950, 236, "by you")
    s.arrow([(230, 400), (230, 290)]); s.label(245, 350, "supplies the material rows", anchor="start")
    s.arrow([(1000, 445), (730, 445), (730, 290)]); s.label(745, 350, "chosen for each material row", anchor="start"); s.label(745, 370, "when the template is applied", anchor="start")
    s.write("templates.svg")

# ---------------------------------------------------------------- 5 procedure stages
def procedure_stages():
    s = SVG(1300, 640, "Procedure stages: material usage rows belong to a stage or to the whole procedure")
    s.heading("Stages of a procedure and the materials that belong to them")
    s.box(60, 70, 380, 100, MOD, strong=True, lines=["Procedure", "Anesthesia, Mouse_01, 2026-03-14", "type policy declares the stage types", "Induction, Maintenance, Top-up, …"])
    s.box(60, 240, 300, 100, MOD, ["Stage 1: Induction", "route: inhaled, chamber", "duration 3 min"])
    s.box(420, 240, 300, 100, MOD, ["Stage 2: Maintenance", "route: inhaled, nose cone", "duration 45 min"])
    s.note(60, 550, 740, 70, ["A stage carries what its materials share: route, rate, duration, temperature.", "Each material usage row names one stage, or none for the whole procedure."])
    s.box(60, 410, 300, 100, MOD, ["Material usage", "Anesthetic agent: isoflurane", "applied 5 %, lot A1", "stage: Induction"])
    s.box(420, 410, 300, 100, MOD, ["Material usage", "Anesthetic agent: isoflurane", "applied 1.5 %, lot A1", "stage: Maintenance"])
    s.box(800, 410, 300, 100, MOD, ["Material usage", "Analgesic: carprofen", "5 mg/kg, subcutaneous", "stage: none (whole procedure)"])
    s.arrow([(250, 170), (250, 200), (950, 200), (950, 410)])
    s.arrow([(210, 200), (210, 240)])
    s.arrow([(570, 200), (570, 240)])
    s.label(385, 192, "stages, in order"); s.label(965, 300, "material row", anchor="start"); s.label(965, 320, "without a stage", anchor="start")
    s.arrow([(210, 340), (210, 410)]); s.label(225, 380, "materials of this stage", anchor="start")
    s.arrow([(570, 340), (570, 410)]); s.label(585, 380, "materials of this stage", anchor="start")
    s.write("procedure-stages.svg")

# ---------------------------------------------------------------- 6 epoch timeline
def epoch_timeline():
    """The epochs of a session on its timeline, each with the behavior, data acquisitions and manipulations placed in
    it, grouped by epoch as on the session's Epochs tab."""
    x0, x1 = 300, 1320
    X = lambda m: x0 + (x1 - x0) * m / 40  # noqa: E731
    s = SVG(1400, 610, "Epoch timeline: named intervals from the session onset, each with the behavior, data "
                       "acquisitions and manipulations placed in it")
    s.box(x0, 30, x1 - x0, 56, STEM, ["Session   Mouse_01, 2026-03-14 10:00   (session onset = 0:00)"], strong=True)
    # axis, with faint guides down through the rows
    s.add(f'  <path d="M{X(0):g} 130 L{X(40):g} 130" stroke="{EDGE}" stroke-width="1.6" fill="none"/>')
    for m in (0, 10, 20, 30, 40):
        s.add(f'  <path d="M{X(m):g} 124 L{X(m):g} 136" stroke="{EDGE}" stroke-width="1.6"/>')
        s.add(f'  <path d="M{X(m):g} 140 L{X(m):g} 500" stroke="{EDGE}" stroke-width="1" stroke-dasharray="3 5" opacity="0.45"/>')
        s.add(f'  <text x="{X(m):g}" y="114" font-size="15" fill="{LABEL}" text-anchor="middle">0:{m:02d}</text>')
    s.add(f'  <text x="{X(40):g}" y="158" font-size="14" fill="{LABEL}" text-anchor="end">time from session onset (h:mm)</text>')
    epochs = [("Baseline", 0, 10, [("Behavior", "Open field")]),
              ("Stimulation", 10, 20, [("Data acquisition", "Extracellular ephys"),
                                        ("Manipulation", "Optogenetic stimulation")]),
              ("Recovery", 20, 40, [("Behavior", "Open field (the same behavior)")])]
    y = 176
    for name, a, b, parts in epochs:
        s.add(f'  <text x="60" y="{y + 26}" font-size="16" font-weight="600" fill="{INK}">Epoch: {esc(name)}</text>')
        s.box(X(a), y, X(b) - X(a), 40, STEM, [f"0:{a:02d} – 0:{b:02d}"], title_size=15)
        y += 46
        for kind, example in parts:
            s.add(f'  <text x="84" y="{y + 22}" font-size="15" fill="{LABEL}">{esc(kind)}</text>')
            s.box(X(a), y, X(b) - X(a), 34, MOD, [example], title_size=15)
            y += 40
        y += 14
    s.note(x0, y + 10, x1 - x0, 62, ["An epoch names at most one behavior, and one behavior can run through several epochs.",
                                      "A data acquisition belongs to one epoch only; a manipulation can span several epochs."])
    s.write("epoch-timeline.svg")

# ---------------------------------------------------------------- 7 session kinds
def session_kinds():
    s = SVG(1400, 720, "Session kinds: subject-based and specimen-based sessions; behaviors only in subject-based sessions")
    s.heading("Two kinds of session")
    s.box(560, 60, 280, 64, STEM, ["Project", "Hippocampal mapping"], strong=True)
    s.box(60, 190, 300, 96, STEM, strong=True, lines=["Session (subject-based)", "Subjects: Mouse_01, Mouse_02", "in vivo"])
    s.box(1040, 190, 300, 96, STEM, strong=True, lines=["Session (specimen-based)", "Specimen set: Slice series", "ex vivo"])
    s.band(500, 170, 400, 266, MOD, "Modules in either session")
    s.box(530, 210, 340, 52, MOD, ["Data acquisitions (through interfaces)"])
    s.box(530, 278, 340, 52, MOD, ["Manipulations (through interfaces)"])
    s.box(530, 346, 340, 52, STEM, ["Epochs"])
    s.box(60, 340, 300, 76, STEM, ["Subject", "Mouse_01"], strong=True)
    s.box(1040, 340, 300, 76, STEM, ["Specimen set", "Acute slices, Mouse_03"], strong=True)
    s.box(60, 480, 300, 96, MOD, ["Experimental interface", "Implanted silicon probe", "target type: Subject"])
    s.box(1040, 480, 300, 96, MOD, ["Experimental interface", "Patch pipette, bath perfusion", "target type: Specimen set"])
    s.box(60, 620, 300, 76, MOD, ["Behaviors", "subject-based sessions only"])
    s.arrow([(700, 124), (700, 150), (210, 150), (210, 190)])
    s.arrow([(700, 150), (1190, 150), (1190, 190)])
    s.label(455, 142, "belongs to", anchor="middle"); s.label(945, 142, "belongs to", anchor="middle")
    s.arrow([(360, 238), (500, 238)]); s.label(430, 228, "contains")
    s.arrow([(1040, 238), (900, 238)]); s.label(970, 228, "contains")
    s.arrow([(60, 238), (32, 238), (32, 658), (60, 658)])
    s.arrow([(210, 286), (210, 340)]); s.label(225, 318, "links", anchor="start")
    s.arrow([(1190, 286), (1190, 340)]); s.label(1205, 318, "links", anchor="start")
    s.arrow([(210, 416), (210, 480)]); s.label(225, 453, "interfaces installed on it", anchor="start")
    s.arrow([(1190, 416), (1190, 480)]); s.label(1205, 453, "interfaces targeting it", anchor="start")
    s.arrow([(360, 528), (650, 528), (650, 436)]); s.label(505, 548, "used by its acquisitions")
    s.arrow([(1040, 528), (750, 528), (750, 436)]); s.label(895, 548, "used by its acquisitions")
    s.write("session-kinds.svg")


# ---------------------------------------------------------------- 8 data model overview
def data_model_overview():
    """The whole model by app, solid as in the interactive data model."""
    s = SVG(1600, 930, "BrainSTEM data model overview")
    S = dict(strong=True)
    # bands, each with its notes directly under the title
    s.band(40, 40, 300, 150, USR, "Users and groups", notes=["roles on projects and personal attributes"])
    s.band(40, 220, 300, 190, DIS, "Dissemination", notes=["submitted by DOI;", "publications link to projects"])
    s.band(380, 40, 860, 670, STEM, "Projects, subjects, sessions, specimen sets and their modules")
    s.band(1280, 40, 280, 670, PA, "Personal attributes",
           notes=["owned by users or groups and", "shared with users and groups,", "like projects"])
    s.band(40, 730, 740, 170, CAT, "Resources: shared catalog, used by everyone",
           notes=["probe and ECoG designs, viruses, reagents, devices; an RRID can be given on submission"])
    s.band(820, 730, 740, 170, TAX, "Taxonomies, used by everyone")
    # users
    s.box(60, 100, 120, 50, USR, ["Users"], **S)
    s.box(200, 100, 120, 50, USR, ["Groups"], **S)
    # dissemination
    s.box(60, 300, 120, 50, DIS, ["Journals"], title_size=16, **S)
    s.box(200, 300, 120, 50, DIS, ["Publications"], title_size=16, **S)
    s.arrow([(180, 325), (200, 325)])
    s.arrow([(320, 325), (360, 325), (360, 128), (720, 128)])
    # project
    s.box(720, 80, 200, 56, STEM, ["Project"], **S)
    s.box(1000, 80, 220, 56, STEM, ["Cohorts, Collections,", "Breedings"], title_size=16, size=15, **S)
    s.arrow([(320, 110), (720, 110)]); s.label(530, 101, "member, contributor, manager, owner")
    s.arrow([(920, 108), (1000, 108)])
    cols = [410, 690, 970]
    s.box(cols[0], 180, 230, 56, STEM, ["Subject"], **S)
    s.box(cols[1], 180, 230, 56, STEM, ["Specimen set"], **S)
    s.box(cols[2], 180, 230, 56, STEM, ["Session"], **S)
    s.arrow([(820, 136), (820, 155), (525, 155), (525, 180)])
    s.arrow([(820, 155), (1085, 155), (1085, 180)])
    s.arrow([(805, 155), (805, 180)])
    # subject column, with the children of Procedures indented
    cx = cols[0]; spine = cx - 14
    s.arrow([(cx + 115, 236), (cx + 115, 258), (spine, 258), (spine, 673)], marker=False)
    s.box(cx, 290, 230, 46, MOD, ["Procedures"], title_size=16, **S); s.arrow([(spine, 313), (cx, 313)])
    inner = cx + 14
    s.arrow([(inner, 336), (inner, 553)], marker=False)
    for i, lab in enumerate(["Experimental interfaces", "Procedure logs", "Material usages", "Procedure stages"]):
        y = 350 + 60 * i
        s.box(cx + 30, y, 200, 46, MOD, [lab], title_size=16, **S)
        s.arrow([(inner, y + 23), (cx + 30, y + 23)])
    s.box(cx, 590, 230, 46, MOD, ["Procedure episodes"], title_size=16, **S); s.arrow([(spine, 613), (cx, 613)])
    s.box(cx, 650, 230, 46, MOD, ["Subject logs"], title_size=16, **S); s.arrow([(spine, 673), (cx, 673)])
    # specimen set column
    cx = cols[1]; spine = cx - 14
    s.arrow([(cx + 115, 236), (cx + 115, 258), (spine, 258), (spine, 493)], marker=False)
    for i, lab in enumerate(["Specimens", "Specimen procedures", "Specimen logs", "Experimental interfaces"]):
        y = 290 + 60 * i
        s.box(cx, y, 230, 46, STEM if lab == "Specimens" else MOD, [lab], title_size=16, **S)
        s.arrow([(spine, y + 23), (cx, y + 23)])
    # session column
    cx = cols[2]; spine = cx - 14
    s.arrow([(cx + 115, 236), (cx + 115, 258), (spine, 258), (spine, 493)], marker=False)
    for i, lab in enumerate(["Data acquisitions", "Manipulations", "Behaviors", "Epochs"]):
        y = 290 + 60 * i
        s.box(cx, y, 230, 46, STEM if lab == "Epochs" else MOD, [lab], title_size=16, **S)
        s.arrow([(spine, y + 23), (cx, y + 23)])
    # personal attributes; equipment and consumable stock belong to the Modules app
    pa = [("Setups", False), ("Equipment", True), ("Inventories", False), ("Consumable stock", True),
          ("Protocols", False), ("Licenses", False), ("Data storage", False), ("Behavioral assays", False)]
    y = 140
    for lab, ind in pa:
        x = 1300 + (30 if ind else 0); w = 240 - (30 if ind else 0)
        s.box(x, y, w, 46, MOD if ind else PA, [lab], title_size=16, **S)
        if ind:
            s.arrow([(1314, y - 14), (1314, y + 23), (x, y + 23)])
        y += 60
    # resources
    s.box(60, 805, 200, 50, CAT, ["Consumables"], **S)
    s.box(300, 805, 200, 50, CAT, ["Hardware devices"], **S)
    s.box(540, 805, 200, 50, CAT, ["Suppliers"], **S)
    # taxonomies: the primary ones only (atlases and coordinate transforms support the regions and coordinates)
    for i, lab in enumerate(["Species", "Strains", "Anatomical regions", "Setup types"]):
        s.box(840 + i * 178, 775, 166, 44, TAX, [lab], title_size=15, **S)
    for i, lab in enumerate(["Regulatory authorities", "Behavioral categories", "Behavioral paradigms"]):
        s.box(840 + i * 237, 835, 225, 44, TAX, [lab], title_size=15, **S)
    s.write("data-model-overview.svg")


# ---------------------------------------------------------------- 9 landing page: how an experiment is structured
def what_records():
    """Each box answers one question about an experiment (what, where, with what, by whom), coloured by app."""
    s = SVG(1260, 830, "How BrainSTEM structures an experiment: a project holds subjects; procedures are done on a "
                       "subject and implants create experimental interfaces; sessions are recorded on a subject and hold "
                       "data acquisitions, behavior, manipulations and epochs; species, data storage, protocols, atlases, "
                       "materials, setups and behavioral assays describe the context.")
    H = 96
    r0, r1, r2, r3, r4 = 20, 160, 300, 470, 640
    bus = r3 - 35

    def q(x, y, w, color, question, title, detail, strong=False):
        if strong:
            fill, stroke, ask, head, ink = color, dark(color), "#ffffff", "#ffffff", "#ffffff"
        else:
            fill, stroke, ask, head, ink = tint(color), outline(color), dark(color, 0.85), dark(color), INK
        cx = x + w / 2
        s.add(f'  <rect x="{x}" y="{y}" width="{w}" height="{H}" rx="9" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>')
        s.add(f'  <text x="{cx:g}" y="{y + 27}" font-size="16" font-style="italic" fill="{ask}" fill-opacity="0.85" text-anchor="middle">{esc(question)}</text>')
        s.add(f'  <text x="{cx:g}" y="{y + 56}" font-size="22" font-weight="700" fill="{head}" text-anchor="middle">{esc(title)}</text>')
        s.add(f'  <text x="{cx:g}" y="{y + 80}" font-size="16" fill="{ink}" text-anchor="middle">{esc(detail)}</text>')

    def link(pts):
        s.arrow(pts, dashed=True)
    # connectors first, so the boxes sit on top
    s.arrow([(435, r0 + H), (435, r1)])
    s.arrow([(435, r1 + H), (435, r2)])
    s.arrow([(570, r1 + H / 2), (600, r1 + H / 2)])
    s.arrow([(755, r1 + H), (755, r2)])
    s.arrow([(435, r2 + H), (435, bus), (145, bus), (145, r3)])
    s.arrow([(435, bus), (1090, bus)], marker=False)
    s.arrow([(435, bus), (435, r3)])
    s.arrow([(755, bus), (755, r3)])
    s.arrow([(1090, bus), (1090, r3)])
    link([(835, r2 + H), (835, r3)])
    link([(880, r2 + H), (880, r2 + H + 17), (1010, r2 + H + 17), (1010, r3)])
    link([(270, r1 + H / 2), (300, r1 + H / 2)])
    link([(270, r2 + H / 2), (300, r2 + H / 2)])
    link([(940, r0 + H / 2), (880, r0 + H / 2), (880, r1)])
    link([(940, r1 + H / 2), (910, r1 + H / 2)])
    link([(990, r1 + H), (990, r1 + H + 22), (870, r1 + H + 22), (870, r2)])
    link([(940, r2 + H / 2), (910, r2 + H / 2)])
    link([(755, r4), (755, r3 + H)])
    link([(600, r4 + H / 2), (435, r4 + H / 2), (435, r3 + H)])
    link([(910, r4 + H / 2), (1090, r4 + H / 2), (1090, r3 + H)])
    link([(270, r4 + H / 2), (360, r4 + H / 2), (360, r3 + H)])
    # the axis of the study, solid
    q(300, r0, 270, STEM, "By whom", "Project", "the study and who sees it", strong=True)
    q(300, r1, 270, STEM, "On what", "Subject", "the animal or specimen set", strong=True)
    q(300, r2, 270, STEM, "When", "Session", "one recording occasion", strong=True)
    # what was done and recorded, faint
    q(600, r1, 310, MOD, "What was done", "Procedures", "surgeries, injections, drugs")
    q(600, r2, 310, MOD, "Through what", "Experimental interfaces", "implanted probes, windows")
    q(20, r3, 250, STEM, "Which part of it", "Epochs", "named intervals")
    q(300, r3, 270, MOD, "What the animal did", "Behavior", "the task and its assay")
    q(600, r3, 310, MOD, "What was recorded", "Data acquisition", "ephys, imaging, video, audio")
    q(940, r3, 300, MOD, "What was changed", "Manipulations", "stimulation, perturbations")
    # the context the records point to, faint
    q(20, r1, 250, TAX, "Which animal", "Species & strains", "describe the subject")
    q(20, r2, 250, PA, "Where the data lives", "Data storage", "servers, paths, repositories")
    q(940, r0, 300, PA, "Under which rules", "Protocols & licenses", "approve the procedures")
    q(940, r1, 300, TAX, "Where in the brain", "Atlas & coordinates", "regions, stereotaxic targets")
    q(940, r2, 300, CAT, "Which products", "Materials", "probes, viruses, drugs")
    q(600, r4, 310, PA, "With what", "Setups & equipment", "rigs, amplifiers, cameras")
    q(20, r4, 250, PA, "Which task", "Behavioral assay", "paradigm and setup type")
    # legend: the app colours of the interactive data model
    x, y = 20, r4 + H + 46
    for key, strong in (("stem", True), ("modules", False), ("personal_attributes", False), ("resources", False), ("taxonomies", False)):
        color = APP[key]
        fill, stroke = (color, dark(color)) if strong else (tint(color), outline(color))
        s.add(f'  <rect x="{x}" y="{y}" width="22" height="22" rx="4" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>')
        s.add(f'  <text x="{x + 32}" y="{y + 17}" font-size="17" fill="{INK}">{esc(APP_LABEL[key])}</text>')
        x += 32 + len(APP_LABEL[key]) * 7.9 + 44
    s.arrow([(x, y + 11), (x + 44, y + 11)], dashed=True)
    s.add(f'  <text x="{x + 54}" y="{y + 17}" font-size="17" fill="{INK}">used by</text>')
    s.write("what-brainstem-records.svg")


# ---------------------------------------------------------------- 10 behavior and setup tracks
BEHAVIOR_TRACK_PAGES = ("behavior", "behavioralassay", "behavioralcategory", "behavioralparadigm", "setup", "setuptype")


def behavior_tracks(focus):
    """The behavioral track and the setup track, from shared taxonomies through the lab's personal attributes to
    the behavior recorded in a session. `focus` is the model of the page the figure sits on, drawn solid."""
    s = SVG(1300, 860, "How behaviors fit together: behavioral categories group paradigms, an assay implements a "
                       "paradigm on a setup type, a setup is a rig of a setup type with its equipment, and a behavior "
                       "records an assay run on a setup with subjects in a session.")
    T = dict(title_size=19, size=15)
    on = lambda key: dict(strong=(key == focus), **T)  # noqa: E731
    L, C, R, W = 60, 480, 900, 340
    # bands: shared taxonomies, the lab's personal attributes, the records of a session
    s.band(30, 30, 1240, 300, TAX, "Taxonomies: shared by everyone")
    s.band(30, 350, 1240, 270, PA, "Personal attributes: your lab's, shared through groups")
    s.band(30, 640, 1240, 200, STEM, "Records of a session, in your projects")
    # connectors first
    s.arrow([(L + W / 2, 160), (L + W / 2, 220)]); s.label(L + W / 2 + 12, 196, "groups", anchor="start")
    s.arrow([(L + W / 2, 304), (L + W / 2, 400)]); s.label(L + W / 2 - 12, 324, "implemented as", anchor="end")
    s.arrow([(R + W / 2, 160), (R + W / 2, 220)]); s.label(R + W / 2 + 12, 196, "a field of", anchor="start")
    s.arrow([(R + W / 2, 304), (R + W / 2, 400)]); s.label(R + W / 2 + 12, 380, "built as", anchor="start")
    s.arrow([(R + 40, 304), (R + 40, 340), (L + W - 40, 340), (L + W - 40, 400)])
    s.label(C + W / 2, 322, "the assay names the setup type it runs on")
    s.arrow([(R + W / 2, 540), (R + W / 2, 484)]); s.label(R + W / 2 + 12, 520, "installed in", anchor="start")
    s.arrow([(L + W, 442), (C + 120, 442), (C + 120, 690)]); s.label(L + W + 14, 432, "run as", anchor="start")
    s.arrow([(R, 442), (C + W - 120, 442), (C + W - 120, 690)]); s.label(R - 14, 432, "run on", anchor="end")
    s.arrow([(L + W, 740), (C, 740)]); s.label((L + W + C) / 2, 730, "contains")
    s.arrow([(R, 740), (C + W, 740)]); s.label((C + W + R) / 2, 730, "involves")
    # behavioral track
    s.box(L, 80, W, 80, TAX, ["Behavioral category", "Anxiety & Affect › Anxiety (nested)"], **on("behavioralcategory"))
    s.box(L, 220, W, 84, TAX, ["Behavioral paradigm", "Elevated Plus Exploration", "the task, as the field knows it"], **on("behavioralparadigm"))
    s.box(L, 400, W, 84, PA, ["Behavioral assay", "EPM 5-min test", "your lab's version of the paradigm"], **on("behavioralassay"))
    # setup track; the setup type category is a field of the setup type, not a model
    s.add(f'  <rect x="{R}" y="80" width="{W}" height="80" rx="7" fill="#f4f3f8" stroke="#c9c6d6" stroke-width="1.2" stroke-dasharray="5 4"/>')
    s.add(f'  <text x="{R + W / 2:g}" y="113" font-size="19" font-weight="600" fill="{INK}" text-anchor="middle">Setup type category</text>')
    s.add(f'  <text x="{R + W / 2:g}" y="137" font-size="15" fill="{INK}" text-anchor="middle">Freely Moving Awake (a choice list)</text>')
    s.box(R, 220, W, 84, TAX, ["Setup type", "Elevated plus maze", "the class of apparatus"], **on("setuptype"))
    s.box(R, 400, W, 84, PA, ["Setup", "EPM rig B, Room 108", "your physical rig"], **on("setup"))
    s.box(R, 540, W, 64, MOD, ["Equipment", "camera, IR lights, tracking software"], title_size=17, size=14)
    # the session
    s.box(L, 700, W, 80, STEM, ["Session", "Mouse_01, 2026-03-14"], **T)
    s.box(C, 690, W, 100, MOD, ["Behavior", "EPM test of Mouse_01", "one assay, one setup, its subjects"], **on("behavior"))
    s.box(R, 700, W, 80, STEM, ["Subjects", "Mouse_01"], **T)
    s.write(f"behavior-tracks-{focus}.svg")


SETUP_HUB_PAGES = ("setup", "equipment")


def setup_hub(focus):
    """Where setups and equipment are used: a behavior names the whole setup; procedures, specimen procedures,
    experimental interfaces, data acquisitions and manipulations name the equipment they used. `focus` (setup or
    equipment) is drawn solid."""
    s = SVG(1300, 580, "Where setups and equipment are used: a setup is built as a setup type and holds equipment, "
                       "which can name its catalog model; procedures, specimen procedures, experimental interfaces, "
                       "data acquisitions and manipulations name the equipment they used, and a behavior names the setup.")
    T = dict(title_size=19, size=15)
    on = lambda key: dict(strong=(key == focus), **T)  # noqa: E731
    W, top, mid, low, H = 340, 60, 220, 430, 84
    bus = 380
    users = [("Procedures", "surgeries, injections"), ("Specimen procedures", "sectioning, staining"),
             ("Experimental interfaces", "probes, fibers, windows"), ("Data acquisitions", "ephys, imaging, video"),
             ("Manipulations", "stimulation, perturbation"), ("Behaviors", "an assay run on a setup")]
    bw, gap, x0 = 190, 20, 30
    centers = [x0 + i * (bw + gap) + bw / 2 for i in range(len(users))]
    # connectors first
    LW = 290  # the left column is narrower, so the connector labels fit between the columns
    s.arrow([(40 + LW, top + 42), (480, top + 42)]); s.label(405, top + 34, "built as")
    s.arrow([(40 + LW, mid + 42), (480, mid + 42)]); s.label(405, mid + 34, "catalog model")
    s.arrow([(650, mid), (650, top + H)]); s.label(662, top + H + 40, "installed in", anchor="start")
    s.arrow([(650, mid + H), (650, bus)], marker=False)
    s.arrow([(centers[0], bus), (centers[4], bus)], marker=False)
    s.label(662, bus - 14, "used by (each names the equipment it used)", anchor="start")
    for cx in centers[:5]:
        s.arrow([(cx, bus), (cx, low)])
    s.arrow([(480 + W, top + 42), (centers[5], top + 42), (centers[5], low)])
    s.label(centers[5] - 12, top + 34, "used by (a behavior names its setup)", anchor="end")
    # setup, its type, its equipment and the catalog
    s.box(40, top, LW, H, TAX, ["Setup type", "Head-fixed disc", "the class of station"], **on("setuptype"))
    s.box(480, top, W, H, PA, ["Setup", "Ephys rig A, Room 108", "your physical rig"], **on("setup"))
    s.box(40, mid, LW, H, CAT, ["Catalog entry", "Intan RHD 64-ch headstage", "a hardware device or consumable"], **T)
    s.box(480, mid, W, H, MOD, ["Equipment", "headstage, camera, stereotax", "one item in one setup"], **on("equipment"))
    # the records that use them
    for (title, detail), cx in zip(users, centers):
        s.box(cx - bw / 2, low, bw, 80, MOD, [title, detail], title_size=16, size=13)
    s.label((centers[0] + centers[2]) / 2, low + 108, "on a subject or specimen set", size=15)
    s.label((centers[3] + centers[5]) / 2, low + 108, "in a session", size=15)
    s.write(f"setup-hub-{focus}.svg")


# ---------------------------------------------------------------- 12 where do I record it?
def where_to_record():
    """What happened, and the entry that records it. Targets solid in their app colour, related entries faint."""
    s = SVG(1400, 970, "Where do I record it: an intervention performed on the animal is a procedure; a measure or "
                       "observation of the animal is a subject log; a device left in or on the animal is an experimental interface, created by "
                       "its implant procedure; tissue taken for ex-vivo work is a specimen set, processed in specimen "
                       "procedures; a product used is a material usage row; in a session, a recorded signal is a data "
                       "acquisition, a delivered stimulus a manipulation, a task a behavior and a time segment an epoch.")
    s.heading("Where do I record it?")
    QX, QW, TX, TW, RX, RW, H, STEP = 60, 470, 620, 340, 1090, 270, 64, 78
    for x, t in ((QX, "What happened"), (TX, "Record it as"), (RX, "Related entry")):
        s.add(f'  <text x="{x}" y="84" font-size="15" font-weight="600" fill="{LABEL}">{esc(t)}</text>')

    def row(y, question, examples, color, title, detail, related=None):
        s.plain(QX, y, QW, H, [question, examples], align="start")
        s.arrow([(QX + QW, y + H / 2), (TX, y + H / 2)])
        s.box(TX, y, TW, H, color, [title, detail], strong=True)
        if related:
            rcolor, rlines, label, inward = related
            pts = [(RX, y + H / 2), (TX + TW, y + H / 2)] if inward else [(TX + TW, y + H / 2), (RX, y + H / 2)]
            s.arrow(pts)
            s.label((TX + TW + RX) / 2, y + H / 2 - 9, label, size=14)
            s.box(RX, y, RW, H, rcolor, rlines)

    s.band(40, 96, 1340, 436, EDGE, "Outside a session: on the animal or its tissue")
    y = 140
    row(y, "An intervention on the animal", "surgery, implant, injection, anesthesia, perfusion",
        MOD, "Procedure", "an intervention performed on the subject"); y += STEP
    row(y, "A measure or observation of the animal", "weight, health check, water intake, training progress",
        MOD, "Subject log", "dated measures and observations"); y += STEP
    row(y, "A device left in or on the animal", "probe, optic fiber, cannula, window, headpost",
        MOD, "Experimental interface", "kept for later sessions",
        (MOD, ["Implant procedure", "creates it when performed"], "creates", True)); y += STEP
    row(y, "Tissue taken for ex-vivo work", "slices, sections, cultures, organoids",
        STEM, "Specimen set", "a batch of material from the subject",
        (MOD, ["Specimen procedure", "sectioning, fixation, staining"], "processed in", False)); y += STEP
    row(y, "A product or lot that was used", "drug, virus, probe, cement, screws",
        MOD, "Material usage", "role, product, source, amount",
        (MOD, ["Procedure", "or specimen procedure"], "a row of", False))
    s.band(40, 552, 1340, 358, EDGE, "During a session")
    y = 596
    row(y, "A signal was recorded", "ephys, imaging, video, audio",
        MOD, "Data acquisition", "a recorded signal, through interfaces"); y += STEP
    row(y, "Something delivered to the target", "stimulus, optogenetics, drug delivery",
        MOD, "Manipulation", "a delivered stimulus, through interfaces"); y += STEP
    row(y, "The animal performed a task", "an assay run on a setup",
        MOD, "Behavior", "assay, setup and subjects"); y += STEP
    row(y, "A stretch of time in the session", "baseline, stimulation, recovery",
        STEM, "Epoch", "start and end from session onset")
    x = s.legend(60, 932, ["stem", "modules"], strong=("stem", "modules"))
    s.add(f'  <rect x="{x}" y="932" width="20" height="20" rx="4" fill="{tint(MOD)}" stroke="{outline(MOD)}" stroke-width="1.2"/>')
    s.add(f'  <text x="{x + 30}" y="947" font-size="15" fill="{INK}">related entry</text>')
    s.write("where-to-record.svg")


# ---------------------------------------------------------------- 13 planning states
def planning_states():
    """The planning status of procedures, specimen procedures, sessions and breedings, its guards, and where
    planned entries show. States are not models: neutral grey."""
    s = SVG(1400, 820, "Planning states: a planned procedure, specimen procedure, session or breeding becomes performed "
                       "with Mark as performed (breedings: Mark as started) or is cancelled; the transition is checked, "
                       "a performed implant with an experimental interface cannot go back to planned, and planned entries "
                       "show in lists but not in statistics, the API by default or the public portal.")
    s.heading("Planned, performed and cancelled")
    s.band(40, 60, 900, 108, EDGE, "Entries with a planning status")
    for x, w, color, title in ((60, 200, MOD, "Procedures"), (275, 210, MOD, "Specimen procedures"),
                               (500, 200, STEM, "Sessions"), (715, 200, STEM, "Breedings")):
        s.box(x, 100, w, 48, color, [title], title_size=16, strong=True)
    # connectors first
    s.arrow([(320, 258), (660, 258)])
    s.add(f'  <text x="490" y="246" font-size="16" font-weight="600" fill="{INK}" text-anchor="middle">Mark as performed</text>')
    s.label(490, 282, "breedings: Mark as started", size=14)
    s.arrow([(150, 306), (150, 420)]); s.label(162, 398, "Status: Cancelled", anchor="start", size=14)
    s.arrow([(720, 306), (720, 352), (250, 352), (250, 306)], dashed=True)
    s.label(485, 376, "back to planned, in the Status field", size=14)
    s.arrow([(860, 306), (860, 420)]); s.label(850, 392, "implants create", anchor="end", size=14)
    s.plain(60, 210, 260, 96, ["Planned", "prepared; nothing happened", "the date is the intended one"], dashed=True)
    s.plain(660, 210, 260, 96, ["Performed", "describes what was done", "the default for new entries"])
    s.plain(60, 420, 260, 96, ["Cancelled", "planned, then dropped", "kept for the record"], dashed=True)
    s.box(660, 420, 260, 96, MOD, ["Experimental interface", "created when an implant", "procedure is performed"])
    s.note(60, 540, 860, 136, ["Checked when a plan becomes performed",
                               "Procedure: subject enrolled, episode not planned, date and time set",
                               "Specimen procedure: set (and targeted specimens) collected, date set",
                               "Session: subjects enrolled, specimen sets collected",
                               "Breeding: parents enrolled, pairing date set"], title=True)
    s.note(60, 692, 860, 96, ["Refused when going back to planned",
                              "a performed implant procedure with linked experimental interfaces",
                              "a breeding whose offspring already exist"], title=True)
    # where planned entries show
    s.band(980, 60, 380, 728, EDGE, "Where planned entries show")
    for i, lines in enumerate((["Lists and forms", "Yes: a Planned pill,", "a Status column and filter"],
                               ["Dropdowns and links", "Yes: names start with", "Planned: or Cancelled:"],
                               ["Statistics and counts", "No: dashboard statistics and", "licence counts are performed only"],
                               ["API", "Only when asked:", "include_planned=true"],
                               ["Public portal", "Never, even when the", "project is public"])):
        s.plain(1000, 102 + i * 134, 340, 120, lines, title_size=18, size=16)
    s.write("planning-states.svg")


# ---------------------------------------------------------------- 14 public sharing scope
def public_sharing_scope():
    """What a public project publishes, what needs its own switch, what is always public and what never is."""
    s = SVG(1400, 800, "Public sharing scope: the project's visibility switch publishes the project with its subjects, "
                       "sessions, specimen sets, their modules and logs, and templates shared with it; setups, "
                       "inventories, behavioral assays, protocols and licenses have their own switch, and a data storage "
                       "is public through its data protocols; the catalog, taxonomies and publications are always public; "
                       "planned entries, memberships, permissions, email addresses and API tokens never are.")
    s.heading("What making a project public publishes")
    # a: inherits from the project
    s.band(40, 64, 660, 502, EDGE, "Published by the project's Project visibility switch")
    s.box(70, 108, 600, 46, STEM, ["Project"], strong=True)
    L, LW, R, RW = 70, 250, 340, 330
    s.box(L, 172, LW, 134, STEM, ["Subjects", "with cohorts", "and breedings"], strong=True)
    s.box(R, 172, RW, 60, MOD, ["Procedures, episodes", "procedure logs, interfaces"])
    s.box(R, 246, RW, 60, MOD, ["Subject logs", "with their entries"])
    s.box(L, 324, LW, 60, STEM, ["Sessions", "collections, epochs"], strong=True)
    s.box(R, 324, RW, 60, MOD, ["Session modules", "behaviors, acquisitions, manipulations"])
    s.box(L, 402, LW, 60, STEM, ["Specimen sets", "and specimens"], strong=True)
    s.box(R, 402, RW, 60, MOD, ["Specimen procedures", "and specimen logs"])
    s.box(L, 480, 600, 60, MOD, ["Templates shared with the project", "read-only in the public portal"])
    # b: their own switch
    s.band(740, 64, 620, 502, EDGE, "Public only with their own visibility switch")
    s.label(754, 106, "Private or Public, set on each entry", anchor="start", size=14)
    L, LW, R, RW = 760, 250, 1050, 290
    for i, title in enumerate(("Setups", "Inventories", "Behavioral assays", "Protocols", "Licenses")):
        s.box(L, 124 + i * 64, LW, 52, PA, [title], strong=True)
    s.arrow([(L + LW, 150), (R, 150)]); s.box(R, 124, RW, 52, MOD, ["Equipment", "public with its setup"], size=14)
    s.arrow([(L + LW, 214), (R, 214)]); s.box(R, 188, RW, 52, MOD, ["Consumable stock", "public with its inventory"], size=14)
    s.box(L, 460, LW, 76, PA, ["Data storage"], strong=True)
    s.arrow([(R, 498), (L + LW, 498)])
    s.note(R, 460, RW, 76, ["public when one of its data", "protocols has Public Access"])
    # c: always public
    s.band(40, 586, 660, 190, EDGE, "Always public")
    for x, color, lines in ((60, CAT, ["Resources", "consumables, devices,", "suppliers"]),
                            (270, TAX, ["Taxonomies", "species, strains,", "atlases, regions"]),
                            (480, DIS, ["Dissemination", "publications", "and journals"])):
        s.box(x, 630, 200, 120, color, lines, strong=True)
    # d: never public
    s.band(740, 586, 620, 190, EDGE, "Never public")
    for (x, y), title in zip(((760, 628), (1060, 628), (760, 700), (1060, 700)),
                             ("Planned, cancelled entries", "Memberships, permissions", "Email addresses", "API tokens")):
        s.plain(x, y, 280, 52, [title], title_size=16)
    s.write("public-sharing-scope.svg")


# ---------------------------------------------------------------- 16 export to NWB
def export_nwb_pipeline():
    """From BrainSTEM to NWB and DANDI: what runs on the BrainSTEM server and what the lab runs on its own computer."""
    s = SVG(1500, 520, "Export to NWB: on BrainSTEM, the server builds the export of one project or session as JSON; on "
                       "your computer, brainstem-nwb converts it with a configuration file into one NWB file per session "
                       "and subject with a manifest and a validation report, metadata only; the lab adds the raw data "
                       "and shares the files on DANDI.")
    s.heading("From BrainSTEM to NWB")
    s.label(40, 64, "Metadata only: the NWB files hold no time series, images or video until the lab adds them.",
            anchor="start", size=15)
    s.band(20, 86, 590, 290, STEM, "On BrainSTEM", notes=["the server builds the export"])
    s.band(640, 86, 600, 412, EDGE, "On your computer", notes=["run by the lab"])
    y, h = 150, 196
    s.plain(40, y, 250, h, ["BrainSTEM", "web: Project → Download", "REST API", "Python and MATLAB tools", "MCP server"])
    s.plain(330, y, 260, h, ["Export JSON", "one project or one session", "versioned format 2.x", "lab resources you cannot",
                             "read: listed as restricted"])
    s.plain(660, y, 260, h, ["brainstem-nwb", "pip install brainstem-nwb", "+ config.toml: experimenter,",
                             "lab, institution", "optional: ndx-brainstem"])
    s.plain(960, y, 260, h, ["NWB files", "one per session and subject", "+ manifest: what was", "written, every warning",
                             "+ validation report"])
    s.plain(960, 390, 260, 90, ["Raw data", "time series, images, video", "added by the lab"], dashed=True)
    s.plain(1280, y + 40, 200, h - 80, ["DANDI", "public archive", "upload by the lab"])
    cy = y + h / 2
    s.arrow([(290, cy), (330, cy)]); s.arrow([(590, cy), (660, cy)]); s.label(625, cy - 12, "download", size=14, bg=True)
    s.arrow([(920, cy), (960, cy)]); s.arrow([(1220, cy), (1280, cy)])
    s.arrow([(1090, 390), (1090, y + h)])
    s.write("export-nwb-pipeline.svg")


# ---------------------------------------------------------------- 17 the parts of a session
SESSION_PART_PAGES = ("behavior", "dataacquisition", "manipulation")


def session_parts(focus):
    """A session holds a behavior (what the subjects did), data acquisitions (what was recorded) and manipulations
    (what was delivered), each placed in one of its epochs (when). `focus` is the model of the page, drawn solid. The
    timeline itself is drawn by epoch_timeline(), with the same example session."""
    s = SVG(1400, 460, "A session and its parts: the behavior (what the subjects were doing), data acquisitions (what "
                       "was recorded) and manipulations (what was delivered), each placed in one of the session's epochs "
                       "(when); behaviors run an assay on a setup, and acquisitions and manipulations pass through "
                       "experimental interfaces.")
    s.heading("A session and its parts", y=36)
    # what the parts draw on, outside the session
    s.box(60, 60, 145, 70, PA, ["Behavioral assay", "the task"], title_size=15)
    s.box(215, 60, 145, 70, PA, ["Setup", "the rig"], title_size=15)
    s.box(390, 60, 630, 70, MOD, ["Experimental interfaces", "the probe, fiber or window a signal or stimulus passes through"])
    s.band(30, 160, 1340, 280, STEM, "")
    s.add(f'  <text x="1050" y="190" font-size="16" font-weight="600" fill="{STEM}">Session: Mouse_01, 2026-03-14</text>')
    s.arrow([(132, 130), (132, 210)]); s.label(144, 150, "run as", anchor="start")
    s.arrow([(287, 130), (287, 210)]); s.label(299, 150, "run on", anchor="start")
    s.arrow([(540, 130), (540, 210)]); s.label(552, 150, "recorded through", anchor="start")
    s.arrow([(870, 130), (870, 210)]); s.label(882, 150, "delivered through", anchor="start")
    # the parts
    s.box(60, 210, 300, 110, MOD, ["Behavior", "what the subjects were doing", "open field"], strong=(focus == "behavior"))
    s.box(390, 210, 300, 110, MOD, ["Data acquisition", "what was recorded", "extracellular ephys"],
          strong=(focus == "dataacquisition"))
    s.box(720, 210, 300, 110, MOD, ["Manipulation", "what was delivered", "optogenetic stimulation"],
          strong=(focus == "manipulation"))
    s.box(1050, 210, 290, 110, STEM, ["Epochs", "when it happened", "baseline, stimulation, recovery"],
          strong=(focus == "epoch"))
    # each part placed in an epoch
    for x in (210, 540):
        s.arrow([(x, 320), (x, 352)], dashed=True, marker=False)
    s.arrow([(870, 320), (870, 352), (1195, 352), (1195, 324)], dashed=True)
    s.add(f'  <path d="M210 352 L870 352" fill="none" stroke="{EDGE}" stroke-width="1.6" stroke-dasharray="6 4"/>')
    s.label(540, 376, "each placed in one of the session's epochs", size=14)
    s.label(60, 418, "An epoch names at most one behavior, and a data acquisition belongs to one epoch only. "
                     "Behaviors are recorded in subject-based sessions only.", anchor="start", size=14)
    s.write(f"session-parts-{focus}.svg")


# ---------------------------------------------------------------- 18 setup type categories
PICT_INK, TISSUE, BATH = "#6f6d82", "#f1d2de", "#dcebf6"
FUR, EAR, METAL, METAL_D, WARM = "#e6e4ee", "#f2c4d2", "#d3d1dc", "#9a98aa", "#f6e4c6"


def _mouse(tx, ty, k=1.0, eye="open"):
    """A side-view mouse facing right in a 100 x 45 frame (ground at y = 41), placed at (tx, ty) and scaled by k."""
    ink = PICT_INK
    return [
        f'  <g transform="translate({tx:g},{ty:g}) scale({k:g})" stroke="{ink}" stroke-linejoin="round" stroke-linecap="round">',
        '    <path d="M9 31 C-6 32 -16 24 -30 33 C-38 38 -44 36 -48 31" fill="none" stroke-width="1.6"/>',
        f'    <path d="M20 37 L17 42 L27 42 M66 37 L66 42 L73 42" fill="none" stroke-width="1.6"/>',
        f'    <path d="M9 31 C3 15 19 3 41 3 C58 3 69 8 78 16 C85 21 92 25 97 30 C95 33 90 34 84 34 '
        f'C76 36 70 37 63 38 C50 41 30 41 18 39 C12 38 10 35 9 31 Z" fill="{FUR}" stroke-width="1.6"/>',
        f'    <ellipse cx="71" cy="11" rx="7" ry="9" transform="rotate(-18 71 11)" fill="{FUR}" stroke-width="1.5"/>',
        f'    <ellipse cx="71.5" cy="11.5" rx="3.6" ry="5.5" transform="rotate(-18 71 11)" fill="{EAR}" stroke="none"/>',
        f'    <circle cx="96.5" cy="30.5" r="2.2" fill="{EAR}" stroke-width="1"/>',
        '    <path d="M93 31 L104 28 M93 32 L104 33" fill="none" stroke-width="0.8" opacity="0.7"/>',
        (f'    <circle cx="84.5" cy="22" r="2.1" fill="{ink}" stroke="none"/>' if eye == "open" else
         '    <path d="M81.5 22 Q84.5 25 87.5 22" fill="none" stroke-width="1.5"/>'),
        '  </g>']


def _pictogram(s, kind, x, y, w, h):
    """The preparation of one setup type category, drawn in a 205 x 150 frame inside a grey panel."""
    s.plain(x, y, w, h, [""])
    ink = PICT_INK
    a = [f'  <g transform="translate({x:g},{y:g})" stroke-linejoin="round" stroke-linecap="round">']
    if kind == "I":  # an acute coronal slice in a perfused recording chamber, with a pipette
        a += [f'  <path d="M8 66 L50 74" stroke="{METAL_D}" stroke-width="4"/>',
              f'  <path d="M154 92 L197 100" stroke="{METAL_D}" stroke-width="4"/>',
              f'  <circle cx="102" cy="82" r="54" fill="{METAL}" stroke="{ink}" stroke-width="1.5"/>',
              f'  <circle cx="102" cy="82" r="46" fill="{BATH}" stroke="{ink}" stroke-width="1.2"/>',
              f'  <path d="M102 60 C120 53 139 62 139 80 C139 97 125 107 109 105 C105 105 103 102 102 99 '
              f'C101 102 99 105 95 105 C79 107 65 97 65 80 C65 62 84 53 102 60 Z" fill="{TISSUE}" stroke="{ink}" stroke-width="1.4"/>',
              f'  <path d="M102 61 L102 98" stroke="{ink}" stroke-width="0.8" opacity="0.5"/>',
              f'  <path d="M78 84 C72 74 84 66 94 72 M126 84 C132 74 120 66 110 72" fill="none" stroke="{ink}" stroke-width="1.3"/>',
              f'  <path d="M80 92 C88 96 96 94 99 90 M124 92 C116 96 108 94 105 90" fill="none" stroke="{ink}" stroke-width="0.9" opacity="0.6"/>',
              f'  <path d="M190 6 L194 10 L160 44 L156 40 Z" fill="{METAL}" stroke="{ink}" stroke-width="1.2"/>',
              f'  <path d="M158 42 L118 78" stroke="{ink}" stroke-width="1.2"/>']
    elif kind == "E":  # an isolated whole brain seen from above, in a perfused bath, with an electrode
        a += [f'  <path d="M4 40 L22 40 L22 60" fill="none" stroke="{METAL_D}" stroke-width="4"/>',
              f'  <rect x="16" y="30" width="172" height="112" rx="8" fill="{METAL}" stroke="{ink}" stroke-width="1.5"/>',
              f'  <rect x="23" y="37" width="158" height="98" rx="5" fill="{BATH}" stroke="{ink}" stroke-width="1.1"/>',
              f'  <rect x="93" y="112" width="14" height="20" rx="5" fill="{TISSUE}" stroke="{ink}" stroke-width="1.3"/>',
              f'  <ellipse cx="100" cy="110" rx="21" ry="10" fill="{TISSUE}" stroke="{ink}" stroke-width="1.4"/>',
              f'  <path d="M83 106 L117 106 M81 110 L119 110 M83 114 L117 114" stroke="{ink}" stroke-width="0.8" opacity="0.6"/>',
              f'  <path d="M99 50 C82 48 69 58 69 76 C69 92 79 103 99 103 Z" fill="{TISSUE}" stroke="{ink}" stroke-width="1.5"/>',
              f'  <path d="M101 50 C118 48 131 58 131 76 C131 92 121 103 101 103 Z" fill="{TISSUE}" stroke="{ink}" stroke-width="1.5"/>',
              f'  <path d="M80 70 C86 66 92 68 95 74 M120 70 C114 66 108 68 105 74" fill="none" stroke="{ink}" stroke-width="0.9" opacity="0.5"/>',
              f'  <ellipse cx="93" cy="45" rx="6.5" ry="8" fill="{TISSUE}" stroke="{ink}" stroke-width="1.3"/>',
              f'  <ellipse cx="107" cy="45" rx="6.5" ry="8" fill="{TISSUE}" stroke="{ink}" stroke-width="1.3"/>',
              f'  <path d="M189 8 L193 12 L163 42 L159 38 Z" fill="{METAL}" stroke="{ink}" stroke-width="1.2"/>',
              f'  <path d="M161 40 L124 72" stroke="{ink}" stroke-width="1.2"/>']
    elif kind == "A":  # lying on a heating pad in a stereotaxic frame, with ear bar, nose cone and a needle
        a += [f'  <rect x="12" y="122" width="181" height="10" rx="3" fill="{METAL}" stroke="{ink}" stroke-width="1.3"/>',
              f'  <path d="M160 122 L160 64 L130 64" fill="none" stroke="{METAL_D}" stroke-width="5"/>',
              f'  <rect x="30" y="112" width="118" height="10" rx="3" fill="{WARM}" stroke="{ink}" stroke-width="1.2"/>']
        a += _mouse(42, 71, k=1.0, eye="closed")
        a += [f'  <circle cx="113" cy="82" r="4" fill="{METAL_D}" stroke="{ink}" stroke-width="1.2"/>',
              f'  <path d="M136 92 L156 86 L156 110 L136 106 Z" fill="{METAL}" stroke="{ink}" stroke-width="1.3"/>',
              f'  <path d="M156 98 C172 98 180 100 205 100" fill="none" stroke="{METAL_D}" stroke-width="3"/>',
              f'  <rect x="102" y="10" width="14" height="40" rx="2" fill="{METAL}" stroke="{ink}" stroke-width="1.3"/>',
              f'  <path d="M109 50 L109 70" stroke="{ink}" stroke-width="1.6"/>',
              f'  <text x="58" y="56" font-size="15" fill="{ink}" font-style="italic">z</text>',
              f'  <text x="68" y="44" font-size="12" fill="{ink}" font-style="italic">z</text>']
    elif kind == "HA":  # awake on a running wheel, its head bar clamped to a post, with a lick spout
        a += [f'  <path d="M96 140 L96 104 M60 140 L132 140" stroke="{METAL_D}" stroke-width="4"/>',
              f'  <circle cx="96" cy="104" r="34" fill="#fff" stroke="{ink}" stroke-width="1.6"/>',
              f'  <circle cx="96" cy="104" r="28" fill="none" stroke="{ink}" stroke-width="0.8" opacity="0.5"/>',
              f'  <path d="M96 76 L96 132 M68 104 L124 104 M76 84 L116 124 M116 84 L76 124" stroke="{ink}" stroke-width="0.8" opacity="0.45"/>',
              f'  <circle cx="96" cy="104" r="4" fill="{METAL_D}"/>',
              f'  <path d="M178 140 L178 34 L128 34" fill="none" stroke="{METAL_D}" stroke-width="5"/>']
        a += _mouse(44, 29, k=0.95)
        a += [f'  <rect x="102" y="28" width="30" height="8" rx="2" fill="{METAL}" stroke="{ink}" stroke-width="1.2"/>',
              f'  <path d="M150 56 L138 58" stroke="{METAL_D}" stroke-width="3"/>',
              f'  <path d="M150 56 L176 50" stroke="{METAL_D}" stroke-width="3"/>']
    elif kind == "RA":  # awake inside a clear tube restrainer, head out the front and tail out the back
        a += [f'  <rect x="22" y="118" width="160" height="9" rx="3" fill="{METAL}" stroke="{ink}" stroke-width="1.2"/>',
              f'  <path d="M50 118 L50 104 M128 118 L128 104" stroke="{METAL_D}" stroke-width="4"/>']
        a += _mouse(48, 62, k=1.0)
        a += [f'  <path d="M40 58 L126 58 A10 24 0 0 1 126 106 L40 106" fill="#cfd8ea" fill-opacity="0.45" stroke="{ink}" stroke-width="1.5"/>',
              f'  <ellipse cx="126" cy="82" rx="10" ry="24" fill="none" stroke="{ink}" stroke-width="1.3"/>',
              f'  <ellipse cx="40" cy="82" rx="10" ry="24" fill="{METAL}" stroke="{ink}" stroke-width="1.5"/>',
              f'  <path d="M58 64 L108 64 M58 100 L108 100" stroke="#ffffff" stroke-width="2.5" opacity="0.8"/>',
              f'  <path d="M64 70 L100 70" stroke="{ink}" stroke-width="1" opacity="0.5"/>']
    elif kind == "FA":  # moving freely in an open arena, with its path and a tethered headstage
        a += [f'  <path d="M46 46 L160 46 L160 92 L46 92 Z" fill="#f7f6fa" stroke="{ink}" stroke-width="1.3"/>',
              f'  <path d="M46 92 L160 92 L188 134 L18 134 Z" fill="#fff" stroke="{ink}" stroke-width="1.5"/>',
              f'  <path d="M18 134 L18 88 L46 46 M188 134 L188 88 L160 46" fill="none" stroke="{ink}" stroke-width="1.3"/>',
              f'  <path d="M18 88 L46 46 L46 92 Z M188 88 L160 46 L160 92 Z" fill="#efeef4" stroke="none" opacity="0.8"/>',
              f'  <path d="M30 126 C44 112 40 102 62 104 C78 106 66 122 84 124" fill="none" stroke="{ink}" stroke-width="1.3" stroke-dasharray="3 4"/>',
              f'  <circle cx="122" cy="10" r="6" fill="{METAL}" stroke="{ink}" stroke-width="1.2"/>',
              f'  <path d="M122 16 C124 40 128 54 128 86" fill="none" stroke="{ink}" stroke-width="1.2"/>']
        a += _mouse(84, 87, k=0.82)
        a += [f'  <rect x="122" y="84" width="11" height="8" rx="2" fill="{METAL_D}" stroke="{ink}" stroke-width="1"/>']
    a.append('  </g>')
    for line in a:
        s.add(line)


def setup_type_categories():
    """The setup type categories from a slice to a freely moving animal, with the three attributes derived from them
    (taxonomies/models/SetupType.py, CATEGORY_DECOMPOSITION) and a seeded setup type of each."""
    cats = [("I", "In Vitro", ["Brain slice", "recording chamber"]),
            ("E", "Ex Vivo", ["Isolated whole-brain", "preparation"]),
            ("A", "Anesthetized In Vivo", ["Stereotaxic frame"]),
            ("HA", "Head-Fixed Awake", ["Head-fixed treadmill"]),
            ("RA", "Restrained Awake", ["Tube restrainer"]),
            ("FA", "Freely Moving Awake", ["Open field arena"])]
    X0, CW, W = 230, 205, 215
    col = lambda i: X0 + i * W  # noqa: E731
    right = col(5) + CW
    s = SVG(right + 30, 660, "Setup type categories, from a slice to a freely moving animal: In Vitro, Ex Vivo, "
                             "Anesthetized In Vivo, Head-Fixed Awake, Restrained Awake and Freely Moving Awake, each with "
                             "an example setup type, and the biological preparation, physiological state and constraint "
                             "level derived from the category.")
    s.heading("Setup type categories: from a slice to a freely moving animal", y=36)
    # the trade-off along the row
    s.add(f'  <path d="M{X0 + 6} 78 L{right - 6} 78" stroke="{EDGE}" stroke-width="1.6" marker-start="url(#arrow)" marker-end="url(#arrow)"/>')
    s.label(X0, 66, "more experimental control", anchor="start", size=14)
    s.label(right, 66, "more natural behavior", anchor="end", size=14)
    for i, (code, name, example) in enumerate(cats):
        x = col(i)
        _pictogram(s, code, x, 96, CW, 150)
        s.plain(x, 260, CW, 52, [name], title_size=16)
        s.box(x, 324, CW, 64, TAX, example, title_size=15, size=15)
    # the derived attributes: one segment per value, spanning the categories that share it; none where not applicable
    def segment(i0, i1, y, text):
        x = col(i0)
        w = col(i1) + CW - x
        if text:
            s.plain(x, y, w, 38, [text], title_size=15)
        else:
            s.plain(x, y, w, 38, ["not applicable"], title_size=14, dashed=True)
    segment(0, 0, 440, "In vitro"); segment(1, 1, 440, "Ex vivo"); segment(2, 5, 440, "In vivo")
    segment(0, 1, 490, None); segment(2, 2, 490, "Anesthetized"); segment(3, 5, 490, "Awake")
    segment(0, 2, 540, None); segment(3, 3, 540, "Head-fixed"); segment(4, 4, 540, "Restrained"); segment(5, 5, 540, "Freely moving")
    # row labels, centred on their rows
    for y, h, text in ((260, 52, "Category"), (324, 64, "Setup type, e.g."), (440, 38, "Biological preparation"),
                       (490, 38, "Physiological state"), (540, 38, "Constraint level")):
        s.label(40, y + h / 2 + 5, text, anchor="start", size=15, color=INK if y < 400 else LABEL)
    s.label(40, 424, "Derived from the category (read-only):", anchor="start", size=14)
    s.label(40, 625, "Unknown: only when the preparation cannot be determined, such as for imported historical records.",
            anchor="start", size=14)
    s.write("setup-type-categories.svg")


FIGURES = {
    "material-chain": material_chain, "procedure-interface-session": procedure_interface_session,
    "specimen-lineage": specimen_lineage, "templates": templates, "procedure-stages": procedure_stages,
    "epoch-timeline": epoch_timeline, "session-kinds": session_kinds, "data-model-overview": data_model_overview,
    "what-brainstem-records": what_records, "where-to-record": where_to_record, "planning-states": planning_states,
    "public-sharing-scope": public_sharing_scope,
    "export-nwb-pipeline": export_nwb_pipeline, "setup-type-categories": setup_type_categories,
}
FIGURES.update({f"behavior-tracks-{page}": (lambda page=page: behavior_tracks(page)) for page in BEHAVIOR_TRACK_PAGES})
FIGURES.update({f"setup-hub-{page}": (lambda page=page: setup_hub(page)) for page in SETUP_HUB_PAGES})
FIGURES.update({f"session-parts-{page}": (lambda page=page: session_parts(page)) for page in SESSION_PART_PAGES})

if __name__ == "__main__":
    for name in sys.argv[1:] or FIGURES:
        FIGURES[name]()
