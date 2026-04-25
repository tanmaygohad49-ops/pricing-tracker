import requests
from bs4 import BeautifulSoup

URL = "https://www.snapdeal.com/search?keyword=smartphones"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_page(url):
    response = requests.get(url, headers=headers)
    print("Status Code:", response.status_code)
    print("HTML Length:", len(response.text))
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")

    products = soup.find_all("div", {"class": "product-tuple-listing"})

    data = []

    for item in products:
        name = item.find("p", {"class": "product-title"})
        price = item.find("span", {"class": "product-price"})
        rating = item.find("div", {"class": "filled-stars"})

        if name and price:
            product = {
                "name": name.text.strip(),
                "price": price.text.strip(),
                "rating": rating["style"] if rating else None
            }
            data.append(product)

    print("Total products found:", len(products))
    print("Parsed products:", len(data))

    return data

if __name__ == "__main__":
    html = fetch_page(URL)
    products = parse_html(html)

    for p in products[:5]:
        print(p)