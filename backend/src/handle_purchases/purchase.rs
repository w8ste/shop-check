use serde::{Deserialize, Serialize};

#[derive(Deserialize)]
pub struct Purchase {
    pub(crate) item: String,
}

#[derive(Serialize)]
pub struct PurchaseResponse {
    pub(crate) message: String,
}
