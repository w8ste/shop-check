import requests

from app import app

@app.server.route("/purchases")  # Proxy to Axum
def proxy_purchases():
    print("Requesting now")
    res = requests.get("http://127.0.0.1:8080/purchases")  # Backend request
    return res.content, res.status_code, res.headers.items()
