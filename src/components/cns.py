# classnames for all layout
# for text
PPD_H1 = "ppd-h1"
PPD_H2 = "ppd-h2"
PPD_H5 = "ppd-h5"

########################################################################
########################################################################

# on web_layout.py

# main div for  all web
WEB_CONTAINER = "web-container"

# div navigation bar
NAVBAR = 'navbar'

# # div web maps
# MAP_ALL = 'map-all'

# div for maps container
MAP_CONTAINER = 'map-container'

# div tabs
MAIN_TABS = "main-tabs"
MAIN_TABLIST = "main-tablist"

# div tabspanel
# overview container
OVW_CONTAINER = "overview-container"
# production performance dashboard container
PPD_CONTAINER = "ppd-container"
# gng dashboard container
GNG_CONTAINER = "gng-container"
# cost analysis dashboard container
CAD_CONTAINER = "cad-container"

# # div production
# PPD_PRODUCTION_ALL = "ppd-production-all"

# div footer
FOOTER_WEB = 'footer-web'

########################################################################
########################################################################

# on web_maps components

# prev on web_layout.py
# MAP_CONTAINER = 'map-container'

# on wmaps_layout.py
MAP_WRAPPER = "map-wrapper"

# MAP_ALL_WRAPPER = 'map-all-wrapper'

# div left grid-side map
LEFT_SIDE_MAP = 'left-side-map'
# Consist of:
# Text title and summary
TITLE_SUMMARY_LAYOUT = 'title-summary-layout'
TITLE_BLOCK = 'title-block'
SUMMARY_BLOCK = 'summary-block'
# Filter map
MAP_ALL_FILTER = 'map-all-filter'

# div right grid-side map
# Consist of:
# Map Leaflet
MAP_LEAFLET = 'map-leaflet'

########################################################################
########################################################################
# on production_performance components

# prev on web_layout.py
# PPD_CONTAINER = "ppd-container"

# on production_performance_layout.py
# div main container for ppd

PPD_WRAPPER = "ppd-wrapper"

# PPD_MAIN_WRAPPER = "ppd-main-wrapper"

# div filter on left grid
# production performance filter
PPD_PRODUCTION_FILTER = "ppd-production-filter"
# production performance accordion filter
PPD_ACCORDION_FILTER = "ppd-accordion-filter"

# div main on right grid
PPD_MAIN_GRAPHS = "ppd-main-graphs"

########################################################################

# parts of filter
# on well_main_multiselect.py
PPD_MULTISELECT_WRAPPER = "ppd-multiselect-wrapper"
PPD_MULTISELECT_MULTISELECT = "ppd-multiselect-multiselect"
PPD_MULTISELECT_BUTTON = "ppd-multiselect-button"

# on from_date_picker.py
PPD_FROM_DATE_PICKER_WRAPPER = "ppd-from-date-picker-wrapper"
PPD_FROM_DATE_PICKER_DATEPICKER = "ppd-from-date-picker-datepicker"
PPD_ALL_DATE_PICKER_CHECKBOX = "ppd-all-date-picker-checkbox"

# on to_date_picker.py
PPD_TO_DATE_PICKER_WRAPPER = "ppd-to-date-picker-wrapper"
PPD_TO_DATE_PICKER_DATEPICKER = "ppd-to-date-picker-datepicker"
PPD_TO_DATE_PICKER_BUTTON = "ppd-to-date-picker-button"

########################################################################
# parts of production performance charts
# summary card on summary_card.py
PPD_SUMMARY_CARD_LEFT_GRID = "ppd-summary-card-left-grid"
PPD_SC_CARDSECTION_LEFT_GRID = "ppd-sc-cardsection-left-grid"
PPD_SC_SIMPLEGRID_LEFT_GRID = "ppd-sc-simplegrid-left-grid"
PPD_SC_GROUP_LEFT_GRID = "ppd-sc-group-left-grid"
PPD_SC_CARD_LEFT_GRID  = "ppd-sc-card-left-grid"
PPD_SC_TITLE_LEFT_GRID = "ppd-sc-title-left-grid"
PPD_SC_TEXT_LEFT_GRID  = "ppd-sc-text-left-grid"
PPD_SC_ICON_LEFT_GRID = "ppd-sc-icon-left-grid"


# on oil_rate_line_chart.py
PPD_OIL_RATE_LINE_CHART = "ppd-oil-rate-line-chart"
# (SOON) on forecasting_oil_rate_line_chart.py
# PPD_SECOND_CHART_LEFT_GRID = "ppd-second-chart-left-grid"

# on well_stats_subplots.py
PPD_WELL_STATS_SUBPLOTS = "ppd-well-stats-subplots"
# on water_injection_subplots.py
PPD_WATER_INJECTION_SUBPLOTS = "ppd-water-injection-subplots"
# on water_cut_gor_line_subplots.py
PPD_WATER_CUT_GOR_SUBPLOTS = "ppd-water-cut-gor-line-subplots"
# on oil_vs_water_subplots.py
PPD_OIL_VS_WATER_SUBPLOTS = "ppd-oil-vs-water-subplots"
# on dp_choke_size_vs_avg_dp_subplots.py
PPD_DP_CS_VS_AVG_DP_SUBPLOTS = "ppd-dp-cs-vs-avg-dp-subplots"

########################################################################
########################################################################
# on gng_analysis components

# prev on web_layout.py
# GNG_CONTAINER = "gng-container"

# on gng_layout.py
GNG_WRAPPER = "gng-wrapper"
GNG_WELL_LOG_MAIN_FILTER = "gng-well-log-main-filter"
GNG_WELL_LOG_ACCORDION_FILTER = "gng-well-log-accordion-filter"

# on well_log_graph.py
GNG_WELL_LOG_GRAPHS = "gng-well-log-graphs"