import dash
from dash import dcc, html, Input, Output, State
import requests

from modules.layout import init_layout
app = dash.Dash(__name__)
app.title = 'Shop-Check'
def fetch_purchases():
    try:
        res = requests.get("http://127.0.0.1:8050/api/purchases")  # Proxy through Dash
        return res.json().get("purchases", [])
    except:
        return []


@app.server.route("/purchases")  # Proxy to Axum
def proxy_purchases():
    print("Requesting now")
    res = requests.get("http://127.0.0.1:8080/purchases")  # Backend request
    return res.content, res.status_code, res.headers.items()

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



def main():
    app.layout = init_layout()
    app.run_server(host='127.0.0.1', port=8050, debug=True)

if __name__ == '__main__':
    main()