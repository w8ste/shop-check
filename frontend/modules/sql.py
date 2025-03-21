import sqlite3
import pandas as pd

def fetch_data():
    conn = sqlite3.connect('../backend/dbs/2025_3.db')
    query = "SELECT name, number, created_at FROM records"

    df = pd.read_sql(query, conn)
    conn.close()
    return df
