# Practical 7 — Web Crawler in Plain English

> **In one sentence:** We build a small robot that visits pages of an online bookshop, copies each book's title, price and link, and saves the list.

## The problem in everyday words

A website has products spread across many pages. You want a spreadsheet of all the products without copying them by hand. A crawler automates the browsing and the copying.

## What the main idea is, without jargon

Think of a robot librarian. It opens a page, looks for the product cards, writes down the title, price and link, then looks for the "next page" button and repeats.

Two jobs are happening:

- **Crawling:** moving from page to page by following links.
- **Scraping:** pulling specific pieces of information out of each page.

The robot must also be polite: do not hammer the server, and follow the site's rules.

## What the code does, step by step

1. Start at the first page of `books.toscrape.com`.
2. Download the page HTML with `requests`.
3. Parse the HTML with BeautifulSoup.
4. Find every `article.product_pod` card.
5. Extract the title, price and link from each card.
6. Turn relative links into full URLs.
7. Find the "next" link and repeat, up to three pages.
8. Save everything to `outputs/products.csv`.

If the network is unavailable, the script prints a notice and parses a small built-in sample instead, so the parsing logic still runs.

## What the result means

The crawl collects **60 products** across three pages. The first page includes books such as *A Light in the Attic* at **£51.77**. The CSV has three columns: title, price and link.

The output is a small catalogue that could be used for price comparison, analysis, or a recommendation system.

## Why these choices?

- `requests` is simple and enough for static HTML pages.
- BeautifulSoup makes it easy to select elements with CSS selectors.
- Three pages keep the crawl polite and fast for a practical.
- A timeout prevents the program from hanging on a slow server.
- A built-in sample keeps the practical runnable offline.

## If the examiner asks (plain answers)

**What is a crawler?** A program that visits web pages and follows links.

**What is scraping?** Extracting specific data from a page.

**Why BeautifulSoup?** It turns HTML into a searchable tree.

**How does it find the next page?** It looks for the link with the "next" class.

**Why `urljoin`?** Links on a page are often relative; this makes them complete URLs.

**What is `robots.txt`?** A file that says which pages a crawler should avoid.

**Why limit the crawl?** To be polite and avoid overloading the server.

**Can it scrape any site?** No — check the terms of service, `robots.txt`, and the law.

**One-line takeaway:** A crawler fetches a page, parses it, extracts links and data, then follows the next link politely.
