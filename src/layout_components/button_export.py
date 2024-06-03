from dash_iconify import DashIconify
from .tooltip import tooltip
from .button import button


def button_export(id):
    style = {"margin-top": "-5px"}
    icon = DashIconify(
        icon="material-symbols:download",
        id=f"{id}_icon",
        width=20,
        height=20,
        style=style,
    )
    btn = button(icon, id, small=True, outlined=True)
    return tooltip(btn, "Download results")


def button_export_report(id):
    icon = DashIconify(icon="ph:export-light", width=20, height=20)
    btn = button(icon, id, small=True, outlined=True)
    return tooltip(btn, "Download table data")
