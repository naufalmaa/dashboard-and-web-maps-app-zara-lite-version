# from dash import Dash, html
# import dash_mantine_components as dmc
# from dash.dependencies import Input, Output
# from dash_iconify import DashIconify

# from ...data.source import DataSource
# from ...components import ids, cns

# def render(app: Dash, source: DataSource) -> html.Div:

#     @app.callback(
#         Output('multiselect-borehole','value'),
#         Output('checkbox_orientation_well','value'),
#         Output('checkbox_status_well','value'),
#         Output('checkbox_purpose_well','value'),
#         Output('checkbox_type_well','value'),
#         Input('reset_well','n_clicks')
#     )

#     def reset_filter_well(n_clicks):
#         if n_clicks is None:
#             raise PreventUpdate
#         else:
#             reset_df = all_wells[(all_wells['orient'].isin(all_wells['orient'])) & (all_wells['status'].isin(all_wells['status'])) & (all_wells['purpose'].isin(all_wells['purpose'])) & (all_wells['type'].isin(all_wells['type']))]
#             reset_well_name = pd.unique(reset_df['name'].to_list())
#             reset_orient = ['Vertical', 'Horizontal', 'Directional']
#             reset_status = ['Active', 'Inactive','Shut-in','Suspended','Abandoned']
#             reset_purpose = ['Exploration','Production','Appraisal','Injection','Monitoring','Abandonment']
#             reset_type = ['Oil','Gas','Water','Observation']
            
#             return reset_well_name, reset_orient, reset_status, reset_purpose, reset_type
        
#     return html.Div(
#         children=[
# dmc.Button('Reset', id='reset_well', variant='outline', color='dark', radius='10px', leftIcon=DashIconify(icon='material-symbols:restart-alt', width=25), 
#                                         style={'marginTop':'25px'})

#             ),
            
#         ]
#     )