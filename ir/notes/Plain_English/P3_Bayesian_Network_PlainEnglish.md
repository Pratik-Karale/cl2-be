# Practical 3 — Bayesian Network in Plain English

> **In one sentence:** We build a probability map from heart-disease data and use it to estimate a patient's risk from their symptoms and risk factors.

## The problem in everyday words

A doctor sees a patient's age, sex, cholesterol, blood pressure and symptoms. No single sign proves heart disease. The doctor combines them into a risk estimate. We want a computer to do the same from data.

## What the main idea is, without jargon

Imagine a map of influences:

- Age, sex, cholesterol and blood pressure can influence heart disease.
- Heart disease can influence chest pain, exercise angina and maximum heart rate.

A **Bayesian network** is that map plus a table of probabilities at every arrow. When you tell it a patient's values, it updates the probabilities and gives you a risk.

Think of it as a chain of "if this, then how likely is that?" questions, combined mathematically.

## What the code does, step by step

1. Load the heart-disease CSV.
2. Clean the column names and turn text values into numbers.
3. Make the disease column binary: 0 = no disease, 1 = disease.
4. Keep the useful columns and drop rows with missing values.
5. Turn continuous values (age, cholesterol, blood pressure, heart rate) into low/medium/high groups.
6. Define the arrows: risk factors → heart disease → symptoms.
7. Learn the probability tables from the 675 remaining records.
8. Ask the model for the probability of heart disease for two example patients.

## What the result means

- The older male with chest pain and exercise angina has **P(heart disease) = 0.99**.
- The young female with no symptoms has **P(heart disease) = 0.01**.

These are probabilities from the data, not medical diagnoses. The model is saying that the first pattern looks very much like the disease cases it has seen, and the second looks very unlike them.

## Why these choices?

- The graph structure encodes common medical sense: risk factors come before disease, and symptoms follow it.
- Discretising continuous values keeps the probability tables small and understandable.
- Dropping missing rows avoids inventing data.
- Two contrasting patients make the inference easy to see.

## If the examiner asks (plain answers)

**What is a Bayesian network?** A graph of variables with probability tables on the arrows.

**What is a prior?** The probability before seeing the patient's details.

**What is evidence?** The patient's known values.

**What is a posterior?** The updated probability after using the evidence.

**What does the arrow mean?** The arrow points from a cause or influence to its effect.

**Why turn numbers into groups?** The network works with a finite set of states; groups make the tables manageable.

**Does this prove causation?** No, it shows statistical association in this dataset.

**One-line takeaway:** A Bayesian network is a probability map; you feed it evidence and it updates the chance of the outcome.
