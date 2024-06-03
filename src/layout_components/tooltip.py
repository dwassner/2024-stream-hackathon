import dash_mantine_components as dmc


def tooltip(target_element, label):
    return dmc.Tooltip(
        target_element,
        label=label,
        withArrow=True,
        transition="slide-up",
        transitionDuration=300,
    )
