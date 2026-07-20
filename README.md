# Poetry Manager

A simple command-line app to browse poems, like your favorites, and add notes — built to learn Docker, PostgreSQL, and Kubernetes.

Poems come from [PoetryDB](https://poetrydb.org), a free public-domain poetry API.

## Tech Stack
- Python (psycopg2, requests, python-dotenv)
- PostgreSQL (Docker)
- Kubernetes (Pod + Service, tested with minikube)

## Features
- List and view poems
- Like a poem
- Add a note
- View liked poems

## Run it
```
uv add psycopg2-binary requests python-dotenv
uv run python setup_db.py
uv run python main.py

```
Needs a `.env` file with `DB_PASSWORD=yourpassword`, matching your Postgres container.

## Note

Built alongside a backend/DevOps internship, to practice Docker, PostgreSQL, and Kubernetes basics.