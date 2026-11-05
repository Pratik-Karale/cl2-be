# IR Evaluation Metrics — Quick Explanation

> Every formula is written in plain text, and every symbol is explained underneath. No LaTeX, no images.

---

## 0. Which metric for which task

| Task | Main metrics |
|---|---|
| Spam classification | Accuracy (only if balanced), precision, recall, F1, confusion matrix |
| Ranked retrieval | Precision@k, recall@k, MAP, MRR, nDCG |
| Clustering | Adjusted Rand Index (ARI), silhouette |
| Index/query efficiency | Index size, query time, number of postings |
| Link ranking | PageRank score, convergence, damping factor |
| Bayesian diagnosis | Query probability, classification accuracy |

---

## 1. Classification metrics (spam filter, diagnosis)

### 1.1 Confusion matrix

```
                        Predicted positive     Predicted negative
Actual positive              TP                     FN
Actual negative              FP                     TN
```

| Term | Plain meaning |
|---|---|
| **TP** | Spam correctly marked spam |
| **TN** | Normal mail correctly marked normal |
| **FP** | Normal mail wrongly marked spam (false alarm) |
| **FN** | Spam wrongly marked normal (missed spam) |

### 1.2 The formulas

```
Accuracy   = (TP + TN) ÷ (TP + TN + FP + FN)
Precision  = TP ÷ (TP + FP)
Recall     = TP ÷ (TP + FN)
F1         = 2 × (Precision × Recall) ÷ (Precision + Recall)
Specificity= TN ÷ (TN + FP)
```

- **Accuracy** = how many predictions were correct overall. Misleading when spam is rare.
- **Precision** = when the model says "spam", how often it is right. High precision = few false alarms.
- **Recall** = of all real spam, how much was caught. High recall = few missed spam.
- **F1** = one balanced number; high only when both precision and recall are high.
- **Specificity** = of all normal mail, how much was correctly left alone.

### 1.3 Worked example

Suppose TP = 40 spam caught, FN = 10 spam missed, FP = 5 normal marked spam, TN = 45 normal left alone.

| Metric | Calculation | Result |
|---|---|---|
| Accuracy | (40 + 45) ÷ 100 | **0.85** |
| Precision | 40 ÷ (40 + 5) | **0.889** |
| Recall | 40 ÷ (40 + 10) | **0.80** |
| Specificity | 45 ÷ (45 + 5) | **0.90** |
| F1 | 2 × (0.889 × 0.80) ÷ (0.889 + 0.80) | **0.842** |

### 1.4 Which one to quote

| Situation | Quote |
|---|---|
| Balanced classes | Accuracy + F1 |
| Imbalanced spam data | Precision, recall, F1 (not accuracy alone) |
| Missing spam is costly | Recall |
| False alarms are costly | Precision |
| Need one number | F1 |

---

## 2. Ranking metrics (search results)

These assume a query returns a ranked list; relevant documents are known for evaluation.

**Precision@k** — of the top k results, how many are relevant?
```
Precision@k = relevant items in top k ÷ k
```

**Recall@k** — of all relevant documents, how many appear in the top k?
```
Recall@k = relevant items in top k ÷ total relevant items
```

**Average Precision (AP)** — precision at each relevant position, averaged over relevant items.
```
AP = (sum of Precision@position for each relevant item) ÷ (number of relevant items)
```
AP rewards putting relevant documents near the top.

**MAP (Mean Average Precision)** — average of AP over all queries.
```
MAP = sum of AP for all queries ÷ number of queries
```

**MRR (Mean Reciprocal Rank)** — 1 ÷ rank of the first relevant result, averaged over queries.
```
MRR = average of (1 ÷ rank of first relevant result)
```
Useful when there is one correct answer.

**nDCG (normalized Discounted Cumulative Gain)** — graded relevance, discounted by position.
```
DCG  = sum of (relevance of result at position i ÷ log2(i + 1))
nDCG = DCG ÷ ideal DCG
```
Ideal DCG = DCG of the perfect ranking. nDCG is 1 for a perfect ranking, 0 for no relevant results.

---

## 3. Clustering metrics

**Adjusted Rand Index (ARI)** — agreement between predicted clusters and known labels, corrected for chance.
```
ARI = 1   perfect agreement
ARI = 0   random labelling
```
Used in P5 to compare the 3 clusters with the 3 Iris species.

