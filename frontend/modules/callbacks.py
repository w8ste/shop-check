import dash
from dash import dcc, html, Input, Output, State
import requests

from .config import app

@app.callback(
    Output("response-message", "children"),
    Input("submit-button", "n_clicks"),
    State("purchase-input", "value"),
    prevent_initial_call=True
)
def send_purchase(n_clicks, purchase):
    if not purchase:
        return "Please enter a purchase."

    # Send the purchase data to the backend
    try:
        res = requests.post("http://127.0.0.1:8080/purchase", json={"item": purchase})
        if res.status_code == 200:
            return "Purchase added successfully!"
        else:
            return f"Error: {res.text}"
    except Exception as e:
        return f"Request failed: {e}"
