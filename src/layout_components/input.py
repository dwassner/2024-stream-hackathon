import dash_bootstrap_components as dbc


def input(id, placeholder=None, style={}, small=False, **kwargs):
    _class = "input"
    if small:
        _class += " small"
    return dbc.Input(
        id=id,
        placeholder=placeholder,
        style=style,
        className=_class,
        debounce=True,
        **kwargs
    )
