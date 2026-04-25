import json
import re

RAW_FILE = "data/raw/products.json"
CLEAN_FILE = "data/cleaned/products_cleaned.json"


def clean_price(price):
    if price:
        # Extract only digits
        digits = re.findall(r"\d+", price)
        
        if digits:
            return int("".join(digits))  # combine all numbers
        
    return None


def clean_rating(rating):
    if rating:
        match = re.search(r"(\d+)", rating)
        if match:
            value = int(match.group(1))
            return round((value / 100) * 5, 1)  # convert % to 5-star scale
    return None


def clean_data():
    with open(RAW_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    cleaned = []

    for item in data:
        cleaned_item = {
            "name": item.get("name"),
            "price": clean_price(item.get("price")),
            "rating": clean_rating(item.get("rating"))
        }
        cleaned.append(cleaned_item)

    return cleaned


def save_clean_data(data):
    import os
    os.makedirs("data/cleaned", exist_ok=True)

    with open(CLEAN_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    cleaned_data = clean_data()
    save_clean_data(cleaned_data)

    print("Cleaned data saved!")