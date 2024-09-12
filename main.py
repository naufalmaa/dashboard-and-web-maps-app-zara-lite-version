from dash import Dash, html, dcc, Input, Output, callback
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc

from src.components.web_layout import create_layout  # Assuming this creates your main page layout
from src.data.loader import load_well_production_data, load_all_blocks, load_all_wells, load_log_data
from src.data.source import DataSource

# File paths for data
PRODUCTION_DATA_PATH = "./data/csv/aceh_production_data_daily_rev.csv"
BLOCK_DATA_PATH = './data/geojson/all_blocks_rev.geojson'
WELL_DATA_PATH = './data/geojson/all_wells_rev.geojson'
LOG_DATA_PATH = "./data/csv/aceh_log_data_rev.csv"

# Load data
data_well = load_well_production_data(PRODUCTION_DATA_PATH)
geodata_block = load_all_blocks(BLOCK_DATA_PATH)
geodata_well = load_all_wells(WELL_DATA_PATH)
data_log = load_log_data(LOG_DATA_PATH)
data = DataSource(_data=data_well, _geodata_blocks=geodata_block, _geodata_wells=geodata_well, _data_log=data_log)

# Initialize Dash app
app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    prevent_initial_callbacks='initial_duplicate',  # Add this line
    external_stylesheets=["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css"],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ]
)

# Main app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # URL management
    html.Div(id='page-content')  # Content container to render pages dynamically
])

# Define the login layout
def create_login_layout():
    return dmc.Center(
        style={
            "position": "absolute",
            "top": "50%",
            "left": "50%",
            "transform": "translate(-50%, -50%)",
        },
        children=[
            dmc.Card(
                children=[
                    dmc.CardSection(
                        [
                            dmc.Title("Welcome to", order=4, align="center"),
                            dmc.Title("WAVIV Knowledge Navigator!", order=2, align="center"),
                            dmc.Text(
                                "login with:",
                                size="sm",
                                align="center",
                                mt="0.5rem",
                                mb="0.5rem",
                            ),
                            dmc.Group(
                                [
                                    dmc.Button(
                                        "Waviv Account",
                                        id="acc-button",
                                        leftIcon=DashIconify(icon="fluent:database-plug-connected-20-filled"),
                                        radius="xl",
                                        variant="outline",
                                        color="indigo"
                                    ),
                                ],
                                grow=True,
                                mt="1rem",
                                mb="1rem",
                            ),
                            dmc.Divider(
                                label="Or continue with email",
                                variant="dashed",
                                labelPosition="center",
                                mb="1.25rem",
                            ),
                            dmc.Stack(
                                [
                                    dmc.TextInput(label="Email:"),
                                    dmc.PasswordInput(label="Password:"),
                                ],
                                spacing="1rem",
                            ),
                            dmc.Group(
                                [
                                    html.A(
                                        "Login",
                                        href="/main",
                                        style={
                                            'display': 'inline-block',
                                            'text-align': 'center',
                                            'padding': '10px 20px',
                                            'background-color': '#4c6ef5',
                                            'color': 'white',
                                            'text-decoration': 'none',
                                            'border-radius': '5px',
                                            'font-size': '16px'
                                        }
                                    )
                                ],
                                grow=True,
                                mt="1.5rem",
                                noWrap=True,
                                spacing="apart",
                            ),
                        ],
                        inheritPadding=True,
                    )
                ],
                withBorder=True,
                shadow="xl",
                radius="lg",
                p="1.5rem",
                style={"width": "420px"},
            ),
        ],
    )

# Define a callback to control which layout is rendered based on URL
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/main':
        return create_layout(app, data)  # Render the main content page
    else:
        return create_login_layout()  # Render the login page by default

# Run the server
if __name__ == "__main__":
    app.run_server(debug=True, port=7654)
