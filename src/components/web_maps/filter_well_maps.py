# from dash import Dash, html
# import dash_mantine_components as dmc
# from dash.dependencies import Input, Output
# from dash_iconify import DashIconify
# import pandas as pd

# from ...data.source import DataSource
# from .. import ids, cns


# def render(app: Dash, source: DataSource) -> html.Div:

#     @app.callback(
#     Output('multiselect-borehole','data'),
#     Input('checkbox_orientation_well','value'),
#     Input('checkbox_status_well','value'),
#     Input('checkbox_purpose_well','value'),
#     Input('checkbox_type_well','value')
#     )

#     def set_well_option(chosen_orientation, chosen_status, chosen_purpose, chosen_type):
#         df_well = all_wells[(all_wells['orient'].isin(chosen_orientation)) & (all_wells['status'].isin(chosen_status)) & (all_wells['purpose'].isin(chosen_purpose)) & (all_wells['type'].isin(chosen_type))]
#         return pd.unique(df_well['name'].to_list())
    
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
                            
#                                 ]
#                             )
#                         )
#                     ], value='wellhead_val'
#                 )
#                 ], variant='contained'
#                 )
#             ]
#         )