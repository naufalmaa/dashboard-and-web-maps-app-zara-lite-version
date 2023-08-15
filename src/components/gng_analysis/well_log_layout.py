# from dash import Dash, html

# from src.components import cns

# from ...data.source import DataSource
# from src.components.well_log import well_log_filter, well_log_graph


# def create_layout(app: Dash, source: DataSource) -> html.Div:
#     return html.Div(
#         className="xxx",
#         children=[
#             # # Content left side PRODUCTION FILTER (Content(4))
#             # html.Div(
#             #     className="xxxx",
#             #     children=[
#             #         well_log_filter.render(app, source),
#             #         ]
#             #     ),
#             # Content Right Side PRODUCTION GRAPH (Content(5))
#             html.Div(
#                 className="xxx",
#                 children=[
#                     html.H2(
#                         "Well-Log Graph",
#                         className=cns.PPD_H2,
#                         style={"marginTop": 30, "text-align": "center"},
#                     ),
#                     well_log_graph.render(app, source),
#                 ],
#                 style={},
#             ),
#         ],
#         style={},
#     ),
