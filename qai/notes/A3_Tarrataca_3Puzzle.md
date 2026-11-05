# Practical 3 — Tarrataca's Quantum Production System for the 3-Puzzle (Viva Theory)

> **Scope note:** A3 is uncertain per the faculty note; it is kept here for backup.

> **30-second answer:** Encode a sequence of **three moves** in **six qubits** (two bits per move), put all 64 move sequences in superposition, mark the sequences that solve the 3-puzzle with a Grover oracle, and amplify them with diffusion. There is **one solution** (basis state **28**); after **6 Grover iterations**, the top outcome is `011100` with **1020/1024** shots, decoding to **up → right → down**.

## 1. MOST LIKELY — Core of the Experiment (High Yield)

**Aim:** Implement Tarrataca's quantum production system for the 3-puzzle: search over production-rule sequences with Grover's algorithm.

**Problem encoding**
- Board cells are numbered `[0 1 / 2 3]`; `0` is the blank.
- Start state: `(3, 1, 0, 2)`; goal state: `(1, 2, 3, 0)`.
- Four production rules: `0 = up`, `1 = down`, `2 = left`, `3 = right`.
- Depth = 3 moves, so `3 × 2 = 6` qubits encode 64 possible sequences.

**Algorithm**
1. Apply `H` to all 6 qubits: every rule sequence is represented at once.
2. **Oracle:** phase-flip each basis state that reaches the goal. The script finds these solutions classically to build the oracle.
3. **Diffusion:** invert about the mean to amplify the marked states.
4. Repeat oracle + diffusion `π/4 × √(64/1) ≈ 6` times.
5. Measure; the most frequent bit string is the solution.

**Key Qiskit calls**
```python
qc = QuantumCircuit(6)
qc.h(range(6))                      # all rule sequences in superposition
for _ in range(6):
    qc.compose(oracle, inplace=True)
    qc.compose(diffusion, inplace=True)
qc.measure_all()
counts = AerSimulator().run(transpile(qc, sim), shots=1024).result().get_counts()
```

**Expected output**
- Solutions (basis states): `[28]` — exactly one valid sequence.
- Grover iterations: **6**.
- Top result: `{'011100': 1020, ...}` — the solution dominates.
- Decoded moves: **up, right, down**.

**Viva Q&A**
1. **What is a production system?** A set of states and rules that transform one state into another; it is a model of problem solving.
2. **What is Tarrataca's quantum production system?** A quantum search over rule sequences, using superposition and Grover amplification to find a sequence that reaches the goal.
3. **Why six qubits?** Three moves × two bits per move = six qubits, giving 64 possible sequences.
4. **Why two bits per move?** Four rules need four codes, and two classical bits can represent 0–3.
5. **What does the oracle do?** It flips the phase of the basis states that correspond to valid solutions.
6. **What does diffusion do?** It increases the amplitude of the marked states and decreases the others.
7. **Why six iterations?** Grover's optimal count is about `π/4 × √(N/M)`, with `N = 64` and `M = 1`, which rounds to 6.
8. **How is the board state updated?** `apply(state, rule)` swaps the blank with the neighbouring cell if the move is legal.
9. **Why is a classical check used?** The script checks all 64 sequences classically only to build the oracle; the search itself runs on the quantum circuit.
10. **What are the decoded moves?** `up`, `right`, `down`.
11. **What happens if the solution needs more than three moves?** The encoding depth must be increased; this circuit only searches sequences of length 3.
12. **Does the circuit prove a speedup?** It demonstrates the search pattern; a real speedup claim needs a careful scaling and resource analysis.

## 2. LIKELY — Syllabus Theory Around This Practical

### Unit VI: Quantum Problem Solving & AI Applications
- **Heuristic search:** use a heuristic to guide the search for a goal.
- **Quantum tree search:** explore many branches in superposition.
- **Quantum production system:** encode rules and states as quantum basis states; search over rule sequences.
- **Tarrataca's model:** applies quantum search to production-system planning.
- **Quantum walks:** a quantum analogue of a random walk on a graph, useful for search and graph problems.

### Unit III: Quantum Algorithms
- **Grover's algorithm:** searches an unstructured space of `N` items in about `√N` steps.
- **Oracle:** a circuit that recognizes solutions.
- **Amplitude amplification:** the general technique behind Grover diffusion.

**Likely Q&A**
- *What is Grover's algorithm used for?* Unstructured search and amplitude amplification.
- *What is the oracle in Grover's algorithm?* A black-box circuit that marks the correct answer.
- *Why does Grover need repeated iterations?* Each iteration increases the solution's amplitude; too many iterations overshoot.
- *What is a quantum walk?* A walk on a graph where the walker has quantum amplitudes; it can spread quadratically faster than a classical walk.
- *What is the difference between classical and quantum search?* Classical search checks items one by one; Grover examines all items through superposition and amplifies the answer.
- *What is the role of interference?* Diffusion uses constructive interference for the solution and destructive interference for the rest.

## 3. LEAST LIKELY — Stretch / Edge Cases

- **Depth limitation:** the circuit only finds solutions within the encoded number of moves.
- **Multiple solutions:** the iteration count changes; too many iterations can reduce success.
- **Oracle cost:** building a reversible oracle for a real puzzle can dominate the circuit size.
- **Scalability:** qubit count grows with depth; real hardware limits the usable depth.
- **Alternative:** classical BFS/DFS is often simpler for tiny puzzles; the quantum version is a proof of concept.
- **Noise:** on real hardware, Grover amplification degrades; error mitigation helps.

**If you remember only one thing:** encode move sequences in qubits, mark the ones that solve the puzzle, and let Grover amplify the winning sequence.
