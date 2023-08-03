# from dash import Dash, html, dcc
# import dash_mantine_components as dmc
# from dash.dependencies import Input, Output
# from dash_iconify import DashIconify

# import pandas as pd
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
# # import plotly.express as px

# from ...data.loader import ProductionDataSchema
# from ...data.source import DataSource
# from .. import ids, cns


# def render(app: Dash, source: DataSource) -> html.Div:
#     @app.callback(
#         Output(ids.WATER_INJECTION_SUBPLOTS, "children"),
#         [
#             Input(ids.FROM_DATE_DATEPICKER,  "value"),
#             Input(ids.TO_DATE_DATEPICKER,    "value"),
#             Input(ids.WELL_MAIN_MULTISELECT, "value"),
#         ],  prevent_initial_call=True
#     )
    
#     def update_subplots(from_date: str, to_date: str, wells: list[str]) -> html.Div:
            
#         log_data_parameter = ['CALI','RDEP','GR','RHOB','NPHI','SP','DTC']
            
#         html.Div(
#             className=cns.PPD_PRODUCTION_FILTER,
#             children=[
                
                
#                 # filter well-log data
#                 dmc.Accordion(
#                     id='accordion-filter-well-log',
#                     value='log-data-filter-value',
#                     style={'marginTop':10, 'marginBottom':20},
#                     radius=10,
#                     children=[
                        
#                         dmc.AccordionItem([
#                             dmc.AccordionControl('Graph Filter (Well-Log Data)', icon=DashIconify(icon='material-symbols:pin-drop-outline',width=20)),
#                             dmc.AccordionPanel(
#                                 html.Div(
#                                     className='accordion-filter-well-log',
#                                     children=[
                                        
#                                         # choosing well name
#                                         html.H5('Well Name', style={'marginTop':10}),
#                                         dmc.Select(
#                                             placeholder="Select Borehole Name",
#                                             id="select-well-log",
#                                             value='well1',
#                                             data=[ 
#                                                 #   'Well-E1' 'Well-N1' 'Well-W1' 'Well-C1' 'Well-S1' 'Well-N2' 'Well-E2' 'Well-W2' 'Well-E3'
#                                                     {'label': 'Well-E1', 'value': 'well1'},
#                                                     {'label': 'Well-N1', 'value': 'well2'},
#                                                     {'label': 'Well-W1', 'value': 'well3'},
#                                                     {'label': 'Well-C1', 'value': 'well4'},
#                                                     {'label': 'Well-S1', 'value': 'well5'},
#                                                     {'label': 'Well-N2', 'value': 'well6'},
#                                                     {'label': 'Well-E2', 'value': 'well7'},
#                                                     {'label': 'Well-W2', 'value': 'well8'},
#                                                     {'label': 'Well-E3', 'value': 'well9'},
#                                                 ],
#                                             style={'marginTop':10},
#                                             clearable=True,
#                                             searchable=True,
#                                             nothingFound= 'No Options Found'
#                                             ),
                                        
#                                         # choosing well-log parameter to show
#                                         html.H5('Well-Log Parameter', style={'marginTop':30}),
#                                         dmc.CheckboxGroup(
#                                             id='checkbox-parameter-well-log',
#                                             orientation='vertical',
#                                             children=[
#                                                 # ['CALI','RDEP','GR','RHOB','NPHI','SP','DTC']
#                                                 dmc.Checkbox(label='CALI',value='CALI',color='dark', style={'marginTop':0}),
#                                                 dmc.Checkbox(label='RDEP',value='RDEP',color='dark', style={'marginTop':-15}),
#                                                 dmc.Checkbox(label='GR',value='GR',color='dark', style={'marginTop':-15}),
#                                                 dmc.Checkbox(label='RHOB',value='RHOB',color='dark', style={'marginTop':-15}),
#                                                 dmc.Checkbox(label='NPHI',value='NPHI',color='dark', style={'marginTop':-15}),
#                                                 dmc.Checkbox(label='SP',value='SP',color='dark', style={'marginTop':-15}),
#                                                 dmc.Checkbox(label='DTC',value='DTC',color='dark', style={'marginTop':-15}),
                                                
#                                             ],
#                                             value=log_data_parameter
#                                         ),

#                                         dmc.Button('Reset', id='reset-filter-well-log', variant='outline', color='dark', radius='10px', leftIcon=DashIconify(icon='material-symbols:restart-alt', width=25), 
#                                                     style={'marginTop':'25px'})

#                                     ]
#                                 )
#                             )
#                         ], value='log-data-filter-value')
#                     ], variant='contained'
#                 ), # closed accordion filter well-log


#             ]
#         ),