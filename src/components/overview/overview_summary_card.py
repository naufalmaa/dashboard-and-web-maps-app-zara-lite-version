from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

from ...data.source import DataSource
from .. import ids, cns


def render(app: Dash, source: DataSource) -> html.Div:
    # @app.callback(
    #     Output(ids.TOTAL_OIL_PRODUCTION_AMOUNT_CARD, "children"),
    #     Output(ids.TOTAL_GAS_PRODUCTION_AMOUNT_CARD, "children"),
    #     Output(ids.TOTAL_WATER_INJECTION_AMOUNT_CARD, "children"),
    #     Output(ids.ON_STREAM_TIME_AMOUNT_CARD, "children"),
    #     [
    #         Input(ids.FROM_DATE_DATEPICKER, "value"),
    #         Input(ids.TO_DATE_DATEPICKER, "value"),
    #         Input(ids.WELL_MAIN_MULTISELECT, "value"),
    #     ],
    #     prevent_initial_call=True,
    # )
    # def calculate_total() -> float:
    #     generate_sum_oil = source.filter(
    #         from_date=from_date, to_date=to_date, wells=wells
    #     ).sum_oil
    #     generate_sum_gas = source.filter(
    #         from_date=from_date, to_date=to_date, wells=wells
    #     ).sum_gas
    #     generate_sum_wi = source.filter(
    #         from_date=from_date, to_date=to_date, wells=wells
    #     ).sum_wi
    #     generate_sum_on_hours = source.filter(
    #         from_date=from_date, to_date=to_date, wells=wells
    #     ).sum_on_hours

    #     abb_sum_oil = source.abbreviate_value(generate_sum_oil)
    #     abb_sum_gas = source.abbreviate_value(generate_sum_gas)
    #     abb_sum_wi = source.abbreviate_value(generate_sum_wi)
    #     abb_sum_on_hours = source.abbreviate_value(generate_sum_on_hours)

    #     return (
    #         f"{abb_sum_oil}",
    #         f"{abb_sum_gas}",
    #         f"{abb_sum_wi}",
    #         f"{abb_sum_on_hours}",
    #     )

    return html.Div(
        html.Div(
            className=cns.OVW_SUMMARY_CARD_WRAPPER,
            children=[
                dmc.CardSection(
                    className=cns.OVW_SC_CARDSECTION,
                    children=[
                        dmc.SimpleGrid(
                            className=cns.OVW_SC_SIMPLEGRID,
                            cols=6,
                            children=[
                                dmc.Group(
                                    className=cns.OVW_SC_GROUP,
                                    children=[
                                        dmc.Card(
                                            className=cns.OVW_SC_CARD,
                                            children=[
                                                DashIconify(
                                                    className=cns.OVW_SC_ICON,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    icon="material-symbols:factory",
                                                    color="#012226",
                                                    height=40,
                                                    width=40,
                                                    style={
                                                        "marginTop": 5,
                                                        "marginRight": 10,
                                                        "float": "left",
                                                    },
                                                ),
                                                dmc.Title(
                                                    f"Total Oil Blocks",
                                                    className=cns.OVW_SC_TITLE,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    weight="500",
                                                    order=5,
                                                    align="left",
                                                    color="#25262B",
                                                    # color='red',
                                                    style={
                                                        "marginLeft": 10,
                                                        "fontSize": 20,
                                                    },
                                                ),
                                                dmc.Text(
                                                    "5",
                                                    id=ids.TOTAL_OIL_BLOCKS_AMOUNT_CARD,
                                                    className=cns.OVW_SC_TEXT,
                                                    align="center",
                                                    color="#25262B",
                                                    # color='red',
                                                    style={
                                                        "fontSize": 40,
                                                        "fontWeight": "bold",
                                                    },
                                                ),
                                            ],
                                            withBorder=True,
                                            radius="20px",
                                            style={
                                                "background-color": "#FFFFFF",
                                                "border": "2px solid #012226",
                                            },
                                        ),
                                    ],
                                ),
                                dmc.Group(
                                    className=cns.OVW_SC_GROUP,
                                    children=[
                                        dmc.Card(
                                            className=cns.OVW_SC_CARD,
                                            children=[
                                                DashIconify(
                                                    className=cns.OVW_SC_ICON,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    icon="mdi:worker",
                                                    color="#012226",
                                                    height=40,
                                                    width=40,
                                                    style={
                                                        "marginTop": 5,
                                                        "marginRight": 10,
                                                        "float": "left",
                                                    },
                                                ),
                                                dmc.Title(
                                                    f"Total Operators",
                                                    className=cns.OVW_SC_TITLE,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    weight="500",
                                                    order=5,
                                                    align="left",
                                                    color="#25262B",
                                                    # color='red',
                                                    style={
                                                        "marginLeft": 10,
                                                        "fontSize": 20,
                                                    },
                                                ),
                                                dmc.Text(
                                                    "5",
                                                    id=ids.TOTAL_OPERATORS_AMOUNT_CARD,
                                                    className=cns.OVW_SC_TEXT,
                                                    align="center",
                                                    color="#25262B",
                                                    # color='red',
                                                    style={
                                                        "fontSize": 40,
                                                        "fontWeight": "bold",
                                                    },
                                                ),
                                            ],
                                            withBorder=True,
                                            radius="20px",
                                            style={
                                                "background-color": "#FFFFFF",
                                                "border": "2px solid #012226",
                                            },
                                        ),
                                    ],
                                ),
                                dmc.Group(
                                    className=cns.OVW_SC_GROUP,
                                    children=[
                                        dmc.Card(
                                            className=cns.OVW_SC_CARD,
                                            children=[
                                                DashIconify(
                                                    className=cns.OVW_SC_ICON,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    icon="fa6-solid:oil-well",
                                                    color="#012226",
                                                    height=40,
                                                    width=40,
                                                    style={
                                                        "marginTop": 5,
                                                        "marginRight": 10,
                                                        "float": "left",
                                                    },
                                                ),
                                                dmc.Title(
                                                    f"Total Number of Wells - Monitor Wells",
                                                    className=cns.OVW_SC_TITLE,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    weight="500",
                                                    order=5,
                                                    align="left",
                                                    color="#25262B",
                                                    # color='red',
                                                    style={
                                                        "marginLeft": 10,
                                                        "fontSize": 20,
                                                    },
                                                ),
                                                dmc.Text(
                                                    "120 - 9",
                                                    id=ids.TOTAL_NUM_OF_WELLS_AMOUNT_CARD,
                                                    className=cns.OVW_SC_TEXT,
                                                    align="center",
                                                    color="#25262B",
                                                    # color='red',
                                                    style={
                                                        "fontSize": 40,
                                                        "fontWeight": "bold",
                                                    },
                                                ),
                                            ],
                                            withBorder=True,
                                            radius="20px",
                                            style={
                                                "background-color": "#FFFFFF",
                                                "border": "2px solid #012226",
                                            },
                                        ),
                                    ],
                                ),
                                dmc.Group(
                                    className=cns.OVW_SC_GROUP,
                                    children=[
                                        dmc.Card(
                                            className=cns.OVW_SC_CARD,
                                            children=[
                                                DashIconify(
                                                    className=cns.OVW_SC_ICON,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    icon="material-symbols:oil-barrel",
                                                    color="#012226",
                                                    height=40,
                                                    width=40,
                                                    style={
                                                        "marginTop": 5,
                                                        "marginRight": 10,
                                                        "float": "left",
                                                    },
                                                ),
                                                dmc.Title(
                                                    f"Average Oil Production / Month (m\u00b3/month)",
                                                    className=cns.OVW_SC_TITLE,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    weight="500",
                                                    order=5,
                                                    align="left",
                                                    color="#25262B",
                                                    # color='red',
                                                    style={
                                                        "marginLeft": 10,
                                                        "fontSize": 20,
                                                    },
                                                ),
                                                dmc.Text(
                                                    "22K",
                                                    id=ids.AVG_OIL_PRODUCTION_MONTH_AMOUNT_CARD,
                                                    className=cns.OVW_SC_TEXT,
                                                    align="center",
                                                    color="#25262B",
                                                    # color='red',
                                                    style={
                                                        "fontSize": 40,
                                                        "fontWeight": "bold",
                                                    },
                                                ),
                                            ],
                                            withBorder=True,
                                            radius="20px",
                                            style={
                                                "background-color": "#FFFFFF",
                                                "border": "2px solid #012226",
                                            },
                                        ),
                                    ],
                                ),
                                dmc.Group(
                                    className=cns.OVW_SC_GROUP,
                                    children=[
                                        dmc.Card(
                                            className=cns.OVW_SC_CARD,
                                            children=[
                                                DashIconify(
                                                    className=cns.OVW_SC_ICON,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    icon="ic:sharp-gas-meter",
                                                    color="#012226",
                                                    height=40,
                                                    width=40,
                                                    style={
                                                        "marginTop": 5,
                                                        "marginRight": 10,
                                                        "float": "left",
                                                    },
                                                ),
                                                dmc.Title(
                                                    f"Average Gas Production / Month (m\u00b3/month)",
                                                    className=cns.OVW_SC_TITLE,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    weight="500",
                                                    order=5,
                                                    align="left",
                                                    color="#25262B",
                                                    # color='red',
                                                    style={
                                                        "marginLeft": 10,
                                                        "fontSize": 20,
                                                    },
                                                ),
                                                dmc.Text(
                                                    "300K",
                                                    id=ids.AVG_GAS_PRODUCTION_MONTH_AMOUNT_CARD,
                                                    className=cns.OVW_SC_TEXT,
                                                    align="center",
                                                    color="#25262B",
                                                    # color='red',
                                                    style={
                                                        "fontSize": 40,
                                                        "fontWeight": "bold",
                                                    },
                                                ),
                                            ],
                                            withBorder=True,
                                            radius="20px",
                                            style={
                                                "background-color": "#FFFFFF",
                                                "border": "2px solid #012226",
                                            },
                                        ),
                                    ],
                                ),
                                dmc.Group(
                                    className=cns.OVW_SC_GROUP,
                                    children=[
                                        dmc.Card(
                                            className=cns.OVW_SC_CARD,
                                            children=[
                                                DashIconify(
                                                    className=cns.OVW_SC_ICON,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    icon="iconoir:depth",
                                                    color="#012226",
                                                    height=40,
                                                    width=40,
                                                    style={
                                                        "marginTop": 5,
                                                        "marginRight": 10,
                                                        "float": "left",
                                                    },
                                                ),
                                                dmc.Title(
                                                    f"Average Depth of Wells (TVD) (m)",
                                                    className=cns.OVW_SC_TITLE,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    weight="500",
                                                    order=5,
                                                    align="left",
                                                    color="#25262B",
                                                    # color='red',
                                                    style={
                                                        "marginLeft": 10,
                                                        "fontSize": 20,
                                                    },
                                                ),
                                                dmc.Text(
                                                    "5.2K",
                                                    id=ids.AVG_DEPTH_AMOUNT_CARD,
                                                    className=cns.OVW_SC_TEXT,
                                                    align="center",
                                                    color="#25262B",
                                                    # color='red',
                                                    style={
                                                        "fontSize": 40,
                                                        "fontWeight": "bold",
                                                    },
                                                ),
                                            ],
                                            withBorder=True,
                                            radius="20px",
                                            style={
                                                "background-color": "#FFFFFF",
                                                "border": "2px solid #012226",
                                            },
                                        ),
                                    ],
                                ),
                            ],
                            style={"marginTop": 20},
                        ),
                    ],
                )
            ],
        ),
        # style={'display': 'grid', 'grid-template-columns': '1fr 1fr 1fr 1fr', 'grid-template-rows': 'auto'},
        className=cns.OVW_SUMMARY_CARD_WRAPPER,
    )
