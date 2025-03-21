use axum::{response::Json, Extension};
use serde_json::json;
use sqlx::{Pool, Sqlite};
use crate::handle_purchases::purchase::{Purchase, PurchaseResponse};
use crate::sql::create::add_product;
pub async fn root() -> &'static str {
    tracing::info!("Running backend root");
    "Rust Backend Running!"
}

pub async fn get_purchases() -> Json<serde_json::Value> {
    tracing::info!("Running backend get_purchases");
    Json(json!({ "purchases": [] })) // Placeholder
}

// Handle POST request to /purchase
pub async fn add_purchase(
    Extension(pool): Extension<Pool<Sqlite>>,
    Json(payload): Json<Purchase>,
) -> Json<PurchaseResponse> {
    tracing::info!("Received product: {} with price: {}$", payload.product, payload.price);

    match add_product(&pool, &payload.product, payload.price).await {
        Ok(_) => Json(PurchaseResponse {
            message: "Product saved successfully".to_string(),
        }),
        Err(e) => {
            tracing::error!("Failed to save product: {}", e);
            Json(PurchaseResponse {
                message: "Failed to save product".to_string(),
            })
        }
    }
}