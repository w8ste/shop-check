from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc


def init_layout():
    pin_modal = dbc.Modal(
        [
            dbc.ModalHeader(
                html.H2("Add Purchase", style={"text-align": "center"})
            ),
            dbc.ModalBody(
                [
                    dcc.Input(id="product-input", type="text", placeholder="Enter purchase"),
                    dcc.Input(id="price-input", type="number", placeholder="price"),
                    html.Div(id="response-message",
                             style={"color": "red", "display": "none", "font-size": "14px", "text-align": "center"}),
                    html.Div([
                        html.H5("or", style={"text-align": "center"}),
                        dcc.Upload(
                            id="upload-purchase",
                            multiple=True,
                            children=html.Div(["Drag and drop or click to select files"]),
                            style={
                                'width': '100%',
                                'height': '100px',
                                'lineHeight': '100px',
                                'borderWidth': '1px',
                                'borderStyle': 'dashed',
                                'borderRadius': '5px',
                                'textAlign': 'center',
                                'backgroundColor': '#f1f1f1',
                                'cursor': 'pointer'
                            },
                            accept="image/png",
                        ),
                        html.Div(id="output-data-upload"),
                    ])
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

        dbc.Button("Add purchase +", id="open-modal-btn", n_clicks=0),

        html.Div([pin_modal]),

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
