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
    def note(self, x, y, w, h, lines, size=15):
        self.add(f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{NOTE_FILL}" stroke="{NOTE_STROKE}" stroke-width="1"/>')
        step = size + 7
        total = size + (len(lines) - 1) * step
        y0 = y + (h - total) / 2 + size - 3
        for i, ln in enumerate(lines):
            self.add(f'  <text x="{x + 14}" y="{y0 + i * step:g}" font-size="{size}" fill="{LABEL}">{esc(ln)}</text>')
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
    s.band(450, 80, 360, 150, PA, "Inventory (personal attribute)")
    s.box(60, 110, 320, 100, CAT, ["Consumable", "Shared catalog entry", "e.g. ASSY-156 silicon probe", "nominal value, supplier"])
    s.box(470, 120, 320, 96, MOD, ["Consumable stock", "Lot or item in an inventory", "as-received value, lot, expiry"])
    s.note(470, 290, 320, 70, ["Manual entry", "name and free text only, no catalog link"])
    s.box(880, 120, 320, 170, MOD, strong=True, lines=["Material usage", "Role: Anesthetic agent", "Source: stock, catalog or manual", "Applied value: dose, volume, conc.", "Stage (optional), frozen snapshot"])
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
    s = SVG(1400, 560, "Epoch timeline: named intervals from the session start, with linked behaviors, acquisitions and manipulations")
    x0, ppm = 200, 28  # px per minute
    X = lambda m: x0 + ppm * m
    s.box(60, 30, 1260, 56, STEM, ["Session   Mouse_01, 2026-03-14 10:00   (session onset = 0:00)"], strong=True)
    # axis
    s.add(f'  <path d="M{X(0)} 150 L{X(40)} 150" stroke="{EDGE}" stroke-width="1.6" fill="none"/>')
    for m in (0, 10, 20, 30, 40):
        s.add(f'  <path d="M{X(m)} 144 L{X(m)} 156" stroke="{EDGE}" stroke-width="1.6"/>')
        s.add(f'  <text x="{X(m)}" y="134" font-size="15" fill="{LABEL}" text-anchor="middle">0:{m:02d}</text>')
    s.add(f'  <text x="{X(40)}" y="176" font-size="15" fill="{LABEL}" text-anchor="end">time from session onset (h:mm)</text>')
    s.add(f'  <text x="60" y="215" font-size="15" fill="{LABEL}">Epochs</text>')
    s.box(X(0), 185, X(10) - X(0), 56, STEM, ["Baseline", "0:00 – 0:10"])
    s.box(X(10), 185, X(20) - X(10), 56, STEM, ["Stimulation", "0:10 – 0:20"])
    s.box(X(20), 185, X(40) - X(20), 56, STEM, ["Recovery", "0:20 – 0:40"])
    s.add(f'  <text x="60" y="325" font-size="15" fill="{LABEL}">Linked</text>')
    s.add(f'  <text x="60" y="345" font-size="15" fill="{LABEL}">modules</text>')
    s.box(X(11), 300, X(19) - X(11), 56, MOD, ["Manipulation", "Optogenetic stimulation"])
    s.box(X(0), 390, X(10) - X(0), 56, MOD, ["Behavior", "Open field"])
    s.box(X(10), 390, X(20) - X(10), 56, MOD, ["Data acquisition", "Extracellular ephys"])
    s.box(X(20), 390, X(40) - X(20), 56, MOD, ["Behavior", "Open field (same record)"])
    s.arrow([(X(5), 241), (X(5), 390)])
    s.arrow([(X(30), 241), (X(30), 390)])
    s.arrow([(X(15), 241), (X(15), 300)])
    s.arrow([(X(10) + 14, 241), (X(10) + 14, 390)])
    s.label(X(5) + 10, 320, "linked to epoch", anchor="start")
    s.label(X(30) + 10, 320, "linked to epoch", anchor="start")
    s.note(200, 480, 1120, 62, ["Epochs are intervals relative to the session onset. One behavior or manipulation may be linked to several epochs;",
                                "a data acquisition belongs to one epoch, because a recording covers one stretch of time."])
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


SETUP_HUB_PAGES = ("setup", "equipment", "setuptype")


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


FIGURES = {
    "material-chain": material_chain, "procedure-interface-session": procedure_interface_session,
    "specimen-lineage": specimen_lineage, "templates": templates, "procedure-stages": procedure_stages,
    "epoch-timeline": epoch_timeline, "session-kinds": session_kinds, "data-model-overview": data_model_overview,
    "what-brainstem-records": what_records,
}
FIGURES.update({f"behavior-tracks-{page}": (lambda page=page: behavior_tracks(page)) for page in BEHAVIOR_TRACK_PAGES})
FIGURES.update({f"setup-hub-{page}": (lambda page=page: setup_hub(page)) for page in SETUP_HUB_PAGES})

if __name__ == "__main__":
    for name in sys.argv[1:] or FIGURES:
        FIGURES[name]()
