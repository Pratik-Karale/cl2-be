# Practical 2 — Document Retrieval with an Inverted Index (Viva Theory)

> **30-second answer:** Build a **word → documents** dictionary from six text files, then answer queries by intersecting the document sets of all query terms. `documents` returns **doc1, doc2, doc4**; `web pages` returns **doc4, doc5**; `spam filters` returns **doc6**.

## 1. MOST LIKELY — Core of the Experiment (High Yield)

**Aim:** Implement Boolean retrieval using an inverted index with AND semantics.

**Dataset:** `data/docs/doc1.txt` … `doc6.txt` — six one-sentence documents about IR, search engines, stemming, crawling, PageRank and spam.

**Pipeline in 5 bullets**
- Read every document and tokenize it with the regex `[a-z]+` after lowercasing.
- Build a `defaultdict(set)` mapping each word to the set of documents containing it.
- For a query, tokenize it the same way.
- Look up each term's document set and take the **intersection** — a document must contain **all** terms.
- Print the sorted document names.

**Code skeleton**
```python
index = defaultdict(set)
for name, text in docs.items():
    for word in re.findall(r"[a-z]+", text.lower()):
        index[word].add(name)

def search(query):
    sets = [index.get(w, set()) for w in re.findall(r"[a-z]+", query.lower())]
    return sorted(set.intersection(*sets)) if sets else []
```

**Expected output**
- Index sample: `documents → [doc1, doc2, doc4]`, `web → [doc4, doc5]`, `links → [doc4, doc5]`
- `documents` → `['doc1', 'doc2', 'doc4']`
- `web pages` → `['doc4', 'doc5']`
- `spam filters` → `['doc6']`

**Viva Q&A**
1. **What is an inverted index?** A mapping from each term to the list (or set) of documents that contain it.
2. **Why is it called inverted?** A forward index maps document → words; the inverted index reverses that to word → documents.
3. **Why use a set?** It removes duplicates and makes intersection fast.
4. **What does the AND query do?** It returns only documents that contain every query term.
5. **What would OR do?** Return the union of the document sets.
6. **What if a query term is absent?** `index.get(term, set())` returns an empty set, so the intersection is empty.
7. **Why tokenize the query the same way as documents?** So the query terms and indexed terms match exactly.
8. **What is the time complexity?** Roughly the size of the postings lists being intersected.
9. **How would you rank results?** Use term frequency, TF-IDF and cosine similarity instead of Boolean AND.
10. **What is a postings list?** The list of document IDs associated with a term in the index.
11. **What is a dictionary?** The set of all terms in the index.
12. **Why is Boolean retrieval limited?** It gives no ranking and treats all matching documents equally.

## 2. LIKELY — Syllabus Theory Around This Practical

### Unit I: Introduction to IR
- **Boolean retrieval:** documents match or do not match a Boolean query (`AND`, `OR`, `NOT`).
- **IR models:** Boolean, vector space, probabilistic and latent semantic indexing.

### Unit II: Dictionaries and Query Processing
- **Index components:** dictionary (terms) and postings (document lists).
- **Dictionary types:** sort-based, hash-based, interleaving with postings.
- **Index construction:** in-memory, sort-based, merge-based, disk-based.
- **Query processing:** document-at-a-time (DAAT) and term-at-a-time (TAAT).
- **Query optimization:** process the rarest term first to shrink candidate sets quickly.

**Likely Q&A**
- *What is a static vs dynamic index?* Static is built once; dynamic supports insertions and deletions.
- *What is DAAT?* Process one document at a time across all query terms.
- *What is TAAT?* Process one query term at a time and accumulate scores per document.
- *Why are postings sorted by document ID?* It makes intersection and compression efficient.
- *What is a skip pointer?* A shortcut that skips blocks of postings to speed up intersection.
- *What is index compression?* Storing postings compactly (for example, gap encoding) to reduce disk use.
- *Why is the rarest term processed first?* It gives the smallest candidate set and reduces work.
- *What is phrase search?* Matching terms in order, usually with a positional index.

## 3. LEAST LIKELY — Stretch / Edge Cases

- **Phrase queries:** need positional postings, not just document sets.
- **Wildcard queries:** need a dictionary structure such as a trie or permuterm index.
- **Ranked retrieval:** Boolean AND gives no score; TF-IDF and cosine similarity do.
- **Index updates:** new documents require merging or a dynamic index.
- **Compression:** gap encoding and variable-byte encoding reduce index size.
- **Scalability:** a distributed index shards documents across machines.
- **Trap question:** "Is a large postings list always good?" No — a term that appears in most documents is a poor discriminator.

**If you remember only one thing:** An inverted index is the word → documents lookup that makes retrieval fast; an AND query intersects the postings sets of all query terms.
