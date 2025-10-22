# Clears the forecast table
import sqlite3
import pandas as pd

conn = sqlite3.connect("forecast.db")
cur = conn.cursor()
cur.execute("DROP TABLE forecast")
conn.close()