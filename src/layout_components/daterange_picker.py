from datetime import datetime, timedelta
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from .button import button


def daterange_picker(
    id,
    value=None,
    max_date=None,
    style={},
    presets=None,
    align="right",
    persistence=True,
):
    today = datetime.today()
    min_date = (today - timedelta(days=365 * 3)).strftime("%Y-%m-%d")
    if not max_date:
        max_date = today.strftime("%Y-%m-%d")
    if not value:
        month_ago = (today - timedelta(days=30)).strftime("%Y-%m-%d")
        value = [month_ago, max_date]
    icon = DashIconify(
        icon="fa:calendar",
        id=f"{id}_dt_icon",
        width=16,
        height=16,
        style={"color": "black"},
    )
    component = dmc.DateRangePicker(
        id=id,
        allowSingleDateInRange=True,
        firstDayOfWeek="sunday",
        amountOfMonths=2,
        clearable=False,
        persistence=persistence,
        minDate=min_date,
        maxDate=max_date,
        value=value,
        style=style,
        icon=icon,
        className="daterange-picker",
    )
    if not presets:
        return component
    div = [
        button(preset, f"{id}_preset_{preset}", small=True, preset=True)
        for preset in presets
    ]
    div.append(component)
    return dmc.Group(div, className=f"date-presets {align}")
