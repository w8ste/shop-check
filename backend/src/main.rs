mod handle_purchases;
mod sql;

use axum::{routing::get, Extension, Router};
use std::net::SocketAddr;
use axum::routing::post;
use tracing_subscriber;

use crate::handle_purchases::handlers::{root, get_purchases, add_purchase};
use crate::sql::create::{init_sql_support};

#[tokio::main]
async fn main() {
    tracing_subscriber::fmt::init();

    let pool = match init_sql_support().await {
        Ok(pool) => pool,
        Err(e) => return tracing::error!("Database initialization failed: {}", e),
    };

    let app = Router::new()
        .route("/", get(root))
        .route("/purchases", get(get_purchases))
        .route("/purchase", post(add_purchase))
        .layer(Extension(pool));

    let addr = SocketAddr::from(([127, 0, 0, 1], 8080)); // Localhost for testing
    tracing::info!("Starting server on {}", addr);

    let listener = tokio::net::TcpListener::bind("0.0.0.0:8080").await.unwrap();

    axum::serve(listener, app).await.unwrap();


}


