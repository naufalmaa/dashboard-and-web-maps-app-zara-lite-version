# from dash import Dash, html, dcc
# import dash_mantine_components as dmc
# from dash.dependencies import Input, Output
# from dash_iconify import DashIconify

# import pandas as pd
# import numpy as np
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
# # import plotly.express as px

# from ...data.loader import ProductionDataSchema
# from ...data.source import DataSource
# from .. import ids, cns


# def render(app: Dash, source: DataSource) -> html.Div:
    
#     @app.callback(
#     Output(component_id='output-graph-well-log', component_property='figure'),
#     Input(component_id='select-well-log', component_property='value'),
#     Input(component_id='checkbox-parameter-well-log', component_property='value'),
#     )

#     def build_graph(plot_chosen,checkbox_chosen):
        
#         # # 'Well-E1' 'Well-N1' 'Well-W1' 'Well-C1' 'Well-S1' 'Well-N2' 'Well-E2' 'Well-W2' 'Well-E3'
#         # dataframe_log_data = {
#         #                 'well1': well1, 
#         #                 'well2': well2, 
#         #                 'well3': well3,
#         #                 'well4': well4, 
#         #                 'well5': well5, 
#         #                 'well6': well6, 
#         #                 'well7': well7, 
#         #                 'well8': well8, 
#         #                 'well9': well9
#         #             }
        
#         # # define colors
#         # colors = ['black', 'firebrick', 'green', 'mediumaquamarine', 'royalblue', 'goldenrod', 'lightcoral']
        
#         # logplot_column = np.arange(1, 1+len(checkbox_chosen))
#         logplot_column = np.arange(1, 1+len(checkbox_chosen))
        
#         logplot = make_subplots(
#             rows=1, cols=len(checkbox_chosen),
#             shared_yaxes=True)

#         for i in range(len(checkbox_chosen)):
#             logplot.add_trace(go.Scatter(
#                 # data_new = [d['value'] for d in data]
#                                             x=dataframe_log_data[plot_chosen][checkbox_chosen[i]],
#                                             y=dataframe_log_data[plot_chosen]['DEPTH_MD'],
#                                             name=checkbox_chosen[i],
#                                             line_color=colors[i]
#                                         ),
#                                 row=1,
#                                 col=logplot_column[i],
#                                 )

#             logplot.update_xaxes(
#                                     type='log', 
#                                     row=1, 
#                                     col=logplot_column[i], 
#                                     title_text=checkbox_chosen[i],
#                                     tickfont_size=12,
#                                     linecolor='#585858'
#                                 )

#         logplot.update_xaxes(showline=True, linewidth=2, linecolor='black', mirror=True, ticks='inside', tickangle=0)
#         logplot.update_yaxes(range=[3300, 400], tickmode='linear', tick0=0, dtick=250, showline=True, linewidth=2, linecolor='black', mirror=True, ticks='outside')
#         logplot.update_layout(title=plot_chosen, height=750, width=1300, showlegend=False)

#         return logplot
    
    
#     @app.callback(
#         Output(ids.WATER_INJECTION_SUBPLOTS, "children"),
#         [
#             Input(ids.FROM_DATE_DATEPICKER,  "value"),
#             Input(ids.TO_DATE_DATEPICKER,    "value"),
#             Input(ids.WELL_MAIN_MULTISELECT, "value"),
#         ],  prevent_initial_call=True
#     )
    
#     def update_subplots(from_date: str, to_date: str, wells: list[str]) -> html.Div:
#     # for graph showing
#         html.Div(

#             className='division-graph-dashboard',
#             id='output-graph',
#             children=[

#                 html.H1('Well-Log Graph', id='title-graph-well-log', style={'marginTop':10, 'paddingLeft':650}),

#                 #graph for well-log data
#                 dcc.Graph(id='output-graph-well-log', className='graph-well-log', figure={}),

#                 html.Br(),
                
#             ]
            
#         )