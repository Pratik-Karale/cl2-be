# Practical 5 — Randomized Benchmarking in Plain English

> **In one sentence:** We test how reliable a quantum gate set is by sending random sequences of gates and their undo through a noisy simulator, and watching how often the answer still comes back correct.

## The problem in everyday words

Real quantum computers make mistakes. A gate that should flip a qubit might do nothing, or do something slightly wrong. We want a simple way to measure the average quality of the gates, without testing every possible circuit.

Randomized benchmarking does this: build a random sequence of gates, then add the inverse sequence that should undo it. If the machine were perfect, the final answer would always be the starting state. Every mistake shows up as a wrong final answer. By making the sequence longer and longer, we see how quickly the success rate drops.

## What the main idea is, without jargon

Imagine testing a calculator by typing a random sum and then its exact reverse. If the calculator is perfect, you get back to the starting number. If it makes a small error at each step, longer chains of sums will drift further away.

In the quantum version:
- The gates are `H` and `S`, which are simple quantum operations.
- Their inverses are `H` and `Sdg`.
- A sequence like "H, S, H" is followed by "H, Sdg, H" so the ideal result is 0.
- A noise model adds a 2% chance of a random error to each gate.
- We count how often the final measurement is 0. That fraction is the **survival probability**.

## What the circuit does, step by step

1. Create a noise model with a 2% depolarizing error on `H`, `S`, and `Sdg`.
2. For each length (1, 2, 4, 8), repeat many times:
   - Choose a random sequence of `H` and `S`.
   - Apply the sequence, then apply its inverse in reverse order.
   - Measure the qubit.
   - Count a success if the result is 0.
3. Divide successes by the number of shots to get the survival probability.
4. Compare the survival probabilities across lengths.

## What the result means

The example run gave:

- Length 1: **0.97**
- Length 2: **0.96**
- Length 4: **0.92**
- Length 8: **0.88**

Shorter sequences survive more often. As the sequence gets longer, there are more chances for a gate error, so the final answer drifts away from 0 more often. The downward slope is the fingerprint of accumulated noise.

## Why these choices?

- **Random gates** average over many circuits, so one unlucky circuit does not dominate the result.
- **The inverse sequence** makes the ideal answer known (`0`), so any deviation is due to noise.
- **`H` and `S`** are Clifford gates, which are easy to invert and standard for RB.
- **A 2% depolarizing model** is a simple, controllable way to simulate realistic gate noise.
- **Several sequence lengths** let you see the trend rather than a single number.

## If the examiner asks (plain answers)

**What is randomized benchmarking?** A method to estimate the average error rate of a gate set using random sequences and their inverses.

**Why random sequences?** They prevent the result from depending on one special circuit and average out coherent errors.

**Why does survival fall with length?** Each gate adds a chance of error; longer sequences accumulate more errors.

**What is depolarizing noise?** A model where the qubit occasionally becomes a random state.

**What does survival probability mean?** The fraction of runs that return the expected 0.

**How do you get the error per gate?** Fit the survival curve and extract its decay rate.

**Does this test one specific gate?** No; standard RB gives an average. Interleaved RB can isolate a specific gate.

**Why seed the random generator?** So the same sequence is used each time, making comparisons reproducible.

**One-line takeaway:** send random gates plus their inverse through a noisy device; the faster the success rate falls with length, the higher the average gate error.
