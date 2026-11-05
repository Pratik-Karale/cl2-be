"""Practical 3 - Bayesian network for heart-disease diagnosis.

Aim
    Learn a Bayesian network from heart-disease data and use it to estimate
    the probability of heart disease for two example patients.

Dataset
    data/heart_disease_uci.csv (UCI heart-disease data).

Prints
    Dataset shape and P(heart disease) for two evidence sets.
"""

from pathlib import Path

import pandas as pd

try:
    from pgmpy.models import DiscreteBayesianNetwork
except ImportError:  # older pgmpy versions
    from pgmpy.models import BayesianNetwork as DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination

BASE = Path(__file__).resolve().parent
DATA = BASE / "data"


def main() -> None:
    df = pd.read_csv(DATA / "heart_disease_uci.csv")

    # Normalise different Kaggle column names.
    df = df.rename(columns={"thalch": "thalach", "num": "target", "HeartDisease": "target"})
    df["sex"] = df.sex.replace({"Male": 1, "Female": 0})
    df["target"] = (df.target > 0).astype(int)  # any disease level -> 1
    df["cp"] = df.cp.astype("category").cat.codes
    df["exang"] = df.exang.astype(str).str.lower().map(
        {"true": 1, "false": 0, "1": 1, "0": 0, "1.0": 1, "0.0": 0}
    )
    df = df[["age", "sex", "cp", "trestbps", "chol", "exang", "thalach", "target"]].dropna()
    df = df[df.chol > 0].astype(float)  # chol = 0 means "not recorded"

    # Discretise continuous columns into low / medium / high.
    for col, cuts in {
        "age": [45, 60],
        "chol": [200, 240],
        "trestbps": [120, 140],
        "thalach": [120, 150],
    }.items():
        df[col] = pd.cut(df[col], [-float("inf")] + cuts + [float("inf")], labels=[0, 1, 2]).astype(int)
    df = df.astype(int)

    print("Rows used:", len(df))

    # Risk factors -> heart disease -> symptoms.
    model = DiscreteBayesianNetwork(
        [
            ("age", "target"),
            ("sex", "target"),
            ("chol", "target"),
            ("trestbps", "target"),
            ("target", "cp"),
            ("target", "exang"),
            ("target", "thalach"),
        ]
    )
    model.fit(df)
    infer = VariableElimination(model)

    cases = {
        "older male, chest pain=0, exercise angina": {
            "age": 2, "sex": 1, "cp": 0, "exang": 1, "thalach": 0
        },
        "young female, no symptoms": {
            "age": 0, "sex": 0, "cp": 2, "exang": 0, "thalach": 2
        },
    }
    for name, evidence in cases.items():
        result = infer.query(["target"], evidence=evidence, show_progress=False)
        print(f"{name}: P(heart disease) = {result.values[1]:.2f}")


if __name__ == "__main__":
    main()
