from dash import Input, Output, State, ctx, clientside_callback, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash

from src.pages.procs.placements_proc import placements_table
from src.pages.layouts import placements_layout
from src.helpers import date_presets
from src.routing import PLACEMENTS

dash.register_page(__name__, path=PLACEMENTS.ROUTE, name=PLACEMENTS.TITLE)

layout = placements_layout.layout


@dash.callback(
    Output(f"{PLACEMENTS.ROUTE}_dates", "value"),
    Input(f"{PLACEMENTS.ROUTE}_dates_preset_7", "n_clicks"),
    Input(f"{PLACEMENTS.ROUTE}_dates_preset_14", "n_clicks"),
    Input(f"{PLACEMENTS.ROUTE}_dates_preset_30", "n_clicks"),
    Input(f"{PLACEMENTS.ROUTE}_dates_preset_60", "n_clicks"),
    Input(f"{PLACEMENTS.ROUTE}_dates_preset_90", "n_clicks"),
    State("redirect", "pathname"),
    prevent_initial_call=True,
)
def dates_preset_callback(_1, _2, _3, _4, _5, pathname):
    if len(ctx.triggered) != 1:
        raise PreventUpdate
    preset = ctx.triggered_id.split("_")[-1]
    return date_presets.get_date_range(preset)


@dash.callback(
    Output(f"{PLACEMENTS.ROUTE}_data", "data"),
    Output(f"{PLACEMENTS.ROUTE}_table", "children"),
    Output(f"{PLACEMENTS.ROUTE}_chart", "data"),
    Input("redirect", "pathname"),
    Input(f"{PLACEMENTS.ROUTE}_dates", "value"),
)
def main_callback(_, dates):
    if dates:
        data, table = placements_table.get_data(dates)
        return data, table, dash.no_update
    raise PreventUpdate


clientside_callback(
    ClientsideFunction(namespace="placements", function_name="prepare_chart"),
    Output(f"{PLACEMENTS.ROUTE}_chart", "children", allow_duplicate=True),
    Input(f"{PLACEMENTS.ROUTE}_data", "data"),
    State(f"{PLACEMENTS.ROUTE}_chart", "id"),
    prevent_initial_call=True,
)
