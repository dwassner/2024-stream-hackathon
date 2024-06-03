from typing import Dict, List
import dash_mantine_components as dmc

from .button_clear_filters import button_clear_filters
from .button_export import button_export
from .multi_select import multi_select
from .button_undo import button_undo


def get_multi_select(id_prefix, toggle_cols, visible_cols):
    id = f"{id_prefix}_multi_select"
    _class = "multi-select right"
    return multi_select(id, visible_cols, toggle_cols, _class=_class)


def ag_grid_div(
    grid,
    id_prfx: str,
    clear_filter_btn: bool = True,
    undo_btn: bool = True,
    export_btn: bool = False,
    toggle_cols: List[Dict[str, str]] = [],
    visible_cols: List = [],
):
    """
    Keyword Arugments:
    grid: Dash AG Grid
    id_prfx: Most of the cases, it is pages.route value
    clear_filter_btn: True if clear button is needed
    undo_btn: True if undo button is needed
    export_btn: True if export button is needed
    toggle_cols: list of dictionaries. Each dict is a key-value pair of "label" and "value" keys.
        This is passed as "options" in multi_select() component
    visible_cols: list of columns that is passed as "value" in multi_select() component
    """
    div = []
    if clear_filter_btn:
        div.append(button_clear_filters(f"{id_prfx}_clear_filter"))
    if undo_btn:
        div.append(button_undo(f"{id_prfx}_undo"))
    if export_btn:
        div.append(button_export(f"{id_prfx}_export"))
    if toggle_cols:
        div.append(get_multi_select(id_prfx, toggle_cols, visible_cols))
    if not div:
        return grid
    return dmc.Stack([dmc.Group(div), grid])
