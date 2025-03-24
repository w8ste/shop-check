from dash import dcc, html, Input, Output, State
import requests
import os
import base64
from datetime import datetime
import json

from app import app, config
from .sql import fetch_data
from .plotting import plot_purchases

@app.callback(
    [Output("product-input", "value"),
     Output("price-input", "value"),
     Output("response-message-purchase", "children")],
    Input("submit-button-footer-purchase", "n_clicks"),
    [State("product-input", "value"),
     State("price-input", "value")],
    prevent_initial_call=True
)
def send_purchase(n_clicks, product, price):
    if not product:
        return "", "", "Please enter a purchase."

    try:
        res = requests.post("http://127.0.0.1:8080/purchase", json={"product": product, "price": price})
        if res.status_code == 200:
            return "", "", "Purchase added successfully!"
        else:
            return "", "", f"Error: {res.text}"
    except Exception as e:
        return "", "", f"Request failed: {e}"

@app.callback(
    Output("response-message-paypal", "children"),
    Input("sync_pay_pal-btn", "n_clicks"),
)
def sync_pay_pal(n_clicks):
    try:
        res = requests.post("http://127.0.0.1:8080/sync_paypal")
        if res.status_code == 200:
            return "Synchronized successfully!"
        else:
            return "Unable to synchronize PayPal right now, try again later!"
    except Exception as e:
        return f"Request failed: {e}"


@app.callback(
    Output("purchase_table", "data"),
    Input("interval-update", "n_intervals"))
def update_purchase_table(n_intervals):
    df = fetch_data()


    return df.to_dict('records')

@app.callback(
    Output("purchase-modal", "is_open"),
    [Input("open-modal-btn-purchase", "n_clicks"),
     Input("close-modal-btn-purchase", "n_clicks")],
    prevent_initial_call=True
)
def toggle_modal_purchase(open_clicks, close_clicks):
    config.is_purchase_modal_open = not config.is_purchase_modal_open
    return config.is_purchase_modal_open

@app.callback(
    Output("budget-modal", "is_open"),
    [Input("open-modal-btn-budget", "n_clicks"),
     Input("close-modal-btn-budget", "n_clicks")],
    prevent_initial_call=True
)
def toggle_modal_budget(open_clicks, close_clicks):
    config.is_budget_modal_open = not config.is_budget_modal_open
    return config.is_budget_modal_open

@app.callback(
    Output("response-message-budget", "children"),
    Input("submit-button-footer-budget", "n_clicks"),
    State("budget-input", "value"),
    prevent_initial_call=True
)
def set_budget(n_clicks, budget):
    month_year = datetime.now().strftime("%m_%Y")
    if os.path.exists(config.budget_path):
        with open(config.budget_path, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {}
    else:
        data = {}

    data[month_year] = budget
    with open(config.budget_path, "w") as file:
        json.dump(data, file, indent=4)

    return f"{budget}$ has been set as the new budget."

@app.callback(
    Output("output-data-upload", "children"),
    Input("upload-purchase", "contents"),
    State("upload-purchase", "filename"),
    prevent_initial_call=True)
def handle_image_upload(contents, filename):
    os.makedirs("./uploads", exist_ok=True)

    if contents is not None:
        file_path = os.path.join("./uploads", filename[0])
        content_type, content_string = contents[0].split(',')
        decoded = base64.b64decode(content_string)

        if not (file_path.lower().endswith(".png")):
            return html.Div(["Error: Only PNG files are allowed."])
        try:
            with open(file_path, "wb") as f:
                f.write(decoded)

            return html.Div([f"File {filename[0]} uploaded and saved successfully!"])
        except Exception as e:
            return html.Div([f"Error saving file: {e}"])
    return html.Div(["No file uploaded."])

@app.callback(
    Output("purchase-chart", "figure"),
    Input("interval-update", "n_intervals"),
)
def update_purchase_history_chart(n_intervals):
    return plot_purchases()