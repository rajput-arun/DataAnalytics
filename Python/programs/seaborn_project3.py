import sqlite3
import pandas as pd
import seaborn as sns

conn = sqlite3.connect("G:/My Drive/Data Analyst/Python/data/db.sqlite3")
cursor = conn.cursor()

cursor.execute("PRAGMA database_list;")
print(cursor.fetchall())

