import pandas as pd
import sqlite3

conn = sqlite3.connect('data/sales.db')

df = pd.read_csv('data/superstore.csv')

df.to_sql('sales',conn, if_exists= 'replace', index= False)

print("Database created successfully!")
print(f"Total rows inserted: {len(df)}")

conn.close()