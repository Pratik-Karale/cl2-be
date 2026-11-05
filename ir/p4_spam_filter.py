"""Practical 4 - E-mail spam filtering with TF-IDF and Naive Bayes.

Aim
    Classify SMS messages as spam or ham using a text-classification pipeline.

Dataset
    data/spam.csv (Kaggle SMS Spam Collection; latin-1 encoding).

Prints
    Test accuracy, precision/recall/F1 per class, and two sample predictions.
"""

from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

BASE = Path(__file__).resolve().parent
DATA = BASE / "data"


def main() -> None:
    df = pd.read_csv(DATA / "spam.csv", encoding="latin-1")
    df = df.rename(columns={"v1": "label", "v2": "message"})[["label", "message"]].dropna()
    print("Messages:", len(df), "| Class counts:\n", df.label.value_counts().to_string())

    X_train, X_test, y_train, y_test = train_test_split(
        df.message, df.label, test_size=0.25, random_state=1
    )

    vectorizer = TfidfVectorizer(stop_words="english")
    model = MultinomialNB().fit(vectorizer.fit_transform(X_train), y_train)

    pred = model.predict(vectorizer.transform(X_test))
    print("\nAccuracy:", round(accuracy_score(y_test, pred), 4))
    print(classification_report(y_test, pred, zero_division=0))

    samples = [
        "Congratulations you win free cash prize click now",
        "team meeting tomorrow please review the report",
    ]
    for message in samples:
        print(f"'{message}' ->", model.predict(vectorizer.transform([message]))[0])


if __name__ == "__main__":
    main()
