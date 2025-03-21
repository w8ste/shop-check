from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc


def init_layout():
    pin_modal = dbc.Modal(
        [
            dbc.ModalHeader(
                html.H2("Access Control Panel", style={"text-align": "center"})
            ),
            dbc.ModalBody(
                [
                    html.P(
                        id="modal-message",
                        children="Enter your PIN to switch roles.",
                        style={"text-align": "center", "margin-bottom": "15px"}
                    ),
                    dcc.Input(
                        id="pin-input",
                        type="password",
                        placeholder="Enter PIN",
                        maxLength=4,
                        pattern="[0-9]*",
                        className="pin-input"
                    ),
                    html.P(
                        id="error-message",
                        children="Invalid PIN. Please try again.",
                        style={"color": "red", "display": "none", "font-size": "14px", "text-align": "center"},
                    ),
                ]
            ),
            dbc.ModalFooter(
                [
                    dbc.Button("Submit", id="submit-button-footer", className="btn-primary", n_clicks=0),
                    dbc.Button("Close", id="close-modal-btn", n_clicks=0, color="secondary"),
                ]
            ),
        ],
        id="pin-modal",
        is_open=False,
        className="custom-modal"
    )

    app_layout = html.Div([

        html.H1("Shop Check", style={'text-align': 'center'}),

        dbc.Button("Open Form", id="open-modal-btn", n_clicks=0),
        html.Div([pin_modal]),
        dcc.Input(id="product-input", type="text", placeholder="Enter purchase"),
        dcc.Input(id="price-input", type="number", placeholder="price"),
        html.Button("Submit", id="submit-button", n_clicks=0),
        html.Div(id="response-message"),
        dash_table.DataTable(
            id='purchase_table',
            columns=[
                {"name": "Product Name", "id": "name"},
                {"name": "Price", "id": "number"},
                {"name": "Timestamp", "id": "created_at"},
            ],
            data=[],
            style_table={'height': '400px', 'overflowY': 'auto'},
            style_cell={'padding': '10px', 'textAlign': 'center'},
            style_header={'backgroundColor': '#f1f1f1', 'fontWeight': 'bold'},
            style_data={'whiteSpace': 'normal', 'height': 'auto'},
        ),

        dcc.Interval(
            id="interval-update",
            interval=1.5*1000,  # 1500 milliseconds = 1.5 seconds
            n_intervals=0
        )
    ])
    return app_layout
