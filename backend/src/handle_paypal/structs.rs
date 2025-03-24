use serde::Deserialize;

#[derive(Debug, Deserialize)]
pub struct AccessTokenResponse {
    pub(crate) access_token: String,
}

#[derive(Debug, Deserialize)]
pub struct Transaction {
    pub transaction_id: String,
    pub status: String,
    pub transaction_amount: Amount,
}

#[derive(Debug, Deserialize)]
pub struct Amount {
    pub value: String,
    pub currency_code: String,
}

#[derive(Debug, Deserialize)]
pub struct TransactionResponse {
    pub(crate) transaction_details: Vec<TransactionDetail>,
}

#[derive(Debug, Deserialize)]
pub struct TransactionDetail {
    pub(crate) transaction_info: Transaction,
}