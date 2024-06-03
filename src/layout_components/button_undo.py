from dash_iconify import DashIconify
from .tooltip import tooltip
from .button import button


def button_undo(id):
    icon = DashIconify(icon="fa:undo", id=f"{id}_icon", width=16, height=16)
    btn = button(icon, id, small=True, outlined=True)
    return tooltip(btn, "Undo last update")
