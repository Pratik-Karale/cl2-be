# Practical 7 — Web Crawler for Product Information (Viva Theory)

> **30-second answer:** Crawl the first **3 pages** of `books.toscrape.com` with `requests` + **BeautifulSoup**, extract each product's **title, price and link**, follow the "next" button, and save **60 products** to `outputs/products.csv`. If the network is unavailable, a built-in sample demonstrates the same parsing logic.

## 1. MOST LIKELY — Core of the Experiment (High Yield)

**Aim:** Build a small web crawler that pulls product information and links from an e-commerce site.

**Source:** `https://books.toscrape.com/catalogue/page-1.html` — a site designed for scraping practice.

**Pipeline in 6 bullets**
- Start from the given URL (or a command-line URL).
- Fetch the page with `requests.get(url, timeout=10)`.
- Parse the HTML with `BeautifulSoup(..., "html.parser")`.
- Select every `article.product_pod` card and extract the title, price and link.
- Convert relative links to absolute links with `urljoin`.
- Find `li.next a`; if present, follow it and repeat for up to 3 pages.

**Code skeleton**
```python
soup = BeautifulSoup(response.text, "html.parser")
for item in soup.select("article.product_pod"):
    a = item.h3.a
    products.append({"title": a["title"],
                     "price": item.select_one(".price_color").text,
                     "link": urljoin(url, a["href"])})
```

**Expected output**
- The first page shows books such as *A Light in the Attic* at **£51.77**.
- **Total products: 60** across 3 pages.
- CSV saved to `outputs/products.csv` with columns `title`, `price`, `link`.
- If the network fails, the script prints a notice and parses a 3-product built-in sample.

**Viva Q&A**
1. **What is a web crawler?** A program that downloads web pages and follows links to collect data.
2. **What is the difference between crawling and scraping?** Crawling discovers and navigates pages; scraping extracts specific data from them.
3. **Why `requests`?** It sends the HTTP GET request and returns the page HTML.
4. **Why BeautifulSoup?** It parses HTML into a tree that is easy to search with CSS selectors.
5. **What does `select("article.product_pod")` do?** Finds every product card element.
6. **Why `urljoin`?** Product links are relative; it turns them into full URLs.
7. **How does the crawler find the next page?** It looks for the `li.next a` link and follows its `href`.
8. **Why limit to 3 pages?** Politeness and to keep the practical fast.
9. **What is `timeout=10`?** It stops the request from hanging forever on a slow server.
10. **What happens if the site changes its HTML?** The CSS selectors may stop matching, so the crawler needs updating.
11. **Is this legal/ethical?** Respect `robots.txt`, terms of service, rate limits, and do not overload the server.
12. **What would you change for a real crawl?** Add politeness delays, deduplication, a frontier queue, and storage.

## 2. LIKELY — Syllabus Theory Around This Practical

### Unit V: Web Retrieval and Web Crawling
- **Web crawler structure:** URL frontier, fetcher, parser, link extractor, deduplication.
- **Crawling strategies:** breadth-first, depth-first, focused crawling.
- **Politeness:** delay between requests and respect for `robots.txt`.
- **Parsing libraries:** BeautifulSoup, lxml, Scrapy.
- **Search engine architecture:** crawler → indexer → query processor → ranker.

**Likely Q&A**
- *What is a URL frontier?* The queue of pages waiting to be crawled.
- *What is deduplication?* Avoiding crawling the same URL twice.
- *What is a canonical URL?* The standard form of a URL after removing duplicates and tracking parameters.
- *What is `robots.txt`?* A file that tells crawlers which paths they may not access.
- *What is a focused crawler?* A crawler that prioritises pages relevant to a topic.
- *What is the difference between static and dynamic pages?* Dynamic pages need JavaScript or API calls; `requests` alone may not see the content.
- *What is rate limiting?* Limiting request frequency to avoid overloading a server.
- *What is a sitemap?* A file listing URLs to help crawlers discover pages.

## 3. LEAST LIKELY — Stretch / Edge Cases

- **JavaScript-rendered pages:** use Playwright or Selenium when the HTML is built by JavaScript.
- **Anti-bot protection:** CAPTCHAs and blocks; always follow the site's terms.
- **Infinite crawling:** without limits or deduplication, a crawler can run forever.
- **Changing HTML:** selectors break; use robust attributes and tests.
- **Large-scale crawling:** distributed crawlers, queues, and storage are needed.
- **Legal issues:** copyright, privacy, and terms of service.
- **Trap question:** "Can you scrape any website?" No — check permissions, `robots.txt`, and the law.

**If you remember only one thing:** A crawler fetches a page, parses it, extracts links and data, then follows the next link — politely, with a limit and deduplication.