**Silhouette score** — how well each point fits its own cluster compared with the nearest other cluster.
```
s = (b − a) ÷ max(a, b)
a = average distance to points in the same cluster
b = average distance to points in the nearest other cluster
```
Range −1 to +1; closer to +1 is better. Needs at least 2 clusters.

**Inertia (WCSS)** — sum of squared distances from points to their own cluster centre; lower is tighter. Used with the elbow method.

---

## 4. IR-specific quantities

**TF-IDF**
```
TF-IDF(term, document) = term frequency in the document × log(total documents ÷ documents containing the term)
```
Frequent-in-one-document but rare-in-corpus words get high scores; common words get low scores.

**Cosine similarity**
```
cosine(A, B) = (A · B) ÷ (length of A × length of B)
```
1 = same direction, 0 = unrelated, −1 = opposite.

**PageRank**
```
rank(page) = (1 − d) ÷ N + d × sum of (rank of linking page ÷ its number of outlinks)
```
`d` = damping factor (usually 0.85), `N` = number of pages. Power iteration repeats until the scores stop changing.

**Index size**
```
postings per term = number of documents containing that term
total index size  = sum of postings over all terms
```
Smaller index = faster lookup and less storage.

---

## 5. Bayesian-network evaluation

- **Query probability:** `P(target | evidence)` from variable elimination; report the probability and the most likely state.
- **Prediction accuracy:** compare the most likely diagnosis with the known label on held-out rows.
- **Calibration:** does a predicted 70% risk actually occur about 70% of the time?
- **Structure:** a wrong edge (missing or extra dependency) changes every query, so validate the graph with domain knowledge.

---

## 6. Traps examiners love

| Trap | Correct answer |
|---|---|
| "Accuracy is 99%, so the spam filter is great." | If 99% of mail is normal, always predicting normal gives 99% accuracy. Use precision/recall/F1. |
| "Precision and recall are the same." | Precision looks at predicted positives; recall looks at actual positives. |
| "F1 uses TN." | F1 uses TP, FP and FN; it ignores TN. |
| "Higher precision always means better." | Recall may collapse; report both or F1. |
| "MAP and accuracy are the same." | MAP evaluates a ranked list; accuracy evaluates labels. |
| "nDCG can exceed 1." | It is normalized by the ideal DCG, so it is at most 1. |
| "ARI of 0 means perfect clustering." | ARI 1 = perfect, 0 = random. |
| "Silhouette works for one cluster." | It needs at least two clusters. |
| "PageRank counts only the number of links." | It weights links by the importance of the linking page and divides by its outlinks. |
| "Cosine similarity depends on document length." | It is normalized, so length cancels out. |

---

## 7. Formula sheet

```
Classification
  Accuracy    = (TP + TN) ÷ total
  Precision   = TP ÷ (TP + FP)
  Recall      = TP ÷ (TP + FN)
  F1          = 2 × (Precision × Recall) ÷ (Precision + Recall)
  Specificity = TN ÷ (TN + FP)

Ranking
  Precision@k = relevant in top k ÷ k
  Recall@k    = relevant in top k ÷ total relevant
  AP          = average of Precision@position over relevant items
  MAP         = average of AP over queries
  MRR         = average of (1 ÷ rank of first relevant result)
  DCG         = sum of relevance ÷ log2(position + 1)
  nDCG        = DCG ÷ ideal DCG

Clustering
  Silhouette  = (b − a) ÷ max(a, b)
  Inertia     = sum of squared distances to own cluster centre
  ARI         = 1 perfect, 0 random

IR quantities
  TF-IDF      = TF × log(total documents ÷ documents with term)
  Cosine      = (A · B) ÷ (|A| × |B|)
  PageRank    = (1 − d) ÷ N + d × sum(rank ÷ outlinks)
```

---

## 8. Last-minute "say this" lines

- **Spam filter:** "TF-IDF turns messages into numbers, Naive Bayes classifies them, and I report precision, recall and F1 because the classes are imbalanced."
- **Search ranking:** "Precision@k asks how many of the top k are relevant; MAP averages precision over all relevant positions; nDCG handles graded relevance."
- **Clustering:** "ARI compares clusters with known labels; silhouette measures separation without labels."
- **PageRank:** "A page is important if important pages link to it, with damping and outlink normalization."
- **Bayesian diagnosis:** "Variable elimination returns the probability of disease given the observed risk factors."
