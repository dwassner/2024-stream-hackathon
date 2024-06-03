import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import html

from .tooltip import tooltip


def icon_button(
    icon, id, icon_color="#F78B27", tooltip_text=None, link=None, **extra_kwargs
):
    icon_item = DashIconify(
        icon=icon, id=f"{id}_icon", width=20, height=20, color=icon_color
    )
    kwargs = {"children": icon_item, "id": id, "className": "button icon"}
    if link:
        kwargs.pop("id")

    kwargs.update(**extra_kwargs)
    btn = dmc.Button(**kwargs)
    if link:
        btn = html.A(btn, id=id, href=link, target="blank")
    if tooltip:
        return tooltip(btn, tooltip_text)
    return btn
