import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.snapdeal.com/search?keyword=smartphones&page={}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_page(url):
    response = requests.get(url, headers=headers)
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

    return data

def scrape_multiple_pages(pages=3):
    all_data = []

    for page in range(1, pages + 1):
        print(f"Scraping page {page}...")
        url = BASE_URL.format(page)

        html = fetch_page(url)
        data = parse_html(html)

        all_data.extend(data)

    return all_data


if __name__ == "__main__":
    products = scrape_multiple_pages(pages=3)

    print("Total products scraped:", len(products))

    for p in products[:5]:
        print(p)