# Information Retrieval — 417524B

Seven runnable practicals. Run from the repository root:

```bash
python ir/p1_preprocessing.py
python ir/p2_inverted_index.py
python ir/p3_bayesian_network.py
python ir/p4_spam_filter.py
python ir/p5_agglomerative.py
python ir/p6_pagerank.py
python ir/p7_web_crawler.py
```

| Script | What it demonstrates |
|---|---|
| `p1_preprocessing.py` | Lowercase, regex tokenization, stop-word removal, Porter stemming |
| `p2_inverted_index.py` | Word → document index, AND query retrieval |
| `p3_bayesian_network.py` | pgmpy Bayesian network for heart-disease diagnosis |
| `p4_spam_filter.py` | TF-IDF features + Multinomial Naive Bayes; accuracy and classification report |
| `p5_agglomerative.py` | Ward-linkage agglomerative clustering, dendrogram, ARI |
| `p6_pagerank.py` | PageRank by power iteration, cross-checked with NetworkX |
| `p7_web_crawler.py` | requests + BeautifulSoup crawler, product CSV output |

## Data

`data/` contains:

- `docs/doc1.txt` … `doc6.txt` — six short documents for P1 and P2
- `heart_disease_uci.csv` — heart-disease data for P3
- `spam.csv` — SMS spam data for P4
- `products.csv` — sample crawler output

P7 uses <https://books.toscrape.com> when online and falls back to a built-in sample page when offline.

## Scope note

P4 (spam filter) and P5 (agglomerative clustering) are marked **backup** because they were the two IR assignments not covered by the local submissions. Keep them ready in case the examiner asks.

## Notes

- `notes/Pn_*.md` — code, outputs, syllabus theory, likely viva Q&A.
- `notes/Plain_English/Pn_*_PlainEnglish.md` — the same practical without math or jargon.
