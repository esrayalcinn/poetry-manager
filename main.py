from dotenv import load_dotenv
import os
import psycopg2
from fetch_poems import fetch_new_poems

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

cur.execute("SELECT COUNT(*) FROM poems")
poem_count = cur.fetchone()[0]

if poem_count == 0:
    fetch_new_poems()

def list_poems():
    cur.execute("SELECT id, title, author FROM poems ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row[0], "-", row[1], "by", row[2])

def list_liked_poems():
    cur.execute("SELECT id, title, author FROM poems WHERE is_liked = true ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row[0], "-", row[1], "by", row[2])

def view_poem(poem_id):
    cur.execute("SELECT title, author, lines, is_liked, notes FROM poems WHERE id = %s", (poem_id,))
    row = cur.fetchone()
    if row:
        title, author, lines, is_liked, notes = row
        print(title, "by", author)
        print(lines)
        if is_liked:
            print("♥ Liked")
        else:
            print("♡ Not liked")
        print("Notes:", notes)
    else:
        print("No poem with that id.")

def like_poem(poem_id):
    cur.execute("UPDATE poems SET is_liked = true WHERE id = %s", (poem_id,))
    conn.commit()

def add_note(poem_id, note_text):
    cur.execute("UPDATE poems SET notes = %s WHERE id = %s", (note_text, poem_id))
    conn.commit()

print("Welcome to the Personalized Poetry Manager. Your preferences and actions will be recorded. Here is the list of the poems: ")
list_poems()
print("You can choose from the menu below what to do: ")
running = True
while running:
    print("\n1. List poems again")
    print("2. View a poem")
    print("3. Like a poem")
    print("4. Add a note")
    print("5. Add new poems")
    print("6. List liked poems")
    print("7. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        list_poems()
    elif choice == "2":
        try:
            poem_id = int(input("Enter poem id: "))
            view_poem(poem_id)
        except ValueError:
            print("That's not a valid number.")
    elif choice == "3":
        try:
            poem_id = int(input("Enter poem id: "))
            like_poem(poem_id)
        except ValueError:
            print("That's not a valid number.")
    elif choice == "4":
        try:
            poem_id = int(input("Enter poem id: "))
            note_text = input("Enter your note: ")
            add_note(poem_id, note_text)
        except ValueError:
            print("That's not a valid number.")
    elif choice == "5":
        fetch_new_poems()
    elif choice == "6":
        list_liked_poems()
        answer = input("View one? Enter id, or press Enter to skip: ")
        if answer != "":
            try:
                poem_id = int(answer)
                view_poem(poem_id)
            except ValueError:
                print("That's not a valid number.")
    elif choice == "7":
        running = False
    else:
        print("Invalid option, try again.") 