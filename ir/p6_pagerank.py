"""Practical 6 - PageRank with power iteration.

Aim
    Rank five web pages from their link graph, then cross-check the result
    with the networkx PageRank implementation.

Graph
    A -> B, C
    B -> C
    C -> A
    D -> C, A
    E -> D, C

Prints
    PageRank scores from the power iteration and from networkx.
"""

import networkx as nx
import numpy as np

LINKS = {
    "A": ["B", "C"],
    "B": ["C"],
    "C": ["A"],
    "D": ["C", "A"],
    "E": ["D", "C"],
}


def main() -> None:
    pages = sorted(LINKS)
    n = len(pages)
    damping = 0.85
    idx = {page: i for i, page in enumerate(pages)}

    # M links[node] = 1 / outdegree of the page that points to it.
    M = np.zeros((n, n))
    for page, outs in LINKS.items():
        for target in outs:
            M[idx[target], idx[page]] = 1 / len(outs)

    rank = np.ones(n) / n
    for _ in range(100):
        rank = (1 - damping) / n + damping * M @ rank

    print("PageRank (power iteration):")
    for page in sorted(pages, key=lambda p: -rank[idx[p]]):
        print(f"  {page}: {rank[idx[page]]:.4f}")

    graph = nx.DiGraph([(page, target) for page, outs in LINKS.items() for target in outs])
    library = nx.pagerank(graph, alpha=damping)
    print("\nnetworkx cross-check:")
    for page, score in sorted(library.items(), key=lambda item: -item[1]):
        print(f"  {page}: {score:.4f}")


if __name__ == "__main__":
    main()
