import dash_mantine_components as dmc


def loading_overlay(section, _class=None, small=False, style={}):
    loader_props = {"variant": "bars"}
    if small:
        _class = f"{_class} small" if _class else "small"
    return dmc.LoadingOverlay(
        section,
        loaderProps=loader_props,
        zIndex=10000,
        transitionDuration=1500,
        exitTransitionDuration=1000,
        overlayOpacity=50,
        className=_class,
        style=style,
    )
