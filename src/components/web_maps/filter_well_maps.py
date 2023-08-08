# from dash import Dash, html
# import dash_mantine_components as dmc
# from dash.dependencies import Input, Output
# from dash_iconify import DashIconify

# from ...data.source import DataSource
# from .. import ids, cns


# def render(app: Dash, source: DataSource) -> html.Div:

#     @app.callback(
#     Output('multiselect-borehole','value'),
#     Output('checkbox_orientation_well','value'),
#     Output('checkbox_status_well','value'),
#     Output('checkbox_purpose_well','value'),
#     Output('checkbox_type_well','value'),
#     Input('reset_well','n_clicks')
# )

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

#         return reset_well_name, reset_orient, reset_status, reset_purpose, reset_type
    
#     return html.Div(
#             children=[
#                 dmc.Accordion(
#                 value='wellhead_val',
#                 style={'marginTop':10, 'marginBottom':20},
#                 radius=10,
#                 children=[dmc.AccordionItem(
#                     [
#                         dmc.AccordionControl('Well Filter', icon=DashIconify(icon='material-symbols:pin-drop-outline',width=20)),
#                         dmc.AccordionPanel(
#                             html.Div(
#                                 className='accordion_content3',
#                                 children=[
#                             html.H5('Well Name', style={'marginTop':10}),
#                             dmc.MultiSelect(
#                                 placeholder="Select Borehole Name",
#                                 id="multiselect-borehole",
#                                 value=all_wells['name'].unique().tolist(),
#                                 data=all_wells['name'].unique().tolist(),
#                                 style={'marginTop':10},
#                                 clearable=True,
#                                 searchable=True,
#                                 nothingFound= 'No Options Found'
#                                 ),

#                             # html.H5('TVDSS in Meters', style={'marginTop':20}),
#                             # dmc.RangeSlider(
#                             #     id='range-slider-TVDSS',
#                             #     value=[500,2000],
#                             #     max=5000,
#                             #     min=0,
#                             #     marks=[
#                             #         {'value':2000, 'label':'2000m'},
#                             #         {'value':4000, 'label':'4000m'},
#                             #         ],
#                             #     style={'marginTop':10},
#                             #     color='dark'),
#                             # dmc.Text(id='output-porosity'), #output for slider porosity

#                             html.H5('Wellbore Orientation', style={'marginTop':30}),
#                             dmc.CheckboxGroup(
#                                 id='checkbox_orientation_well',
#                                 orientation='vertical',
#                                 children=[
#                                     dmc.Checkbox(label='Vertical',value='Vertical',color='dark', style={'marginTop':0}),
#                                     dmc.Checkbox(label='Horizontal',value='Horizontal',color='dark', style={'marginTop':-15}),
#                                     dmc.Checkbox(label='Directional',value='Directional',color='dark', style={'marginTop':-15})
#                                 ],
#                                 value=['Vertical','Horizontal','Directional']
#                             ),

#                             html.H5('Status', style={'marginTop':20}),
#                             dmc.CheckboxGroup(
#                                 id='checkbox_status_well',
#                                 orientation='vertical',
#                                 children=[
#                                     dmc.Checkbox(label='Active',value='Active',color='dark', style={'marginTop':0}),
#                                     dmc.Checkbox(label='Inactive',value='Inactive',color='dark', style={'marginTop':-15}),
#                                     dmc.Checkbox(label='Shut-in',value='Shut-in',color='dark', style={'marginTop':-15}),
#                                     dmc.Checkbox(label='Suspended',value='Suspended',color='dark', style={'marginTop':-15}),
#                                     dmc.Checkbox(label='Abandoned',value='Abandoned',color='dark', style={'marginTop':-15})
#                                 ],
#                                 value=['Active','Inactive','Shut-in','Suspended','Abandoned']
#                             ),

#                             html.H5('Purpose', style={'marginTop':20}),
#                             dmc.CheckboxGroup(
#                                 id='checkbox_purpose_well',
#                                 orientation='vertical',
#                                 children=[
#                                     dmc.Checkbox(label='Exploration',value='Exploration',color='dark', style={'marginTop':0}),
#                                     dmc.Checkbox(label='Production',value='Production',color='dark',style={'marginTop':-15}),
#                                     dmc.Checkbox(label='Appraisal',value='Appraisal',color='dark', style={'marginTop':-15}),
#                                     dmc.Checkbox(label='Injection',value='Injection',color='dark', style={'marginTop':-15}),
#                                     dmc.Checkbox(label='Monitoring',value='Monitoring',color='dark', style={'marginTop':-15}),
#                                     dmc.Checkbox(label='Abandonment',value='Abandonment',color='dark', style={'marginTop':-15})
#                                 ],
#                                 value=['Exploration','Production','Appraisal','Injection','Monitoring','Abandonment']
#                             ),

#                             html.H5('Type', style={'marginTop':20}),
#                             dmc.CheckboxGroup(
#                                 id='checkbox_type_well',
#                                 orientation='vertical',
#                                 children=[
#                                     dmc.Checkbox(label='Oil',value='Oil',color='dark', style={'marginTop':0}),
#                                     dmc.Checkbox(label='Gas',value='Gas',color='dark', style={'marginTop':-15}),
#                                     dmc.Checkbox(label='Water',value='Water',color='dark', style={'marginTop':-15}),
#                                     dmc.Checkbox(label='Observation',value='Observation',color='dark', style={'marginTop':-15})
#                                 ],
#                                 value=['Oil','Gas','Water','Observation']
#                             ),
#                             dmc.Button('Reset', id='reset_well', variant='outline', color='dark', radius='10px', leftIcon=DashIconify(icon='material-symbols:restart-alt', width=25), 
#                                         style={'marginTop':'25px'})

#                                 ]
#                             )
#                         )
#                     ], value='wellhead_val'
#                 )
#                 ], variant='contained'
#                 )
#             ]
#         )