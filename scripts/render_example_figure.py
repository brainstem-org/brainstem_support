"""Draw the data-model example figure (docs/assets/images/diagrams/data-model-example.svg): one ephys session in a rat, as table cards.

Edit the cards below and rerun: python scripts/render_example_figure.py"""
import sys
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).resolve().parent))
from diagram_style import FONT, STEM, MOD, EDGE, LABEL, INK, tint, outline, dark  # noqa: E402

ROW, HEAD, PAD = 30, 36, 10
# Colours by app, as in the interactive data model: the project, subject and session are drawn solid (STEM data);
# the records around them faint (Modules). Coordinates are fields of a procedure, not a model: neutral grey.
#        header fill, body fill, outline, title colour
COL = {
    "stem": (STEM, tint(STEM, 0.05), dark(STEM), "#fff"),
    "module": (tint(MOD, 0.2), "#ffffff", outline(MOD), dark(MOD)),
    "field": ("#efeef4", "#ffffff", "#c9c6d6", INK),
}
COL.update({"project": COL["stem"], "subject": COL["stem"], "session": COL["stem"], "procedure": COL["module"],
            "interface": COL["module"], "acq": COL["module"], "material": COL["module"], "coords": COL["field"]})
parts = []; W = 0; H = 0
def text(x, y, s, bold=False, size=15, anchor="start", underline=False, fill=INK):
    weight = "700" if bold else "400"
    deco = ' text-decoration="underline"' if underline else ""
    parts.append(f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" text-anchor="{anchor}" '
                 f'font-weight="{weight}" fill="{fill}"{deco}>{escape(s)}</text>')
def card(x, y, w, kind, title, rows, subtitle=None, label_w=None):
    """A card: coloured header with the title, then label/value rows. Rows: (label, value, is_link). Returns bottom y."""
    global W, H
    head, body, line, title_ink = COL[kind]
    label_w = label_w or max(len(r[0]) for r in rows) * 8.4 + 2 * PAD
    h = HEAD + len(rows) * ROW + (26 if subtitle else 0)
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{body}" stroke="{line}" stroke-width="1.2"/>')
    parts.append(f'<path d="M{x+6},{y} h{w-12} a6,6 0 0 1 6,6 v{HEAD-6} h-{w} v-{HEAD-6} a6,6 0 0 1 6,-6 z" fill="{head}"/>')
    parts.append(f'<path d="M{x},{y+HEAD} h{w}" stroke="{line}" stroke-width="1"/>')
    text(x + PAD, y + 24, title, bold=True, size=16, fill=title_ink)
    yy = y + HEAD
    if subtitle:
        text(x + PAD, yy + 18, subtitle, bold=True, size=13, fill=LABEL); yy += 26
        parts.append(f'<path d="M{x},{yy} h{w}" stroke="#c9c6d6" stroke-width="0.8"/>')
    for i, (lab, val, link) in enumerate(rows):
        ry = yy + i * ROW
        text(x + PAD, ry + 20, lab, size=14, underline=link, fill=INK)
        text(x + label_w + PAD, ry + 20, val, size=14)
        parts.append(f'<path d="M{x},{ry+ROW} h{w}" stroke="#dcdae6" stroke-width="0.6"/>' if i < len(rows) - 1 else "")
    parts.append(f'<path d="M{x+label_w},{yy} v{len(rows)*ROW}" stroke="#dcdae6" stroke-width="0.6"/>')
    W = max(W, x + w); H = max(H, y + h)
    return y + h
def elbow(x1, y1, x2, y2, arrow=True):
    my = (y1 + y2) / 2
    mk = ' marker-end="url(#arrow)"' if arrow else ""
    parts.append(f'<path d="M{x1},{y1} L{x1},{my} L{x2},{my} L{x2},{y2}" fill="none" stroke="{EDGE}" stroke-width="1.3"{mk}/>')
def hline(x1, x2, y):
    parts.append(f'<path d="M{x1},{y} L{x2},{y}" fill="none" stroke="{EDGE}" stroke-width="1.3"/>')
def vline(x, y1, y2, arrow=True):
    mk = ' marker-end="url(#arrow)"' if arrow else ""
    parts.append(f'<path d="M{x},{y1} L{x},{y2}" fill="none" stroke="{EDGE}" stroke-width="1.3"{mk}/>')

