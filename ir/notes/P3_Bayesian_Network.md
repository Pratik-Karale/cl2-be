# Practical 3 — Bayesian Network for Heart-Disease Diagnosis (Viva Theory)

> **30-second answer:** Learn a Bayesian network from **675 heart-disease records**, with risk factors pointing to heart disease and heart disease pointing to symptoms. For the two example patients, the model estimates **P(heart disease) = 0.99** for the older male with exercise angina and **0.01** for the young female with no symptoms.

## 1. MOST LIKELY — Core of the Experiment (High Yield)

**Aim:** Build a Bayesian network from medical data and use probabilistic inference to diagnose heart disease.

**Dataset:** `data/heart_disease_uci.csv` — the UCI heart-disease dataset. After cleaning and dropping missing rows, **675 records** are used.

**Pipeline in 7 bullets**
- Read the CSV and normalise column names (`thalch` → `thalach`, `num` → `target`).
- Encode `sex` as 0/1 and turn the disease level into a binary `target`.
- Encode chest-pain type and exercise angina as numbers.
- Keep the eight relevant columns and drop missing rows; remove cholesterol values of 0 (not recorded).
- **Discretise** continuous columns (age, cholesterol, blood pressure, max heart rate) into low/medium/high bins.
- Define the network structure: risk factors → `target` → symptoms.
- Learn the probability tables with `model.fit(df)` and run `VariableElimination` for the two patients.

**Code skeleton**
```python
model = DiscreteBayesianNetwork([
    ("age", "target"), ("sex", "target"), ("chol", "target"),
    ("trestbps", "target"), ("target", "cp"),
    ("target", "exang"), ("target", "thalach")])
model.fit(df)
infer = VariableElimination(model)
p = infer.query(["target"], evidence={"age": 2, "sex": 1, "cp": 0, "exang": 1, "thalach": 0})
print(p.values[1])
```

**Expected output**
- Rows used: **675**
- Older male, chest pain = 0, exercise angina: **P(heart disease) = 0.99**
- Young female, no symptoms: **P(heart disease) = 0.01**

**Viva Q&A**
1. **What is a Bayesian network?** A graph of random variables where edges encode conditional dependencies and each node has a probability table.
2. **What do the edges mean here?** Risk factors influence heart disease, and heart disease influences symptoms.
3. **Why use a Bayesian network?** It combines prior probabilities with evidence and handles uncertainty.
4. **What is `VariableElimination`?** An exact inference algorithm that sums out irrelevant variables to compute a query.
5. **Why discretise continuous columns?** A discrete Bayesian network needs a finite set of states; bins make the table manageable.
6. **What does `model.fit(df)` learn?** The conditional probability tables from the data, usually by maximum likelihood.
7. **What is the evidence?** The observed values for a patient, such as age group, sex and symptoms.
8. **What is the query?** The probability of `target = 1` (heart disease) given that evidence.
9. **Why is the first patient's risk 0.99?** The combination of older age, male sex, chest pain and exercise angina is strongly associated with disease in this dataset.
10. **Why is the second patient's risk 0.01?** A young female with no symptoms matches the low-risk pattern.
11. **Does this prove causation?** No — it captures statistical association, not medical causation.
12. **What is the Naive Bayes connection?** Naive Bayes is a Bayesian network with one class node and all features independent given the class; this practical allows a richer structure.

## 2. LIKELY — Syllabus Theory Around This Practical

### Unit III: Probabilistic Retrieval and Language Modelling
- **Bayes' theorem:** posterior probability is proportional to likelihood × prior.
- **Probability ranking principle:** rank items by the probability that they are relevant.
- **Bayesian networks in IR:** model dependencies between terms, queries and documents.

### Unit IV: Text Classification
- **Bayesian classification:** predict a class from observed features.
- **Naive Bayes:** assumes features are conditionally independent given the class.
- **Bayesian network classifier:** relaxes that independence assumption with a graph.

**Likely Q&A**
- *What is conditional probability?* The probability of an event given that another event is known.
- *What is a prior?* The probability before seeing evidence.
- *What is a likelihood?* The probability of the evidence under a hypothesis.
- *What is a posterior?* The updated probability after seeing evidence.
- *What is structure learning?* Learning the graph edges from data instead of specifying them.
- *What is parameter learning?* Estimating the conditional probability tables for a fixed graph.
- *What is a CPT?* Conditional probability table — one row per parent-value combination.
- *What is the main limitation of Naive Bayes?* Its independence assumption is often unrealistic.

## 3. LEAST LIKELY — Stretch / Edge Cases

- **Discretisation choice:** too few bins lose information; too many bins make the tables sparse.
- **Missing data:** dropping rows loses information; imputation may be better.
- **Structure assumptions:** a wrong graph gives wrong inferences even with good data.
- **Small samples:** rare parent combinations produce unreliable probabilities.
- **Causal claims:** an edge is not proof of causation.
- **Scalability:** exact inference is exponential in the worst case; large networks need approximate methods.
- **Trap question:** "Is a higher probability always more accurate?" No — calibration and validation matter.

**If you remember only one thing:** A Bayesian network turns a graph of dependencies into conditional probability tables, and inference combines those tables with patient evidence to produce a diagnosis probability.
