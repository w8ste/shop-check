# Tech Stack

## **Backend**
- **Language:** Rust  
- **Framework:** Axum (lightweight and async)
- **Database:** PostgreSQL (with `sqlx`)  
- **ORM:** `sea-orm` (async and feature-rich) or `diesel` (type-safe but heavier)  
- **Serialization:** `serde` (for JSON handling)  
- **API Format:** REST (Axum/Actix)  
- **Optical Character Recognition (OCR)** tesseract-rs
## **Frontend**
- **Framework:** Dash (for simplicity and Python integration)  
- **Alternative:** Svelte (lightweight) or React (more complex but flexible)  
  

## **Hosting & Security**
- **Web Server:** Nginx (reverse proxy for Rust backend)  
- **Access Control:** `iptables` or `ufw` (to restrict access to local network)  

## **Data Processing & Storage**
- **Storage:** SQLite (lightweight) or PostgreSQL (for scalability)  
- **ORM Query Optimization:** `sqlx` or `diesel` for efficient queries  
- **Logging:** `tracing` (structured logging for Rust)  

## **Build & Deployment**
- **Package Management:** Cargo  
- **Cross-compilation:** `cross` (to build Rust for Raspberry Pi)  
- **Containerization (Optional):** Docker (for easier deployment)  

## **Extras**
- **Task Scheduling:** `cron` (for periodic reports)  
- **Authentication (if needed):** `jsonwebtoken` (JWT-based auth)  
- **Configuration Management:** `dotenvy` (load environment variables)  

