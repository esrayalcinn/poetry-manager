import requests
import psycopg2
from dotenv import load_dotenv
import os

def fetch_new_poems():
    response = requests.get("https://poetrydb.org/random/20")
    poems = response.json()

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

    for poem in poems:
        title = poem["title"]
        author = poem["author"]
        lines_text = "\n".join(poem["lines"])
        cur.execute("INSERT INTO poems (title, author, lines) VALUES (%s, %s, %s)", (title, author, lines_text))

    conn.commit()