use reqwest::{Client, header};
use crate::handle_paypal::structs::{Transaction, TransactionResponse, TransactionDetail, Amount, AccessTokenResponse};
use crate::handle_paypal::utils::{get_current_time, get_start_of_month};

/// Retrieves the PayPal API access token.
async fn get_access_token(client: &Client, client_id: &str, secret: &str) -> Result<String, reqwest::Error> {
    let res = client
        .post("https://api-m.sandbox.paypal.com/v1/oauth2/token")
        .basic_auth(client_id, Some(secret))
        .form(&[("grant_type", "client_credentials")])
        .send()
        .await?
        .json::<AccessTokenResponse>()
        .await?;

    Ok(res.access_token)
}

/// Retrieves PayPal transactions.
pub async fn get_transactions(
    client: &Client,
    client_id: &str,
    secret: &str,
) -> Result<Vec<Transaction>, reqwest::Error> {
    let access_token = get_access_token(client, client_id, secret).await?;
    let url = "https://api-m.sandbox.paypal.com/v1/reporting/transactions";

    let res = client
        .get(url)
        .header(header::AUTHORIZATION, format!("Bearer {}", access_token))
        .query(&[("start_date", get_start_of_month()), ("end_date", get_current_time())])
        .send()
        .await?
        .json::<TransactionResponse>()
        .await?;

    let transactions = res.transaction_details.into_iter().map(|t| t.transaction_info).collect();
    Ok(transactions)
}