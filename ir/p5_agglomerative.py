"""Practical 5 - Agglomerative hierarchical clustering on the Iris dataset.

Aim
    Build a dendrogram and cut the tree into three clusters, then compare
    the clusters with the true species using the Adjusted Rand Index.

Dataset
    Iris dataset bundled with scikit-learn.

Outputs
    outputs/p5_dendrogram.png
    outputs/p5_agglomerative_clusters.png
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import load_iris
from sklearn.metrics import adjusted_rand_score

OUT = Path(__file__).resolve().parents[1] / "outputs"
OUT.mkdir(exist_ok=True)


def main() -> None:
    X, y = load_iris(return_X_y=True)

    # The dendrogram shows the order and distance at which clusters merge.
    fig, ax = plt.subplots(figsize=(10, 4))
    dendrogram(linkage(X, method="ward"), truncate_mode="lastp", p=20, ax=ax)
    ax.set_title("Dendrogram (Ward linkage)")
    ax.set_xlabel("samples")
    ax.set_ylabel("distance")
    fig.tight_layout()
    fig.savefig(OUT / "p5_dendrogram.png", dpi=150)
    plt.close(fig)

    # Cut the tree into 3 clusters.
    labels = AgglomerativeClustering(n_clusters=3, linkage="ward").fit_predict(X)
    print("Agreement with real species (ARI):", round(adjusted_rand_score(y, labels), 3))

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(X[:, 2], X[:, 3], c=labels, cmap="viridis", s=35)
    ax.set_xlabel("petal length")
    ax.set_ylabel("petal width")
    ax.set_title("Agglomerative clusters (k=3)")
    fig.tight_layout()
    fig.savefig(OUT / "p5_agglomerative_clusters.png", dpi=150)
    plt.close(fig)
    print("Plots saved to", OUT)


if __name__ == "__main__":
    main()
