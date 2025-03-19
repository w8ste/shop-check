mod handle_purchases;

use axum::{routing::get, Router};
use std::net::SocketAddr;
use axum::routing::post;
use tracing_subscriber;

use crate::handle_purchases::handlers::{root, get_purchases, add_purchase};
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


