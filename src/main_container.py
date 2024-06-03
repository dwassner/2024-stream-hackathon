import dash_mantine_components as dmc
from dash import html, dcc
import dash

from src.constants import TOP_MENU, SIDE_MENU


def top_menu_div():
    return dmc.Group(id=TOP_MENU, className="top-menu")


def side_menu_div():
    return html.Div(id=SIDE_MENU)


def layout():
    return html.Div(
        [
            dcc.Location(id="redirect"),
            top_menu_div(),
            side_menu_div(),
            dash.page_container,
        ]
    )
