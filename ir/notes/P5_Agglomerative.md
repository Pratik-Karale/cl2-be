# Practical 5 — Agglomerative Hierarchical Clustering (Viva Theory)

> **Scope note:** this practical may be one of the two uncertain IR assignments; kept for backup.

> **30-second answer:** Build a **dendrogram** for the Iris data with **Ward linkage**, cut the tree into **3 clusters**, and compare the clusters with the true species. The **Adjusted Rand Index is 0.731**, showing strong but not perfect agreement.

## 1. MOST LIKELY — Core of the Experiment (High Yield)

**Aim:** Cluster unlabeled data with agglomerative hierarchical clustering and visualise the merge process.

**Dataset:** Iris — **150 samples, 4 features, 3 species** (bundled with scikit-learn).

**Pipeline in 5 bullets**
- Load `X` and the true labels `y` from `load_iris(return_X_y=True)`.
- Compute the **linkage matrix** with Ward's method.
- Draw a **dendrogram** (truncated to the last 20 merges).
- Cut the tree into **3 clusters** with `AgglomerativeClustering(n_clusters=3, linkage="ward")`.
- Compare the cluster labels with the true species using the **Adjusted Rand Index**.

**Code skeleton**
```python
X, y = load_iris(return_X_y=True)
dendrogram(linkage(X, method="ward"), truncate_mode="lastp", p=20)
labels = AgglomerativeClustering(n_clusters=3, linkage="ward").fit_predict(X)
print(adjusted_rand_score(y, labels))
```

**Expected output**
- **ARI = 0.731**
- Two plots saved: `outputs/p5_dendrogram.png` and `outputs/p5_agglomerative_clusters.png`

**Viva Q&A**
1. **What is agglomerative clustering?** A bottom-up method: start with every point as its own cluster and repeatedly merge the closest pair.
2. **What is divisive clustering?** The top-down opposite: start with one cluster and repeatedly split.
3. **What is a dendrogram?** A tree diagram showing which clusters merge and at what distance.
4. **What does Ward linkage do?** It merges the pair that increases within-cluster variance the least.
5. **Why use Ward?** It tends to produce compact, balanced clusters.
6. **How do you choose the number of clusters?** Cut the dendrogram at a large vertical gap, or use domain knowledge (here, 3 species).
7. **What is ARI?** Adjusted Rand Index — agreement between two labelings, corrected for chance. 1 = perfect, 0 = random.
8. **Why is ARI 0.731 not 1.0?** The clusters are based only on the four measurements, and two Iris species overlap.
9. **Does clustering use the true labels?** No — `y` is used only for evaluation.
10. **What is the time complexity?** Naive agglomerative clustering is roughly O(n²) or worse; it does not scale to huge datasets.
11. **What is the difference from K-Means?** K-Means partitions around centroids and needs k; hierarchical clustering builds a full merge tree.
12. **What distance measure is used?** Euclidean distance by default, with Ward linkage.

## 2. LIKELY — Syllabus Theory Around This Practical

### Unit IV: Text Clustering
- **Clustering vs classification:** clustering is unsupervised; classification uses labels.
- **Partitioning methods:** K-Means, K-Medoids.
- **Hierarchical methods:** agglomerative (bottom-up) and divisive (top-down).
- **Linkage methods:** single, complete, average, Ward.
- **Dendrogram:** visualises the hierarchy and helps choose the cut level.

**Likely Q&A**
- *What is single linkage?* Merge clusters whose closest points are nearest; can create long chains.
- *What is complete linkage?* Merge clusters whose farthest points are nearest; tends to make compact clusters.
- *What is average linkage?* Use the average pairwise distance between clusters.
- *What is a distance matrix?* Pairwise distances between all points or clusters.
- *What is the curse of dimensionality?* In high dimensions, distances become less meaningful.
- *Why scale features before clustering?* Otherwise a large-range feature dominates the distance.
- *What is K-Means?* A centroid-based partitioning algorithm that alternates assignment and centroid updates.
- *What is silhouette?* A measure of how well a point fits its own cluster versus the nearest other cluster.

## 3. LEAST LIKELY — Stretch / Edge Cases

- **Scalability:** hierarchical clustering is expensive for large n; use sampling or K-Means first.
- **Linkage choice:** different linkages can give very different trees.
- **Noise and outliers:** single linkage is especially sensitive.
- **Feature scaling:** essential when features have different units.
- **Categorical data:** Euclidean distance is inappropriate; use matching or Jaccard distance.
- **Cutting the tree:** there is no single correct k; domain knowledge and validation help.
- **Trap question:** "Does a taller dendrogram mean better clusters?" No — height shows merge distance, not cluster quality.

**If you remember only one thing:** Agglomerative clustering builds a merge tree bottom-up; cut the dendrogram where the gap is large, and use ARI or silhouette to judge the result.
