"""Colours and type for the static drawings of the support site, shared by render_diagrams.py and
render_example_figure.py.

The app colours are those of BrainSTEM's interactive data model (the --dm-group-* tokens of
data-model-diagram.css), so a model has the same colour in every drawing and in the interactive view.
The main records of a drawing are drawn solid in their app colour; supporting models are drawn faint, as
a pale tint of their app colour with a coloured outline."""

FONT = "Inter, 'Segoe UI', Helvetica, Arial, sans-serif"

APP = {
    "stem": "#8122a1",                 # STEM data: projects, subjects, specimen sets, sessions, epochs
    "modules": "#2f7f8a",              # Modules: procedures, interfaces, acquisitions, behavior, logs, stock
    "personal_attributes": "#3f6bb3",  # Personal attributes: setups, inventories, storage, protocols, licenses
    "resources": "#9a5a14",            # Resources: the shared catalog of consumables, devices, suppliers
    "taxonomies": "#6b7c2a",           # Taxonomies: species, strains, atlases and regions, paradigms
    "dissemination": "#a8365e",        # Dissemination: publications, journals
    "users": "#51459d",                # Users and groups
}
APP_LABEL = {
    "stem": "STEM data", "modules": "Modules", "personal_attributes": "Personal attributes",
    "resources": "Resources", "taxonomies": "Taxonomies", "dissemination": "Dissemination", "users": "Users",
}
STEM, MOD, PA, CAT, TAX, DIS, USR = (APP[k] for k in
    ("stem", "modules", "personal_attributes", "resources", "taxonomies", "dissemination", "users"))

EDGE = "#6f6d82"      # connectors
LABEL = "#4a4858"     # connector labels
INK = "#2c2a38"       # body text on light fills
NOTE_FILL, NOTE_STROKE = "#fbf8ee", "#d8d0b4"


def _rgb(color):
    color = color.lstrip("#")
    return [int(color[i:i + 2], 16) for i in (0, 2, 4)]


def mix(color, other, amount):
    """`amount` of `color` mixed into `other` (both #rrggbb)."""
    a, b = _rgb(color), _rgb(other)
    return "#" + "".join(f"{round(x * amount + y * (1 - amount)):02x}" for x, y in zip(a, b))


def tint(color, amount=0.11):
    """The pale fill of a supporting model."""
    return mix(color, "#ffffff", amount)


def outline(color):
    """The outline of a supporting model."""
    return mix(color, "#ffffff", 0.55)


def dark(color, amount=0.72):
    """Title text on a tint, and the outline of a solid box."""
    return mix(color, "#000000", amount)
