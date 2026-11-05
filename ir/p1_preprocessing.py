"""Practical 1 - Text pre-processing: lowercase, tokenize, stop-word removal, stemming.

Aim
    Clean a raw text document into meaningful root words.

Dataset
    data/docs/doc3.txt (a short sentence about stemming).

Prints
    Original text, tokens, tokens without stop words, and stemmed tokens.
"""

import re
from pathlib import Path

from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

BASE = Path(__file__).resolve().parent
DATA = BASE / "data"


def main() -> None:
    text = (DATA / "docs" / "doc3.txt").read_text(encoding="utf-8").strip()
    print("Original :", text)

    # Lowercase, remove punctuation, and split into word tokens.
    tokens = re.findall(r"[a-z]+", text.lower())
    print("Tokens   :", tokens)

    # Remove common words such as "is", "the", "and".
    filtered = [w for w in tokens if w not in ENGLISH_STOP_WORDS]
    print("No stop  :", filtered)

    # Reduce each word to a common root: running/runs/runner -> run.
    stemmer = PorterStemmer()
    stemmed = [stemmer.stem(w) for w in filtered]
    print("Stemmed  :", stemmed)


if __name__ == "__main__":
    main()
