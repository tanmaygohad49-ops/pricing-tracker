from fastapi import FastAPI
import sqlite3

app = FastAPI()

DB_NAME = "data/products.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


@app.get("/")
def home():
    return {"message": "Pricing Tracker API is running"}


@app.get("/products")
def get_products():
    conn = get_connection()
    cursor = conn.execute("SELECT name, price, rating FROM products LIMIT 50")

    data = []
    for row in cursor:
        data.append({
            "name": row[0],
            "price": row[1],
            "rating": row[2]
        })

    conn.close()
    return data


@app.get("/products/cheap")
def get_cheap_products(max_price: int = 10000):
    conn = get_connection()
    cursor = conn.execute(
        "SELECT name, price, rating FROM products WHERE price <= ?",
        (max_price,)
    )

    data = []
    for row in cursor:
        data.append({
            "name": row[0],
            "price": row[1],
            "rating": row[2]
        })

    conn.close()
    return data