# Row 0: project
px, pw = 760, 400
pb = card(px, 20, pw, "project", "Project", [("Name", "Place cells 2026", False), ("Groups", "Buzsaki Lab", True), ("Public access", "Private", False)])
# Row 1: subject and session
sx, sw = 440, 400; ssx, ssw = 1080, 400; y1 = 200
hline(px + pw/2, px + pw/2, pb)
elbow(px + pw/2, pb, sx + sw/2, y1); elbow(px + pw/2, pb, ssx + ssw/2, y1)
sb = card(sx, y1, sw, "subject", "Subject", [("Name", "Rat 17", False), ("Species", "Rattus norvegicus", True), ("Strain", "Long Evans", True), ("Sex", "Male", False), ("Status", "Active", False)])
seb = card(ssx, y1, ssw, "session", "Session", [("Name", "Rat17_2026-03-13", False), ("Date and time onset", "13 March 2026, 10:00", False), ("Subjects", "Rat 17", True), ("Data storage", "nas://lab/working", True), ("Epochs", "Baseline, Task, Rest", True)])
# Row 2: procedures under the subject; modules under the session
y2 = 460
pr1x, pr1w = 20, 400; pr2x, pr2w = 440, 400
elbow(sx + sw/2, sb, pr1x + pr1w/2, y2); vline(sx + sw/2, sb, y2)
b1 = card(pr1x, y2, pr1w, "procedure", "Silicon probe implant", [("Date and time", "10 March 2026", False), ("Subject", "Rat 17", True), ("Target regions", "CA1", True), ("Protocol", "Chronic implant v3", True), ("Status", "Performed", False)])
b1 = card(pr1x, b1 + 8, pr1w, "material", "Materials", [("Silicon probe", "ASSY-156 (NeuroNexus)", True), ("Source", "Inventory: probes cabinet", False), ("Adhesive, cement", "C&B Metabond", True), ("Anchor screw", "Stainless M1", True)], subtitle="one row per material used")
b1 = card(pr1x, b1 + 8, pr1w, "coords", "Coordinates", [("AP", "-3.5 mm", False), ("ML", "2.5 mm", False), ("Depth", "1.6 mm", False), ("ML angle", "10°", False)], subtitle="Bregma stereotaxic, from brain surface")
b2 = card(pr2x, y2, pr2w, "procedure", "Virus injection", [("Date and time", "5 March 2026", False), ("Subject", "Rat 17", True), ("Target regions", "CA1", True), ("Injection volume", "50 µL", False), ("Injection rate", "10 µL/min", False)])
b2 = card(pr2x, b2 + 8, pr2w, "material", "Materials", [("Viral vector", "AAV1-CaMKII-GCaMP6f", True), ("Source", "Inventory: -80 °C freezer", False)], subtitle="one row per material used")
b2 = card(pr2x, b2 + 8, pr2w, "coords", "Coordinates", [("AP", "-3.5 mm", False), ("ML", "2.5 mm", False), ("Depth", "1.6 mm", False)], subtitle="Bregma stereotaxic, from brain surface")
# the implant creates an interface
ix, iw = 20, 400
yi = b1 + 40
vline(pr1x + pr1w/2, b1, yi)
text(pr1x + pr1w/2 + 10, yi - 14, "creates", size=13, fill=LABEL)
bi = card(ix, yi, iw, "interface", "Experimental interface", [("Type", "Silicon probe", False), ("Subject", "Rat 17", True), ("Target region", "CA1", True), ("Coordinates", "copied from the implant", False), ("Persistence", "Chronic", False)], subtitle="the implanted probe, kept across sessions")
# session modules
m1x, m1w = 880, 400; m2x, m2w = 1300, 400; m3x, m3w = 1720, 400
for mx, mw in [(m1x, m1w), (m2x, m2w), (m3x, m3w)]:
    elbow(ssx + ssw/2, seb, mx + mw/2, y2)
c1 = card(m1x, y2, m1w, "acq", "Data acquisition: Extracellular ephys", [("Session", "Rat17_2026-03-13", True), ("Interfaces", "Silicon probe in CA1", True), ("Equipment", "Intan RHD2000", True), ("File name", "dataset1.dat", False), ("Sampling rate", "20000 Hz", False), ("Channels", "128", False), ("Epoch", "Task", True)])
c2 = card(m2x, y2, m2w, "acq", "Data acquisition: Behavioral tracking", [("Session", "Rat17_2026-03-13", True), ("Equipment", "Basler camera", True), ("File name", "behavior1.avi", False), ("Frame rate", "30 Hz", False), ("Resolution", "640 × 480", False)])
c3 = card(m3x, y2, m3w, "acq", "Behavior", [("Session", "Rat17_2026-03-13", True), ("Behavioral assay", "Alternation run", True), ("Setup", "Linear track rig", True), ("Behavioral paradigm", "Spatial alternation", True), ("Epoch", "Task", True)])
# interface -> data acquisition link
ly = yi + HEAD + 26 + ROW * 1.5
parts.append(f'<path d="M{ix+iw},{ly} L{m1x+m1w/2},{ly} L{m1x+m1w/2},{c1+2}" fill="none" stroke="{EDGE}" stroke-width="1.3" stroke-dasharray="6 4" marker-end="url(#arrow)"/>')
text(ix + iw + 14, ly - 8, "the recording names the interface it was made through", size=13, fill=LABEL)

width, height = W + 20, H + 20
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" '
       f'aria-label="Example: an extracellular recording session in a rat, as BrainSTEM records it">\n<title>Example: an extracellular recording session in a rat</title>\n'
       f'<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{EDGE}"/></marker></defs>\n'
       f'<rect width="{width}" height="{height}" fill="#fff"/>\n' + "\n".join(p for p in parts if p) + "\n</svg>\n")
open(__import__("pathlib").Path(__file__).resolve().parents[1] / "docs" / "assets" / "images" / "diagrams" / "data-model-example.svg", "w").write(svg)
print("size", width, height)
