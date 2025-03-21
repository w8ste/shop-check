use sqlx::{sqlite::SqlitePool, Pool, Row, Sqlite};
use crate::sql::utils::{test_for_file};
use std::io;

pub async fn init_sql_support() -> Result<Pool<Sqlite>, sqlx::Error> {
    let path = match test_for_file() {
        Ok(path) => path,
        Err(e) => return Err(sqlx::Error::Io(io::Error::new(io::ErrorKind::Other, e.to_string()))),
    };

    tracing::info!("SQL support: {}", path);
    let db_url = format!("sqlite://{}", path);

    let pool = SqlitePool::connect(&db_url).await?;

    Ok(pool)
}

pub async fn add_product(pool: &Pool<Sqlite>, product: &String, price: f64) -> Result<(), sqlx::Error> {

    let _ = sqlx::query(
        "CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            number REAL NOT NULL
        )"
    )
        .execute(pool)
        .await?;

    // Insert product into the table
    let result = sqlx::query("INSERT INTO records (name, number) VALUES (?1, ?2)")
        .bind(product)
        .bind(price)
        .execute(pool)
        .await;

    match result {
        Ok(_) => println!("Data inserted successfully!"),
        Err(e) => {
            println!("Error inserting data: {:?}", e);
            return Err(e);
        }
    }

    let rows = sqlx::query("SELECT name, number FROM records")
        .fetch_all(pool)
        .await?;

    for row in rows {
        let name: String = row.get("name");
        let number: f64 = match row.try_get::<f64, _>("number") {
            Ok(n) => n,
            Err(_) => row.get::<i64, _>("number") as f64,
        };

        println!("{}: {}", name, number);
    }

    Ok(())
}
