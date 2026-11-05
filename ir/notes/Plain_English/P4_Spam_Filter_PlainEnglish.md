# Practical 4 — Spam Filter in Plain English

> **In one sentence:** We teach a program to recognise spam messages by learning which words are common in spam and which are common in normal messages.

## The problem in everyday words

Your inbox receives both real messages and junk. You want a filter that sends junk to the spam folder. The filter must learn from examples because spammers keep changing their wording.

## What the main idea is, without jargon

Think of a new employee sorting mail. You show them hundreds of spam and normal messages. They notice that spam often contains words like "free", "win", "cash" and "click", while normal messages contain words like "meeting", "report" and "tomorrow".

The computer does the same, but it converts each message into numbers.

- **TF-IDF** gives each word a weight: common in this message, but rare across all messages, means a high weight.
- **Naive Bayes** uses those weights to estimate which class is more likely.

## What the code does, step by step

1. Load the SMS dataset of 5,572 messages.
2. Split it into a training set and a test set.
3. Convert the training messages into TF-IDF numbers.
4. Train a Multinomial Naive Bayes classifier.
5. Convert the test messages the same way and predict their labels.
6. Print accuracy and a classification report.
7. Try two new messages: a prize message and a meeting message.

## What the result means

- The dataset has **4,825 ham** and **747 spam** messages.
- Test accuracy is **0.9756**, so about 97.6% of test messages are classified correctly.
- Spam precision is **1.00**: every message the model called spam really was spam.
- Spam recall is **0.81**: the model catches about 81% of spam, so it misses about 19%.
- Ham recall is **1.00**: almost no normal message is wrongly marked as spam.
- The prize message is predicted **spam**; the meeting message is predicted **ham**.

The lower spam recall is the important detail. A spam filter that misses spam is less useful, even if overall accuracy looks high.

## Why these choices?

- TF-IDF turns text into numbers and downweights very common words.
- Multinomial Naive Bayes is fast and works well for word-based text.
- A 75/25 split gives enough test data while keeping most data for training.
- The classification report shows per-class performance, not just accuracy.

## If the examiner asks (plain answers)

**What is spam and ham?** Spam is junk; ham is normal mail.

**Why is accuracy not enough?** The classes are imbalanced, so a model that always says "ham" would already be about 87% accurate.

**What is precision?** Of the messages we called spam, how many really were spam.

**What is recall?** Of all the real spam, how many we caught.

**Why is spam recall only 0.81?** Some spam looks similar to normal messages, so the model misses it.

**What is Naive Bayes?** A fast probabilistic classifier that assumes words are independent given the class.

**How could we improve it?** Add n-grams, adjust the threshold, use class weights, or try an SVM.

**One-line takeaway:** A spam filter learns word weights from examples; judge it by spam recall and precision, not just overall accuracy.
