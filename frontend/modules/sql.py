import sqlite3
import pandas as pd
from datetime import datetime

def fetch_data():
    conn = sqlite3.connect('../backend/dbs/2025_3.db')
    query = "SELECT name, number, created_at FROM records"

    df = pd.read_sql(query, conn)
    conn.close()
    df["created_at"] = df["created_at"].apply(lambda x:
                                              datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
                                              .strftime("%H:%M:%S %d.%m.%Y")
                                              )
    return df
