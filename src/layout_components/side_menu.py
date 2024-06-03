import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import html

from src import routing as pages


def icon_large(icon, item_name):
    icon = DashIconify(icon=icon, width=25, color="#f90", className="sidemenu-icons")
    label = html.Font(item_name)
    return dmc.Group([icon, label])


def create_menu_item(icon, item_name, item_link):
    return dbc.NavLink(
        icon_large(icon, item_name),
        href=item_link,
        active="exact",
        className="nav-link",
    )


def create_dbc_nav_section(*args, label=None, top_spacing=True):
    contents = [
        dmc.Divider(label=label, labelPosition="center", styles={"font-size": "50px"}),
        dbc.Nav(children=[arg for arg in args], vertical=True, pills=True, fill=True),
    ]
    if top_spacing:
        contents.insert(0, html.Div(style={"height": "20px"}))
    return html.Div(contents)


def side_menu_content():
    items = [pages.BUDGET, pages.PLACEMENTS, pages.SETUP]
    args = [create_menu_item(*item) for item in items]
    return create_dbc_nav_section(*args)
