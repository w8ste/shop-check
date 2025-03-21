use chrono::{Datelike, Local};
use std::fs;
use std::io::{self};
use std::path::Path;

pub fn test_for_file() -> io::Result<String> {

    let path = get_path();

    if let Some(parent) = Path::new(&path).parent() {
        fs::create_dir_all(parent)?;
    }

    if !Path::new(&path).exists() {
        fs::File::create(&path)?;
    }

    Ok(path)
}

pub fn get_path() -> String {
    let now = Local::now();
    let month = now.month();
    let year = now.year();
    format!("./dbs/{}_{}.db", year, month)

}
