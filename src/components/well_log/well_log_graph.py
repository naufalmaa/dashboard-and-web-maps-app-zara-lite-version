from dash import Dash, html, dcc
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# import plotly.express as px

from ...data.loader import LogDataSchema
from ...data.source import DataSource
from .. import ids, cns


def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(component_id="output-graph-well-log", component_property="children"),
        [
            Input(component_id="select-well-log", component_property="value"),
            Input(component_id="checkbox-parameter-well-log", component_property="value"),
        ],
        prevent_initial_call=True,
    )
    def build_graph(well_chosen, params_chosen):
        # # 'Well-E1' 'Well-N1' 'Well-W1' 'Well-C1' 'Well-S1' 'Well-N2' 'Well-E2' 'Well-W2' 'Well-E3'
        # dataframe_log_data = {
        #                 'well1': well1,
        #                 'well2': well2,
        #                 'well3': well3,
        #                 'well4': well4,
        #                 'well5': well5,
        #                 'well6': well6,
        #                 'well7': well7,
        #                 'well8': well8,
        #                 'well9': well9
        #             }

        # # define colors
        # colors = ['black', 'firebrick', 'green', 'mediumaquamarine', 'royalblue', 'goldenrod', 'lightcoral']

        # figure_column = np.arange(1, 1+len(params_chosen))

        filtered_well_log_data = source.filter_log(
            wells=well_chosen, params=params_chosen
        ).to_dataframe

        figure_column = np.arange(1, 1 + len(params_chosen))

        figure = make_subplots(rows=1, cols=len(params_chosen), shared_yaxes=True)

        for i in range(len(params_chosen)):
            figure.add_trace(
                go.Scatter(
                    # data_new = [d['value'] for d in data]
                    x=filtered_well_log_data[params_chosen[i]],
                    y=filtered_well_log_data[LogDataSchema.DEPTH],
                    name=params_chosen[i],
                    # line_color=colors[i]
                ),
                row=1,
                col=figure_column[i],
            )

            figure.update_xaxes(
                type="log",
                row=1,
                col=figure_column[i],
                title_text=params_chosen[i],
                tickfont_size=12,
                linecolor="#585858",
            )

        figure.update_xaxes(
            showline=True,
            linewidth=2,
            linecolor="black",
            mirror=True,
            ticks="inside",
            tickangle=0,
        )
        figure.update_yaxes(
            range=[3300, 400],
            tickmode="linear",
            tick0=0,
            dtick=250,
            showline=True,
            linewidth=2,
            linecolor="black",
            mirror=True,
            ticks="outside",
        )
        figure.update_layout(
            title=well_chosen, height=750, width=1200, showlegend=True
        )

        return \
            html.Div(  # graph for well-log data
                dcc.Graph(figure=figure),
                id="output-graph-well-log",
                className=cns.WL_FIRST_GRAPH
            ),
        

    return html.Div(
        id="output-graph-well-log",
        className=cns.WL_FIRST_GRAPH,
        # children=[
        #     html.H1(
        #         "Well-Log Graph",
        #         id="title-graph-well-log",
        #         style={"marginTop": 10, "paddingLeft": 10},
        #     ),
        #     # graph for well-log data
        #     dcc.Graph(
        #         id="output-graph-well-log", className=cns.WL_FIRST_GRAPH, figure={}
        #     ),
        #     html.Br(),
        # ],
    )
