import dash_mantine_components as dmc


def multi_select(
    id,
    value=None,
    options=[],
    style={},
    _class="multi-select",
    placeholder="Select columns",
    small=False,
    creatable=False,
):
    if small:
        _class = f"{_class} small"
    return dmc.MultiSelect(
        id=id,
        value=value,
        data=options,
        style=style,
        className=_class,
        placeholder=placeholder,
        searchable=True,
        creatable=creatable,
    )
