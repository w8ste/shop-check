use serde::{Deserialize, Serialize};

#[derive(Deserialize)]
pub struct Purchase {
    pub(crate) product: String,
    pub(crate) price: f64,
}

#[derive(Serialize)]
pub struct PurchaseResponse {
    pub(crate) message: String,
}
