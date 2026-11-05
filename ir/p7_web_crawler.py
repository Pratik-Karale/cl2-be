"""Practical 7 - Web crawler for product information.

Aim
    Crawl product cards from a practice e-commerce site and save title,
    price and link for each product to a CSV file.

Default source
    https://books.toscrape.com/catalogue/page-1.html (a site made for scraping).

Output
    outputs/products.csv

If the network is unavailable, the script parses a small built-in sample so
the practical still demonstrates the same BeautifulSoup logic.
"""

import sys
from pathlib import Path
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup

OUT = Path(__file__).resolve().parents[1] / "outputs"
OUT.mkdir(exist_ok=True)

DEFAULT_URL = "https://books.toscrape.com/catalogue/page-1.html"

SAMPLE_HTML = """
<html><body>
  <article class="product_pod">
    <h3><a title="Sample Book One" href="one.html">One</a></h3>
    <p class="price_color">GBP 10.00</p>
  </article>
  <article class="product_pod">
    <h3><a title="Sample Book Two" href="two.html">Two</a></h3>
    <p class="price_color">GBP 20.00</p>
  </article>
  <article class="product_pod">
    <h3><a title="Sample Book Three" href="three.html">Three</a></h3>
    <p class="price_color">GBP 30.00</p>
  </article>
</body></html>
"""


def parse_page(html: str, base_url: str) -> tuple[list[dict], str | None]:
    soup = BeautifulSoup(html, "html.parser")
    products = []
    for item in soup.select("article.product_pod"):
        link = item.h3.a
        products.append(
            {
                "title": link["title"],
                "price": item.select_one(".price_color").text,
                "link": urljoin(base_url, link["href"]),
            }
        )
    next_link = soup.select_one("li.next a")
    next_url = urljoin(base_url, next_link["href"]) if next_link else None
    return products, next_url


def main() -> None:
    url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
    products: list[dict] = []

    try:
        for _ in range(3):
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            page_products, next_url = parse_page(response.text, url)
            products.extend(page_products)
            if not next_url:
                break
            url = next_url
    except Exception as exc:
        print(f"Network unavailable ({exc}); using the built-in sample instead.")
        products, _ = parse_page(SAMPLE_HTML, "https://example.com/")

    df = pd.DataFrame(products)
    destination = OUT / "products.csv"
    df.to_csv(destination, index=False)
    print(df.head().to_string(index=False))
    print(f"\nTotal products: {len(df)}  (saved to {destination})")


if __name__ == "__main__":
    main()
