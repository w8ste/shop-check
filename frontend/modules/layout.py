from dash import html, dcc, dash_table

def init_layout():
    app_layout = html.Div([
        html.H1("Shop Check", style={'text-align': 'center'}),

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
            interval=5*1000,  # 5000 milliseconds = 5 seconds
            n_intervals=0
        )
    ])
    return app_layout
