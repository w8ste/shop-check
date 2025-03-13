use axum::{routing::get, Router, response::Json, extract::Json as AxumJson};
use std::net::SocketAddr;
use axum::routing::post;
use serde::{Deserialize, Serialize};
use serde_json::json;
use tracing_subscriber;

#[tokio::main]
async fn main() {
    tracing_subscriber::fmt::init();

    let app = Router::new()
        .route("/", get(root))
        .route("/purchases", get(get_purchases))
        .route("/purchase", post(add_purchase));

    let addr = SocketAddr::from(([127, 0, 0, 1], 8080)); // Localhost for testing
    tracing::info!("Starting server on {}", addr);

    let listener = tokio::net::TcpListener::bind("0.0.0.0:8080").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}

async fn root() -> &'static str {
    tracing::info!("Running backend root");
    "Rust Backend Running!"
}

async fn get_purchases() -> Json<serde_json::Value> {
    tracing::info!("Running backend get_purchases");
    Json(json!({ "purchases": [] })) // Placeholder
}

#[derive(Deserialize)]
struct Purchase {
    item: String,
}

#[derive(Serialize)]
struct PurchaseResponse {
    message: String,
}

// Handle POST request to /purchase
async fn add_purchase(AxumJson(payload): AxumJson<Purchase>) -> Json<PurchaseResponse> {
    tracing::info!("Received purchase: {}", payload.item);
    Json(PurchaseResponse {
        message: format!("Added purchase: {}", payload.item),
    })
}