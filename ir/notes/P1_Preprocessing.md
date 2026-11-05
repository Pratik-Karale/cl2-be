# Practical 1 — Text Pre-processing: Stop Words and Stemming (Viva Theory)

> **30-second answer:** Clean a raw sentence by lowercasing it, splitting it into word tokens, removing common stop words, and reducing each word to its root with the **Porter stemmer**. For the sample sentence, `running`, `runs` and `runner` all become **`run`**.

## 1. MOST LIKELY — Core of the Experiment (High Yield)

**Aim:** Pre-process a text document so that later retrieval and classification steps see clean, meaningful terms.

**Dataset:** `data/docs/doc3.txt` — the sentence: *"Stemming reduces words like running, runs and runner to the common root run."*

**Pipeline in 5 bullets**
- Read the text and **lowercase** it.
- Remove punctuation and split into tokens with `re.findall(r"[a-z]+", text.lower())`.
- Remove **stop words** using scikit-learn's built-in `ENGLISH_STOP_WORDS`.
- Apply the **PorterStemmer** to each remaining token.
- Print each stage so the transformation is visible.

**Code skeleton**
```python
text = (DATA / "docs" / "doc3.txt").read_text()
tokens = re.findall(r"[a-z]+", text.lower())
filtered = [w for w in tokens if w not in ENGLISH_STOP_WORDS]
stemmed = [PorterStemmer().stem(w) for w in filtered]
```

**Expected output**
- Tokens: `stemming, reduces, words, like, running, runs, and, runner, to, the, common, root, run`
- After stop-word removal: `stemming, reduces, words, like, running, runs, runner, common, root, run`
- Stemmed: `stem, reduc, word, like, run, run, runner, common, root, run`

**Viva Q&A**
1. **Why lowercase?** So `Search` and `search` are treated as the same term.
2. **What is tokenization?** Splitting text into individual words or terms.
3. **What are stop words?** Very common words such as `the`, `is`, `and` that carry little meaning for retrieval.
4. **Why remove stop words?** They appear everywhere, so they add little discriminating power and increase index size.
5. **What is stemming?** Reducing a word to a common root by removing suffixes.
6. **Why do `running`, `runs` and `runner` become `run`?** They share the same root; stemming collapses them so a query for `run` can match all three.
7. **Why is `runner` not reduced to `run` here?** Porter's rules do not handle every suffix; this is a known limitation, not a bug.
8. **Stemming vs lemmatization?** Stemming chops suffixes with rules and may produce non-words (`reduc`); lemmatization uses a dictionary and returns a real word (`reduce`).
9. **What is the Porter stemmer?** A rule-based English stemming algorithm by Martin Porter.
10. **Does the order matter?** Yes: lowercase → tokenize → remove stop words → stem. Stemming before stop-word removal could change the stop-word match.
11. **Does this lose information?** Yes — stop words can matter in phrases, and over-stemming can merge different words.
12. **Where is this used?** Inverted-index construction, search queries, text classification, and topic modelling.

## 2. LIKELY — Syllabus Theory Around This Practical

### Unit I: Introduction to IR
- **Information retrieval** finds relevant documents for an information need; text pre-processing is the first stage of the IR pipeline.
- **IR vs data retrieval:** IR deals with unstructured text and ranked relevance; data retrieval deals with structured records and exact matches.
- **Text operations:** tokenization, normalization, stop-word removal, stemming, lemmatization, case folding.

### Unit II: Dictionaries and Query Processing
- Pre-processing produces the **terms** stored in the inverted index.
- Fewer, cleaner terms mean a smaller dictionary and faster query processing.

**Likely Q&A**
- *What is a term?* A normalized token stored in the index.
- *What is case folding?* Converting text to one case, usually lowercase.
- *What is over-stemming?* Different words collapse to one root incorrectly (for example, `university` and `universe`).
- *What is under-stemming?* Related words remain separate (for example, `runner` and `run`).
- *Name two stemming algorithms.* Porter and Lancaster (Paice/Husk).
- *Why not always use lemmatization?* It is slower and needs linguistic resources such as WordNet.
- *What is a stop-word list?* A predefined set of common words removed before indexing.
- *Can removing stop words hurt?* Yes, for phrase queries such as "to be or not to be".

## 3. LEAST LIKELY — Stretch / Edge Cases

- **Apostrophes and contractions:** `don't` may become `don` and `t`; a better tokenizer handles contractions.
- **Unicode and accents:** normalize with Unicode normalization and strip accents carefully.
- **URLs, emails, hashtags:** regex `[a-z]+` removes digits and symbols; domain-specific tokenizers are needed.
- **Domain stop words:** words common in one corpus (for example, `patient` in medical text) may need removal.
- **Stemming vs lemmatization:** lemmatization preserves meaning better but costs more.
- **Language:** Porter is English-specific; other languages need different stemmers.
- **Trap question:** "Is stemming always better?" No — it can merge unrelated words and hurt precision.

**If you remember only one thing:** Pre-processing turns raw text into clean root terms — lowercase, tokenize, drop stop words, then stem — and this is what the index and every later model actually see.
