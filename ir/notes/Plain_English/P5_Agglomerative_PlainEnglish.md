# Practical 5 — Agglomerative Clustering in Plain English

> **In one sentence:** We let the computer group similar flowers step by step, drawing a family tree of merges and cutting it into three groups.

## The problem in everyday words

You have 150 flowers with four measurements each, but you hide the species labels. Can the computer discover groups that mostly match the real species? This is clustering: finding groups without being told the answers.

## What the main idea is, without jargon

Imagine every flower starts as its own tiny group. The computer repeatedly finds the two closest groups and merges them. It keeps merging until everything is one big group.

The record of those merges is a **dendrogram** — a tree that shows which groups joined and how far apart they were when they joined.

To get the final clusters, you cut the tree at a chosen height. Here we cut it into three groups because we know there are three species.

## What the code does, step by step

1. Load the Iris measurements; keep the true species only for checking later.
2. Compute the distances between flowers and build the merge tree with Ward's method.
3. Draw the dendrogram.
4. Cut the tree into three clusters.
5. Compare the computer's clusters with the true species using the Adjusted Rand Index.
6. Draw the clusters on a petal-length vs petal-width plot.

## What the result means

The **Adjusted Rand Index is 0.731**. A score of 1 means the clusters match the species perfectly; 0 means random grouping. So 0.731 is strong agreement: most flowers are grouped with their own species, but two species overlap and a few flowers are on the wrong side.

The plots are saved in `outputs/`:
- `p5_dendrogram.png` shows the merge tree.
- `p5_agglomerative_clusters.png` shows the three clusters.

## Why these choices?

- Agglomerative clustering builds the full hierarchy, so you can choose the number of groups after seeing the tree.
- Ward linkage tends to make compact, balanced clusters.
- Three clusters match the known number of species.
- ARI is a fair comparison because it corrects for random agreement.

## If the examiner asks (plain answers)

**What is agglomerative clustering?** A bottom-up method that starts with single points and merges the closest groups.

**What is a dendrogram?** A tree diagram of the merges.

**What does Ward linkage do?** It merges the pair that increases the spread inside clusters the least.

**How do you choose the number of clusters?** Cut the tree where the vertical gap is large, or use domain knowledge.

**Does clustering use the true labels?** No; the labels are only used to check the result.

**Why is ARI not 1.0?** Two Iris species overlap in their measurements, so some flowers are genuinely hard to separate.

**Is this better than K-Means?** It gives a hierarchy and does not need k in advance, but it is slower on large data.

**One-line takeaway:** Agglomerative clustering builds a merge tree bottom-up; cut the tree where the gap is large and check the groups with ARI or silhouette.
