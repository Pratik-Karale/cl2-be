# Practical 6 — PageRank with Power Iteration (Viva Theory)

> **30-second answer:** Compute PageRank on a five-page link graph using **power iteration** with damping factor **0.85**, then cross-check with networkx. The ranking is **C (0.3747), A (0.3667), B (0.1858), D (0.0428), E (0.0300)** — identical to networkx.

## 1. MOST LIKELY — Core of the Experiment (High Yield)

**Aim:** Implement the PageRank algorithm from scratch and verify it against a library.

**Graph:**
```
A -> B, C
B -> C
C -> A
D -> C, A
E -> D, C
```

**Pipeline in 6 bullets**
- List the pages and build an index for matrix positions.
- Build the transition matrix `M`, where `M[target, source] = 1 / outdegree(source)`.
- Start with equal rank `1/n` for every page.
- Repeat the update **100 times**: `rank = (1 - d)/n + d × M × rank`.
- Sort pages by rank.
- Compare with `networkx.pagerank(graph, alpha=0.85)`.

**Code skeleton**
```python
rank = np.ones(n) / n
for _ in range(100):
    rank = (1 - damping) / n + damping * M @ rank
print(sorted(zip(pages, rank), key=lambda x: -x[1]))
```

**Expected output**
- C: **0.3747**
- A: **0.3667**
- B: **0.1858**
- D: **0.0428**
- E: **0.0300**
- networkx gives the same values.

**Viva Q&A**
1. **What is PageRank?** A link-based ranking that treats a link as a vote and gives more weight to votes from important pages.
2. **Why is C ranked first?** C receives links from A, B, D and E — many votes — and A is also important.
3. **What is the damping factor?** The probability (0.85) of following a link instead of jumping to a random page.
4. **Why is there a random-jump term?** It prevents rank from getting trapped in cycles and models a random surfer.
5. **What is power iteration?** Repeatedly multiply the rank vector by the transition matrix until it converges.
6. **Why 100 iterations?** It is more than enough for this small graph to converge; the rank changes become negligible.
7. **What is a dangling node?** A page with no outgoing links; it needs special handling so rank does not disappear.
8. **What does `M[target, source] = 1/outdegree` mean?** A source page divides its vote equally among the pages it links to.
9. **Why does networkx agree?** Both implement the same PageRank recurrence with the same damping factor.
10. **What is the random surfer model?** A user follows links with probability d and jumps to a random page with probability 1-d.
11. **Does PageRank use page content?** No — it uses only the link structure.
12. **What is the main limitation?** Link spam and dead links can distort the ranking.

## 2. LIKELY — Syllabus Theory Around This Practical

### Unit V: Web Retrieval and Web Crawling
- **Search engine ranking:** combine content relevance with link-based authority.
- **Link-based ranking:** PageRank and HITS.
- **PageRank:** importance flows along links; a page is important if important pages link to it.
- **Simple ranking functions and evaluation:** compare rankings with precision/recall or human judgments.

**Likely Q&A**
- *What is the difference between PageRank and HITS?* PageRank gives one global authority score; HITS produces hubs and authorities.
- *What is a hub?* A page that links to many good authorities.
- *What is an authority?* A page that is linked to by many good hubs.
- *What is the teleportation term?* The `(1-d)/n` random-jump contribution.
- *What is convergence?* The rank vector stops changing beyond a small tolerance.
- *Why normalize the rank vector?* So the scores sum to 1 and can be interpreted as probabilities.
- *What is personalized PageRank?* The random jump is biased toward a set of preferred pages.
- *How does link spam affect PageRank?* Fake links can inflate a page's score; spam detection is needed.

## 3. LEAST LIKELY — Stretch / Edge Cases

- **Dangling nodes:** distribute their rank uniformly or to a teleport set.
- **Personalized/trusted PageRank:** use a non-uniform teleport vector.
- **Scalability:** real web graphs need sparse matrices and distributed computation.
- **Convergence rate:** depends on the damping factor; values near 1 converge slowly.
- **Link farms:** coordinated fake links can manipulate rankings.
- **Dynamic graphs:** recomputing PageRank as links change is expensive.
- **Trap question:** "Is a page with the most links always ranked first?" No — the importance of the linking pages matters too.

**If you remember only one thing:** PageRank is repeated voting along links with a random-jump term; power iteration converges to the same scores as networkx.
