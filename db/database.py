import sqlite3
import json

DB_NAME = "data/products.db"
CLEAN_FILE = "data/cleaned/products_cleaned.json"


def create_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn


def create_table(conn):
    query = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price INTEGER,
        rating REAL
    )
    """
    conn.execute(query)
    conn.commit()


def load_clean_data():
    with open(CLEAN_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def insert_data(conn, data):
    query = """
    INSERT INTO products (name, price, rating)
    VALUES (?, ?, ?)
    """

    for item in data:
        conn.execute(query, (
            item.get("name"),
            item.get("price"),
            item.get("rating")
        ))

    conn.commit()


def main():
    conn = create_connection()
    create_table(conn)

    data = load_clean_data()
    insert_data(conn, data)

    print("Data inserted into database!")

    conn.close()


if __name__ == "__main__":
    main()