# Practical 2 — Inverted Index in Plain English

> **In one sentence:** We build a lookup table that says which documents contain each word, then use it to answer queries quickly.

## The problem in everyday words

Imagine six short documents. A user searches for "web pages". You need to find every document that contains both words. Reading all six documents for every query works, but it is slow. We want a shortcut.

## What the main idea is, without jargon

Think of the index at the back of a textbook. Instead of reading the whole book to find a topic, you look up the topic and see the page numbers.

An **inverted index** is that index for documents:

- Each word is a topic.
- The "page numbers" are the names of the documents that contain that word.

To answer an **AND** query, look up each word and take the overlap: a document must appear in every word's list.

## What the code does, step by step

1. Read all six text files from `data/docs/`.
2. Lowercase each document and split it into words.
3. For every word, add the document name to that word's set.
4. For a query, split it into words the same way.
5. Look up each query word's set.
6. Keep only the document names that appear in all sets (the intersection).
7. Print the matching documents.

## What the result means

- "documents" matches **doc1, doc2 and doc4**.
- "web pages" matches **doc4 and doc5**, because both documents mention both words.
- "spam filters" matches **doc6**.

If a word is missing from the index, its set is empty, so the query returns nothing. That is correct for an AND query.

## Why these choices?

- A set removes duplicate entries and makes intersection fast.
- Tokenizing the query the same way as the documents keeps the terms consistent.
- AND semantics are simple and easy to demonstrate.
- The index is built once and reused for many queries.

## If the examiner asks (plain answers)

**What is an inverted index?** A table from each word to the documents that contain it.

**Why "inverted"?** A normal index goes document → words; this one goes word → documents.

**What does AND mean?** The document must contain every query word.

**What would OR mean?** The document may contain any of the query words; we would take the union instead of the intersection.

**What is a postings list?** The list of documents attached to one word.

**Why not just scan every document?** Scanning is slow for large collections; the index makes lookup much faster.

**How would you rank results?** Use term frequency and TF-IDF instead of a simple yes/no match.

**One-line takeaway:** An inverted index is the word-to-documents lookup that makes search fast; an AND query intersects the word lists.
