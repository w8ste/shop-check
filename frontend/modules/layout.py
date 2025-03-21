import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Output, Input, State, ctx, dash_table

def init_layout():
    app_layout = html.Div([
        html.H1("Shop Check"),

        dcc.Input(id="product-input", type="text", placeholder="Enter purchase"),
        dcc.Input(id="price-input", type="number", placeholder="price"),
        html.Button("Submit", id="submit-button", n_clicks=0),

        # Display response from backend
        html.Div(id="response-message"),
    ])
    return app_layout
