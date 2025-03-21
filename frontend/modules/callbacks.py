from dash import dcc, html, Input, Output, State
import requests
import os
import base64
from datetime import datetime

from app import app
from .sql import fetch_data


@app.callback(
    [Output("product-input", "value"),
     Output("price-input", "value"),
     Output("response-message", "children")],
    Input("submit-button-footer", "n_clicks"),
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
    Output("purchase_table", "data"),
    Input("interval-update", "n_intervals"))
def update_purchase_table(n_intervals):
    df = fetch_data()


    df["created_at"] = df["created_at"].apply(lambda x:
                                              datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
                                              .strftime("%H:%M:%S %d.%m.%Y")
                                              )
    print("update")
    return df.to_dict('records')

@app.callback(
    Output("pin-modal", "is_open"),
    [Input("open-modal-btn", "n_clicks"), Input("close-modal-btn", "n_clicks")],
    prevent_initial_call=True
)
def toggle_modal(open_clicks, close_clicks):
    print("open model")
    return open_clicks > close_clicks

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
