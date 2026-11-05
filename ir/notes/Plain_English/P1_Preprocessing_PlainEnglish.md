# Practical 1 — Text Pre-processing in Plain English

> **In one sentence:** We take a messy sentence and clean it into simple root words so a search engine or classifier can work with it.

## The problem in everyday words

A computer does not understand a sentence the way you do. It sees punctuation, capital letters, and different forms of the same word: "running", "runs", "runner". If we search for "run", we would like all three to match. Before any search or classification, we clean the text.

## What the main idea is, without jargon

Think of preparing vegetables before cooking. You wash them, remove the parts you do not need, and cut them into pieces. Text pre-processing does the same:

- **Lowercase:** "Search" and "search" become the same word.
- **Tokenize:** split the sentence into individual words.
- **Remove stop words:** throw away very common words such as "the", "is", "and" that do not help distinguish documents.
- **Stem:** chop word endings so "running", "runs" and "runner" become "run".

The result is a short list of meaningful roots.

## What the code does, step by step

1. Read the sample sentence from `data/docs/doc3.txt`.
2. Make everything lowercase and keep only letters, which removes punctuation.
3. Split the cleaned text into word tokens.
4. Remove words that appear in the built-in English stop-word list.
5. Run the Porter stemmer on each remaining word.
6. Print the text at every stage so you can see the changes.

## What the result means

The original sentence is:
"Stemming reduces words like running, runs and runner to the common root run."

After tokenizing, we get all the words, including "and", "to" and "the". After stop-word removal, those common words disappear. After stemming, "running" and "runs" become "run". "Runner" stays as "runner" because the Porter rules do not handle every ending — that is a known limitation, not an error.

## Why these choices?

- Lowercasing and regex keep the token list consistent.
- The built-in stop-word list works offline and needs no download.
- Porter is a classic, fast, rule-based stemmer.
- Printing each stage makes the pipeline easy to explain in a viva.

## If the examiner asks (plain answers)

**Why remove stop words?** They appear in almost every document, so they do not help tell documents apart.

**What is stemming?** Cutting a word down to a common root by removing suffixes.

**Why do "running" and "runs" both become "run"?** They share the same root, and stemming collapses them.

**Why did "runner" not become "run"?** Stemming is rule-based and imperfect; it sometimes under-stems.

**Stemming or lemmatization?** Stemming is faster but may produce non-words; lemmatization uses a dictionary and returns real words.

**Does this lose meaning?** Yes, a little — stop words can matter in phrases, and stemming can merge unrelated words.

**What is tokenization?** Splitting text into words or terms.

**One-line takeaway:** Pre-processing turns raw text into clean root words; every later search or classifier works on that cleaned list.
