import sqlite3

import pandas
import pandas as pd
from datetime import datetime
import calendar


def fetch_data(config):
    try:
        conn = sqlite3.connect(f"../backend/dbs/{config.selected_db}")
        query = "SELECT name, number, created_at FROM records"

        df = pd.read_sql(query, conn)
        conn.close()

        now = datetime.now()
        num_days = calendar.monthrange(config.selected_year, config.selected_month)[1]

        df["created_at"] = df["created_at"].apply(lambda x:
                                              datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
                                              .strftime("%H:%M:%S %d.%m.%Y")
                                              )
        return df
    except:
        print("DB has not been found")
        return pandas.DataFrame()
