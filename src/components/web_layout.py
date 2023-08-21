from dash import Dash, html
import dash_mantine_components as dmc
from dash_iconify import DashIconify

from src.components import ids, cns

from ..data.source import DataSource

from .web_maps import (
    wmaps_layout
    # filter_maps,
    # restart_button,
    # leaflet_maps,
    # filter_well_maps,
    # restart_well_button,
)

from .production_performance import (
    production_performance_layout,
    # summary_card,
    # oil_rate_line_chart,
    # # forecasting_oil_rate_line_chart,
    # well_stats_subplots,
    # water_injection_subplots,
    # water_cut_gor_line_subplots,
    # oil_vs_water_subplots,
    # # dp_choke_size_vs_avg_dp_subplots,
    # well_main_multiselect,
    # from_date_datepicker,
    # to_date_datepicker
)

from .gng_analysis import (
    gng_layout,
    # well_log_filter,
    # well_log_graph,
    
)

from .web_maps.data_color_map import colormap


def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        className=cns.WEB_CONTAINER,
        children=[
            # div navbar (header(1))
            html.Div(className=cns.NAVBAR, children=[html.H1("Navigation Bar")]),
            
            # div for webmaps
            html.Div(
                className=cns.MAP_CONTAINER,
                children=[
                    wmaps_layout.create_layout_map(app, source)
                ]
            ),

            # # div left-side map (content(2)) map filter
            # html.Div(
            #     className=cns.LEFT_SIDE_MAP,
            #     children=[
            #         html.Div(
            #             className=cns.TITLE_SUMMARY_LAYOUT,
            #             children=[
            #                 html.H1("Dummy Block", className=cns.TITLE_BLOCK),
            #                 html.H4("Summary"),
            #                 dmc.Spoiler(
            #                     className=cns.SUMMARY_BLOCK,
            #                     showLabel="Show More",
            #                     hideLabel="Hide",
            #                     maxHeight=50,
            #                     style={"marginBottom": 35},
            #                     children=[
            #                         dmc.Text(
            #                             """
            #                             Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi luctus elit at eros accumsan iaculis. Nulla facilisi. Morbi vitae venenatis ante. Nulla dui tellus, euismod at malesuada ac, luctus quis orci. Nullam in eros mollis, vulputate neque ut, vulputate dolor. In sed ultrices mauris. Ut vitae dolor augue. Ut ac purus eu felis scelerisque facilisis. Donec consectetur odio orci, non volutpat eros suscipit vestibulum. Quisque a fermentum massa. Sed ac nibh nibh.
            #                             """
            #                         )
            #                     ],
            #                 ),
            #             ],
            #         ),
            #         html.Div(
            #             className=cns.MAP_ALL_FILTER,
            #             children=[
            #                 # MAP COLOR FILTER
            #                 dmc.Accordion(
            #                     value="color map filter",
            #                     radius=10,
            #                     variant="contained",
            #                     style={"marginBottom": 10},
            #                     children=[
            #                         dmc.AccordionItem(
            #                             [
            #                                 dmc.AccordionControl(
            #                                     "Map Settings",
            #                                     icon=DashIconify(
            #                                         icon="ic:twotone-map", width=25
            #                                     ),
            #                                 ),
            #                                 dmc.AccordionPanel(
            #                                     html.Div(
            #                                         children=[
            #                                             # MAP COLOR FILTER
            #                                             html.H5("Layout Map"),
            #                                             dmc.RadioGroup(
            #                                                 [
            #                                                     dmc.Radio(
            #                                                         i, value=k, color=c
            #                                                     )
            #                                                     for i, k, c in colormap()
            #                                                 ],
            #                                                 id=ids.MAP_COLOR,
            #                                                 value="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
            #                                                 orientation="vertical",
            #                                                 spacing="xs",
            #                                             ),
            #                                         ]
            #                                     )
            #                                 ),
            #                             ],
            #                             value="color map filter",
            #                         )
            #                     ],
            #                 ),
            #                 # BLOCK FILTER
            #                 dmc.Accordion(
            #                     value="block filter",
            #                     radius=10,
            #                     variant="contained",
            #                     style={"marginBottom": 10},
            #                     children=[
            #                         dmc.AccordionItem(
            #                             [
            #                                 dmc.AccordionControl(
            #                                     "Block Filter",
            #                                     icon=DashIconify(
            #                                         icon="mdi:surface-area", width=20
            #                                     ),
            #                                 ),
            #                                 dmc.AccordionPanel(
            #                                     html.Div(
            #                                         children=[
            #                                             filter_maps.render(app, source),
            #                                             restart_button.render(app, source),
            #                                         ]
            #                                     )
            #                                 ),
            #                             ],
            #                             value="block filter",
            #                         )
            #                     ],
            #                 ),
            #                 # WELL FILTER
            #                 dmc.Accordion(
            #                     value="well filter",
            #                     radius=10,
            #                     variant="contained",
            #                     children=[
            #                         dmc.AccordionItem(
            #                             [
            #                                 dmc.AccordionControl(
            #                                     "Well Filter",
            #                                     icon=DashIconify(
            #                                         icon="material-symbols:pin-drop-outline",
            #                                         width=20,
            #                                     ),
            #                                 ),
            #                                 dmc.AccordionPanel(
            #                                     html.Div(
            #                                         children=[
            #                                             filter_well_maps.render(
            #                                                 app, source
            #                                             ),
            #                                             restart_well_button.render(
            #                                                 app, source
            #                                             ),
            #                                         ]
            #                                     )
            #                                 ),
            #                             ],
            #                             value="well filter",
            #                         )
            #                     ],
            #                 ),
            #             ],
            #         ),
            #     ],
            # ),
            # # div map-map (content(3))
            # html.Div(
            #     className=cns.MAP_LEAFLET, children=[leaflet_maps.render(app, source)]
            # ),
            
            # div for tab and tab list after map
            dmc.Tabs(
                [
                    dmc.TabsList(
                        [
                            dmc.Tab("Overview", value="1"),
                            dmc.Tab("Production Performance Analysis", value="2"),
                            dmc.Tab("Geology & Geophysics Analysis", value="3"),
                            dmc.Tab("Cost Analysis", value="4"),
                        ],
                        className=cns.PPD_TABLIST,
                    ),
                    # overview (chatbot, preview data, about data)
                    dmc.TabsPanel("AAAAAAAA", value="1", className=cns.PPD_TABSPANEL),
                    
                    # tabs for production performance analysis
                    dmc.TabsPanel(production_performance_layout.create_layout(app, source), value="2", className=cns.PPD_CONTAINER),
                    
                    # tabs for gng analysis
                    dmc.TabsPanel(gng_layout.create_layout(app, source), value="3", className=cns.GNG_CONTAINER),
                    
                    # tabs for cost analysis
                    dmc.TabsPanel("DD", value="4", className=cns.PPD_TABSPANEL),
                ],
                value="2",
                variant="outline",
                className=cns.PPD_TABS,
            ),
            # # div ppd-production filter (content{4})
            # html.Div(
            #     className=cns.PPD_PRODUCTION_FILTER,
            #     children=[
            #         dmc.Accordion(
            #             value="production filter",
            #             radius=10,
            #             variant="contained",
            #             className=cns.PPD_ACCORDION_FILTER,
            #             children=[
            #                 dmc.AccordionItem(
            #                     [
            #                         dmc.AccordionControl(
            #                             "Well Production Filter",
            #                             icon=DashIconify(
            #                                 icon="octicon:graph-16", width=25
            #                             ),
            #                         ),
            #                         dmc.AccordionPanel(
            #                             html.Div(
            #                                 children=[
            #                                     well_main_multiselect.render(
            #                                         app, source
            #                                     ),
            #                                     from_date_datepicker.render(
            #                                         app, source
            #                                     ),
            #                                     to_date_datepicker.render(app, source),
            #                                 ]
            #                             )
            #                         ),
            #                     ],
            #                     value="production filter",
            #                 )
            #             ],
            #         )
            #     ],
            # ),
            # # div ppd-main-graph (content(5))
            # html.Div(
            #     className=cns.PPD_MAIN_GRAPHS,
            #     children=[
            #         summary_card.render(app, source),
            #         oil_rate_line_chart.render(app, source),
            #         well_stats_subplots.render(app, source),
            #         water_injection_subplots.render(app, source),
            #         water_cut_gor_line_subplots.render(app, source),
            #         oil_vs_water_subplots.render(app, source),
            #     ],
            # ),
            
            # 040823 - adding div wl-filter and wl-main-graph
            # # div wl-main-filter
            # html.Div(
            #     className=cns.WL_MAIN_FILTER,
            #     children=[
            #         dmc.Accordion(
            #             value="well-log filter",
            #             radius=10,
            #             variant="contained",
            #             className=cns.WL_ACCORDION_FILTER,
            #             children=[
            #                 dmc.AccordionItem(
            #                     [
            #                         dmc.AccordionControl(
            #                             "Well-Log Filter",
            #                             icon=DashIconify(
            #                                 icon="octicon:graph-16", width=25
            #                             ),
            #                         ),
            #                         dmc.AccordionPanel(
            #                             html.Div(
            #                                 children=well_log_filter.render(app, source)
            #                             )
            #                         ),
            #                     ],
            #                     value="well-log filter",
            #                 )
            #             ],
            #         )
            #     ],
            # ),
            # # div wl-main-graph
            # html.Div(
            #     className=cns.WL_MAIN_GRAPHS,
            #     children=[
            #         html.H1("Well-Log"),
            #         # well_log_filter.render(app, source),
            #         well_log_graph.render(app, source),
            #     ],
            # ),
            
            # Div Footer (Footer(6))
            html.Div(
                className=cns.FOOTER_WEB,
                children=[
                    html.H1("Footer"),
                ],
            ),
        ],
    )