use sqlx::{sqlite::SqlitePool, Error, Pool, Row, Sqlite};
use crate::sql::utils::{test_for_file};
use std::io;
use std::io::ErrorKind;
use chrono::{DateTime, Local, NaiveDateTime, ParseResult, Utc};

pub async fn init_sql_support() -> Result<Pool<Sqlite>, sqlx::Error> {
    let path = match test_for_file() {
        Ok(path) => path,
        Err(e) => return Err(sqlx::Error::Io(io::Error::new(io::ErrorKind::Other, e.to_string()))),
    };

    tracing::info!("SQL support: {}", path);
    let db_url = format!("sqlite://{}", path);

    let pool = SqlitePool::connect(&db_url).await?;


    let _ = sqlx::query(
        "CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            number REAL NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )"
    )
        .execute(&pool)
        .await?;

    Ok(pool)
}

pub async fn add_product(pool: &Pool<Sqlite>, product: &String, price: f64) -> Result<(), sqlx::Error> {

    let created_at = Local::now().naive_local();
    let created_at_str = created_at.format("%Y-%m-%d %H:%M:%S").to_string();


    let result = sqlx::query("INSERT INTO records (name, number, created_at) VALUES (?1, ?2, ?3)")
        .bind(product)
        .bind(price)
        .bind(created_at_str)
        .execute(pool)
        .await;

    match result {
        Ok(_) => println!("Data inserted successfully!"),
        Err(e) => {
            println!("Error inserting data: {:?}", e);
            return Err(e);
        }
    }

    let rows = sqlx::query("SELECT name, number, created_at FROM records")
        .fetch_all(pool)
        .await?;

    for row in rows {
        let name: String = row.get("name");
        let number: f64 = match row.try_get::<f64, _>("number") {
            Ok(n) => n,
            Err(_) => row.get::<i64, _>("number") as f64,
        };
        let created_at: String = row.get("created_at");  // The timestamp as a string
        tracing::info!(created_at);

        let created_at = match NaiveDateTime::parse_from_str(&created_at, "%Y-%m-%d %H:%M:%S") {
            Ok(created_at) => created_at,
            Err(e) => {
                return Err(Error::Decode(format!("Failed to parse timestamp: {}", e).into()));
            }
        };
        let formatted_created_at = created_at.format("%H:%M:%S %d-%m-%Y").to_string();

        println!("{}: {} at {}", name, number, formatted_created_at);
    }

    Ok(())
}
