# Practical 4 — E-mail Spam Filtering with TF-IDF and Naive Bayes (Viva Theory)

> **Scope note:** this practical may be one of the two uncertain IR assignments; kept for backup.

> **30-second answer:** Classify **5,572 SMS messages** as spam or ham using **TF-IDF** features and a **Multinomial Naive Bayes** classifier. Test accuracy is **0.9756**; spam recall is **0.81** and spam precision is **1.00**. The sample "free cash prize" message is predicted spam, and the meeting message is predicted ham.

## 1. MOST LIKELY — Core of the Experiment (High Yield)

**Aim:** Build a text classifier that filters spam e-mail/SMS messages.

**Dataset:** `data/spam.csv` — Kaggle SMS Spam Collection, **5,572 messages** (4,825 ham, 747 spam), latin-1 encoding.

**Pipeline in 6 bullets**
- Read the CSV, rename `v1`/`v2` to `label`/`message`, and drop missing rows.
- Split into **75% train / 25% test** with `random_state=1`.
- Convert messages to numeric features with **TF-IDF** (`TfidfVectorizer(stop_words="english")`).
- Fit **MultinomialNB** on the training features.
- Predict on the test set and report accuracy and a classification report.
- Predict two new sample messages.

**Code skeleton**
```python
vec = TfidfVectorizer(stop_words="english")
model = MultinomialNB().fit(vec.fit_transform(X_train), y_train)
pred = model.predict(vec.transform(X_test))
print(accuracy_score(y_test, pred))
print(classification_report(y_test, pred))
```

**Expected output**
- Messages: **5,572** — ham **4,825**, spam **747**
- Accuracy: **0.9756**
- Ham: precision **0.97**, recall **1.00**, F1 **0.99**
- Spam: precision **1.00**, recall **0.81**, F1 **0.90**
- Macro F1 **0.94**; weighted F1 **0.97**
- "Congratulations you win free cash prize click now" → **spam**
- "team meeting tomorrow please review the report" → **ham**

**Viva Q&A**
1. **Why TF-IDF and not raw counts?** TF-IDF downweights words that appear in almost every message and highlights distinctive words.
2. **What is TF-IDF?** Term frequency × inverse document frequency: frequent in this message, rare across the corpus.
3. **Why Multinomial Naive Bayes?** It is fast, works well with word-count-like features, and is a standard text-classification baseline.
4. **What does Naive Bayes assume?** That words are conditionally independent given the class.
5. **Why is spam recall only 0.81?** The model misses about 19% of spam; false negatives are the costly error for a spam filter.
6. **What does precision 1.00 for spam mean?** Every message predicted spam really was spam in this test set.
7. **Why is accuracy misleading here?** The classes are imbalanced (747 spam vs 4,825 ham), so a ham-only model would already score about 87%.
8. **What is the confusion matrix here?** Ham is almost perfectly recalled; the main errors are spam messages classified as ham.
9. **Why `encoding="latin-1"`?** The Kaggle CSV contains characters that are not valid UTF-8.
10. **Why split before fitting the vectorizer?** Fitting on all data would leak test vocabulary into training.
11. **How would you improve spam recall?** Adjust the decision threshold, use class weights, add n-grams, or try SVM/logistic regression.
12. **Is this e-mail or SMS?** The dataset is SMS messages, but the same pipeline applies to e-mail text.

## 2. LIKELY — Syllabus Theory Around This Practical

### Unit IV: Text Classification
- **Text classification:** assign a label to a document from its content.
- **TF-IDF:** a weighting scheme that balances term frequency against corpus frequency.
- **Naive Bayes:** a probabilistic classifier based on Bayes' theorem and conditional independence.
- **Evaluation:** confusion matrix, accuracy, precision, recall, F1.

### Unit I / III: IR Foundations
- **Vector space model:** documents and queries are vectors; TF-IDF is a common weighting.
- **Probabilistic ranking:** relevance is treated as a probability.

**Likely Q&A**
- *Precision vs recall?* Precision = of predicted spam, how many were real; recall = of real spam, how many were caught.
- *When is recall more important?* When missing a positive (spam, fraud, disease) is costly.
- *What is a confusion matrix?* A table of true positives, true negatives, false positives and false negatives.
- *What is class imbalance?* One class has far more examples than another.
- *Why use stratified splitting?* To keep the spam/ham ratio in both train and test.
- *What is a stop word?* A very common word removed before vectorizing.
- *What is an n-gram?* A sequence of n consecutive words; bigrams capture short phrases.
- *What is a baseline?* A simple model used for comparison, such as predicting the majority class.

## 3. LEAST LIKELY — Stretch / Edge Cases

- **Concept drift:** spam vocabulary changes over time, so the model must be retrained.
- **Adversarial spam:** spammers deliberately misspell words to evade filters.
- **Class imbalance:** accuracy hides poor minority-class performance; use F1 or PR-AUC.
- **Threshold tuning:** lowering the spam threshold raises recall but may lower precision.
- **Feature leakage:** fitting the vectorizer on test data inflates the score.
- **Alternatives:** linear SVM, logistic regression, random forest, or transformer models.
- **Trap question:** "Is 97.5% accuracy excellent?" Check the class balance and the spam recall before saying yes.

**If you remember only one thing:** A spam filter turns text into TF-IDF numbers and learns a Naive Bayes boundary; accuracy is not enough — check spam recall and precision.
