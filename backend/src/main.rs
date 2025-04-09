use clap::{Arg, Command};
use axum::{routing::get, Extension, Router};
use std::net::SocketAddr;
use axum::routing::post;
use tracing_subscriber;

use crate::handle_purchases::handlers::{root, get_purchases, add_purchase, sync_paypal};
use crate::sql::create::{init_sql_support};

mod handle_purchases;
mod sql;
mod image_processing;
mod handle_paypal;

#[tokio::main]
async fn main() {

    let matches = Command::new("MyApp")
        .arg(
            Arg::new("activate_paypal")
                .short('a')
                .long("activate-paypal")
                .help("Activate PayPal integration")
        )
        .arg(
            Arg::new("client_id")
                .short('c')
                .long("client-id")
                .value_parser(clap::value_parser!(String))
                .requires("activate_paypal")
                .help("PayPal Client ID"),
        )
        .arg(
            Arg::new("secret")
                .short('s')
                .long("secret")
                .value_parser(clap::value_parser!(String))
                .requires("activate_paypal")
                .help("PayPal Secret"),
        )
        .get_matches();


    tracing_subscriber::fmt::init();

    let pool = match init_sql_support().await {
        Ok(pool) => pool,
        Err(e) => return tracing::error!("Database initialization failed: {}", e),
    };

    let app = Router::new()
        .route("/", get(root))
        .route("/sync_paypal", post(sync_paypal))
        .route("/purchase", post(add_purchase))
        .route("/purchases", post(get_purchases))
        .layer(Extension(pool));

    let addr = SocketAddr::from(([127, 0, 0, 1], 8080)); // Localhost for testing
    tracing::info!("Starting server on {}", addr);

    let listener = tokio::net::TcpListener::bind("0.0.0.0:8080").await.unwrap();

    axum::serve(listener, app).await.unwrap();
}


