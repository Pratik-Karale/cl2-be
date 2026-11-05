# Practical 1 — 16-qubit Random Number Generator (Viva Theory)

> **30-second answer:** Put **16 qubits** into an equal superposition with Hadamard gates and measure them. The result is a random 16-bit string, uniformly distributed over all **2^16 = 65,536** possibilities. One example run produced `0000111101011101` = **3933**.

## 1. MOST LIKELY — Core of the Experiment (High Yield)

**Aim:** Generate a random 16-bit number using quantum superposition and measurement.

**Circuit:** 16 qubits, 16 classical bits. Apply `H` to every qubit, measure every qubit into its classical bit, run the circuit for **one shot** on `AerSimulator`.

**Key Qiskit calls**
```python
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(16, 16)
qc.h(range(16))               # equal superposition of all 2^16 bit strings
qc.measure(range(16), range(16))

sim = AerSimulator()
result = sim.run(transpile(qc, sim), shots=1).result()
bitstring = list(result.get_counts())[0]
```

**Expected output**
- One 16-character bit string, for example `0000111101011101`.
- Decimal value of that example: **3933**.
- Because the circuit is random, the exact string changes on every run; the **distribution** is uniform.

**Viva Q&A**
1. **What is a qubit?** A two-level quantum system that can be in a superposition of 0 and 1 until measured.
2. **What does the Hadamard gate do?** It turns `|0>` into an equal blend of `|0>` and `|1>`, so measuring gives 0 or 1 with equal probability.
3. **Why 16 qubits?** Sixteen independent bits give 2^16 = 65,536 possible outcomes.
4. **Why is the result random?** Quantum measurement is probabilistic; the circuit creates an equal superposition, so every bit string has the same chance.
5. **Is this pseudo-random like Python's `random`?** No. The randomness comes from quantum measurement, not a deterministic seed.
6. **What is a shot?** One execution of the circuit and one set of measurements. Here one shot gives one number.
7. **What is `transpile` doing?** It rewrites the circuit into the gate set of the chosen backend so it can run.
8. **Why use `AerSimulator`?** It simulates the circuit locally without an IBM account; real hardware would add noise.
9. **Can the same number appear twice?** Yes, by chance; each run is independent.
10. **How would you get a number in a smaller range?** Measure enough bits and discard or scale the result, but naive modulo introduces bias; use rejection sampling for a uniform range.
11. **What is the difference between a simulator and real hardware here?** The simulator is ideal and uniform; hardware has gate and measurement errors, so randomness tests are needed.
12. **What does the decimal conversion do?** It treats the 16-bit string as a binary number and converts it to base 10.

## 2. LIKELY — Syllabus Theory Around This Practical

### Unit I: Introduction to Quantum Computation
- **Qubit:** the quantum unit of information; state is a superposition of `|0>` and `|1>`.
- **Single-qubit gates:** `X` (bit flip), `Z` (phase flip), `H` (superposition), `S`/`T` (phase gates), rotations.
- **Measurement:** collapses the state to a basis state; the computational basis is `|0>` and `|1>`.
- **Quantum circuit:** gates applied left to right, then measurement.
- **Bell states and teleportation:** entanglement-based examples of multi-qubit circuits.

### Unit II: Quantum Architecture
- **State of a quantum system:** a vector of amplitudes; probabilities come from squared magnitudes.
- **Composite systems:** tensor products of qubit states.
- **Universal gate sets:** a small set of gates can approximate any quantum operation.
- **Entanglement:** a joint state that cannot be written as independent qubit states.

**Likely Q&A**
- *What is superposition?* A state that is a combination of basis states until measured.
- *What is a basis?* A set of mutually exclusive outcomes; the computational basis is 0 and 1.
- *Why does measurement change the state?* The state collapses to the observed outcome.
- *What is a classical bit vs a qubit?* A bit is 0 or 1; a qubit can be in a superposition and can be entangled.
- *What is a quantum random number generator used for?* Cryptography, simulations, lotteries, and any application needing unpredictable randomness.

## 3. LEAST LIKELY — Stretch / Edge Cases

- **Bias:** real hardware may not produce perfectly uniform bits; test with statistical tests.
- **Entropy source:** a quantum RNG is only as good as its measurement and post-processing.
- **Shot independence:** repeated shots should be independent; correlated noise can break this.
- **Post-processing:** hashing or whitening can remove residual bias.
- **Scaling:** more qubits mean more possible values, but hardware connectivity and readout errors grow.
- **Alternative:** use QRNG APIs or hardware modules when a certified source is required.

**If you remember only one thing:** 16 Hadamards create all 65,536 bit strings at once, and one measurement picks one random 16-bit number.
