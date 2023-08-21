from dash import Dash, html
import dash_mantine_components as dmc
from dash_iconify import DashIconify

from src.components import ids, cns

from ...data.source import DataSource

from ..production_performance.multiselect_helper import to_multiselect_options

from ..web_maps import (
    filter_maps,
    restart_button,
    leaflet_maps,
    filter_well_maps,
    restart_well_button,
)

from ..web_maps.data_color_map import colormap


def create_layout_map(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        className=cns.MAP_WRAPPER,
        children=[
            
            # div left-side map (content(2)) map filter
            html.Div(
                className=cns.LEFT_SIDE_MAP,
                children=[
                    html.Div(
                        className=cns.TITLE_SUMMARY_LAYOUT,
                        children=[
                            html.H1("Dummy Block", className=cns.TITLE_BLOCK),
                            html.H4("Summary"),
                            dmc.Spoiler(
                                className=cns.SUMMARY_BLOCK,
                                showLabel="Show More",
                                hideLabel="Hide",
                                maxHeight=50,
                                style={"marginBottom": 35},
                                children=[
                                    dmc.Text(
                                        """
                                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi luctus elit at eros accumsan iaculis. Nulla facilisi. Morbi vitae venenatis ante. Nulla dui tellus, euismod at malesuada ac, luctus quis orci. Nullam in eros mollis, vulputate neque ut, vulputate dolor. In sed ultrices mauris. Ut vitae dolor augue. Ut ac purus eu felis scelerisque facilisis. Donec consectetur odio orci, non volutpat eros suscipit vestibulum. Quisque a fermentum massa. Sed ac nibh nibh.
                                        """
                                    )
                                ],
                            ),
                        ],
                    ),
                    html.Div(
                        className=cns.MAP_ALL_FILTER,
                        children=[
                            # MAP COLOR FILTER
                            dmc.Accordion(
                                # value="color map filter",
                                radius=10,
                                variant="contained",
                                style={"marginBottom": 10},
                                children=[
                                    dmc.AccordionItem(
                                        [
                                            dmc.AccordionControl(
                                                "Map Settings",
                                                icon=DashIconify(
                                                    icon="ic:twotone-map", width=25
                                                ),
                                            ),
                                            dmc.AccordionPanel(
                                                html.Div(
                                                    children=[
                                                        # MAP COLOR FILTER
                                                        html.H5("Layout Map"),
                                                        dmc.RadioGroup(
                                                            [
                                                                dmc.Radio(
                                                                    i, value=k, color=c
                                                                )
                                                                for i, k, c in colormap()
                                                            ],
                                                            id=ids.MAP_COLOR,
                                                            value="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
                                                            orientation="vertical",
                                                            spacing="xs",
                                                        ),
                                                    ]
                                                )
                                            ),
                                        ],
                                        value="color map filter",
                                    )
                                ],
                            ),
                            # BLOCK FILTER
                            dmc.Accordion(
                                # value="block filter",
                                radius=10,
                                variant="contained",
                                style={"marginBottom": 10},
                                children=[
                                    dmc.AccordionItem(
                                        [
                                            dmc.AccordionControl(
                                                "Block Filter",
                                                icon=DashIconify(
                                                    icon="mdi:surface-area", width=20
                                                ),
                                            ),
                                            dmc.AccordionPanel(
                                                html.Div(
                                                    children=[
                                                        filter_maps.render(app, source),
                                                        restart_button.render(app, source),
                                                    ]
                                                )
                                            ),
                                        ],
                                        value="block filter",
                                    )
                                ],
                            ),
                            # WELL FILTER
                            dmc.Accordion(
                                # value="well filter",
                                radius=10,
                                variant="contained",
                                children=[
                                    dmc.AccordionItem(
                                        [
                                            dmc.AccordionControl(
                                                "Well Filter",
                                                icon=DashIconify(
                                                    icon="material-symbols:pin-drop-outline",
                                                    width=20,
                                                ),
                                            ),
                                            dmc.AccordionPanel(
                                                html.Div(
                                                    children=[
                                                        filter_well_maps.render(
                                                            app, source
                                                        ),
                                                        restart_well_button.render(
                                                            app, source
                                                        ),
                                                    ]
                                                )
                                            ),
                                        ],
                                        value="well filter",
                                    )
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            # div map-map (content(3))
            html.Div(
                className=cns.MAP_LEAFLET, children=[leaflet_maps.render(app, source)]
            ),

        ],
    )
