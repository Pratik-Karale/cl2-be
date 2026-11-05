# Practical 3 — Tarrataca's 3-Puzzle in Plain English

> **Scope note:** A3 is uncertain per the faculty note; it is kept here for backup.

> **In one sentence:** We let the computer try every possible sequence of three moves at the same time, then amplify the one sequence that solves the puzzle.

## The problem in everyday words

A 3-puzzle is a tiny sliding puzzle: a 2×2 board with three tiles and one empty space. You can slide a tile into the empty space if it is next to it. The goal is to reach a particular arrangement.

A classical program would try one move sequence after another until it finds a solution. That is fine for a tiny puzzle, but it becomes slow when the number of possible sequences grows. The quantum version tries all sequences at once and then boosts the correct one.

## What the main idea is, without jargon

Imagine a giant room full of people, and each person holds a different three-move instruction sheet: "up, left, down", "right, right, up", and so on. You ask everyone to follow their sheet. Most end up at the wrong board. One person ends at the goal.

Instead of checking each person one by one, you use a quantum trick:
- Put all instruction sheets into a blur where every sheet is present at once.
- Use an **oracle** to put a mark on the sheets that reach the goal.
- Use **diffusion** to make the marked sheets stand out, like turning up the volume on the correct answer and turning down the rest.
- Repeat the mark-and-boost step a few times, then measure. The winning sheet is the most likely result.

This is Grover's search idea applied to a puzzle.

## What the circuit does, step by step

1. Define the start board, the goal board, and the four moves: up, down, left, right.
2. Encode each move in two bits, so three moves need six qubits.
3. Put all six qubits into a superposition, representing all 64 three-move sequences at once.
4. Build an oracle that flips the sign of every sequence that reaches the goal.
5. Build a diffusion step that amplifies the marked sequences.
6. Repeat oracle plus diffusion six times.
7. Measure the six qubits and decode the most frequent result into moves.

## What the result means

The script found exactly one solution among the 64 sequences. After six Grover rounds, the top measured result was `011100`, which appeared **1020 out of 1024** times in the example run. Decoded, that is **up, right, down**.

The fact that one answer dominates is the signature of Grover amplification. In a classical random search you would expect the correct sequence to appear only about once every 64 tries.

## Why these choices?

- **Three moves** are enough to solve this particular puzzle from the chosen start.
- **Two bits per move** represent the four possible directions.
- **Six qubits** give 64 sequences, which is small enough to simulate comfortably.
- **Grover's algorithm** is the natural quantum tool for searching an unstructured list of possibilities.
- **A classical check** is used only to build the oracle; the actual search is quantum.

## If the examiner asks (plain answers)

**What is a production system?** A set of states and rules that transform one state into another.

**What is the quantum part?** Searching over many rule sequences at once and amplifying the one that reaches the goal.

**Why six qubits?** Three moves times two bits per move.

**What does the oracle do?** It marks the correct sequences.

**What does diffusion do?** It makes the marked sequences more likely to be measured.

**Why repeat the oracle and diffusion?** Each round increases the correct answer's lead; too many rounds would overshoot.

**Could this solve a bigger puzzle?** Yes, but it needs more qubits and a deeper circuit; the current version only searches three-move sequences.

**Does it always find the answer?** It finds it with high probability; there is still a small chance of measuring something else.

**One-line takeaway:** encode many move sequences in qubits, mark the ones that solve the puzzle, and let Grover amplify the winner.
