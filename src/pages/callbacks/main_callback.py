from dash.exceptions import PreventUpdate
from dash import Input, Output, State, clientside_callback, ClientsideFunction
import dash

from src.layout_components.side_menu import side_menu_content
from src.layout_components.top_menu import top_menu_content
from src.constants import SIDE_MENU, TOP_MENU
from src import routing
from src import main_container

dash.register_page(__name__)

layout = main_container.layout()


@dash.callback(
    Output(TOP_MENU, "children"),
    Output(SIDE_MENU, "children"),
    Input("redirect", "pathname"),
)
def insert_side_menu(_):
    return top_menu_content(), side_menu_content()


@dash.callback(
    Output("redirect", "href"),
    Input("redirect", "pathname"),
)
def initial_redirect(pathname):
    if pathname == routing.HOME.ROUTE:
        return routing.BUDGET.ROUTE
