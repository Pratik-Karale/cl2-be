"""Practical 2 - Document retrieval using an inverted index with AND search.

Aim
    Build a word -> documents index and answer multi-word queries by
    returning documents that contain all query terms.

Dataset
    data/docs/*.txt (six short documents).

Prints
    A sample of the index and the result of several queries.
"""

import glob
import os
import re
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA = BASE / "data"


def main() -> None:
    docs = {
        os.path.basename(path)[:-4]: Path(path).read_text(encoding="utf-8")
        for path in sorted(glob.glob(str(DATA / "docs" / "*.txt")))
    }

    # word -> set of document names that contain it
    index = defaultdict(set)
    for name, text in docs.items():
        for word in re.findall(r"[a-z]+", text.lower()):
            index[word].add(name)

    print("Index sample:", {w: sorted(index[w]) for w in ["documents", "web", "links"]})

    def search(query: str) -> list[str]:
        terms = re.findall(r"[a-z]+", query.lower())
        sets = [index.get(w, set()) for w in terms]
        return sorted(set.intersection(*sets)) if sets else []

    for query in ["documents", "web pages", "spam filters"]:
        print(f"Query '{query}' ->", search(query))


if __name__ == "__main__":
    main()
