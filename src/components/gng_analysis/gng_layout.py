from dash import Dash, html
import dash_mantine_components as dmc
from dash_iconify import DashIconify

from src.components import cns

from ...data.source import DataSource
from src.components.gng_analysis import well_log_filter, well_log_graph


def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        className=cns.GNG_WRAPPER,
        children=[
            # div wl-main-filter
            html.Div(
                className=cns.WL_MAIN_FILTER,
                children=[
                    dmc.Accordion(
                        value="well-log filter",
                        radius=10,
                        variant="contained",
                        className=cns.WL_ACCORDION_FILTER,
                        children=[
                            dmc.AccordionItem(
                                [
                                    dmc.AccordionControl(
                                        "Well-Log Filter",
                                        icon=DashIconify(
                                            icon="octicon:graph-16", width=25
                                        ),
                                    ),
                                    dmc.AccordionPanel(
                                        html.Div(
                                            children=well_log_filter.render(app, source)
                                        )
                                    ),
                                ],
                                value="well-log filter",
                            )
                        ],
                    )
                ],
            ),
            # div wl-main-graph
            html.Div(
                className=cns.WL_MAIN_GRAPHS,
                children=[
                    html.H1("Well-Log"),
                    # well_log_filter.render(app, source),
                    well_log_graph.render(app, source),
                ],
            ),
        ],
    )
