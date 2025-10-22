# Read the forecast table

import sqlite3
import pandas as pd

conn = sqlite3.connect("forecast.db")
df = pd.read_sql_query("SELECT * FROM forecast", conn)
conn.close()
print(df.head(100))