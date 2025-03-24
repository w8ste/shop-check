use chrono::{Datelike, Timelike, Utc};

/// Compute the first day of the current month at midnight (UTC)
pub fn get_start_of_month() -> String {
    let now = Utc::now();
    format!("{}-{:02}-01T00:00:00Z", now.year(), now.month())
}

/// Get the current date and time in UTC
pub fn get_current_time() -> String {
    let now = Utc::now();
    format!(
        "{}-{:02}-{:02}T{:02}:{:02}:{:02}Z",
        now.year(),
        now.month(),
        now.day(),
        now.hour(),
        now.minute(),
        now.second()
    )
}