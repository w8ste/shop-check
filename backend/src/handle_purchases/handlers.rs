use axum::{response::Json, extract::Json as AxumJson};
use serde_json::json;

use crate::handle_purchases::purchase::{Purchase, PurchaseResponse};

pub async fn root() -> &'static str {
    tracing::info!("Running backend root");
    "Rust Backend Running!"
}

pub async fn get_purchases() -> Json<serde_json::Value> {
    tracing::info!("Running backend get_purchases");
    Json(json!({ "purchases": [] })) // Placeholder
}

// Handle POST request to /purchase
pub async fn add_purchase(AxumJson(payload): AxumJson<Purchase>) -> Json<PurchaseResponse> {
    tracing::info!("Received purchase: {}", payload.item);
    Json(PurchaseResponse {
        message: format!("Added purchase: {}", payload.item),
    })
}
