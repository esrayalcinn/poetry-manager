import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
db_password = os.getenv("DB_PASSWORD")

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password=db_password,
    dbname="postgres"
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS poems (
        id SERIAL PRIMARY KEY,
        title TEXT,
        author TEXT,
        lines TEXT,
        is_liked BOOLEAN DEFAULT FALSE,
        notes TEXT
    )
""")

conn.commit()