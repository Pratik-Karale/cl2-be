# Quantum AI Concepts — Quick Cheat Sheet
### Qiskit + Aer, no math required

> Use this to understand what each practical is doing and to answer viva questions in plain words. No LaTeX, no images.

---

## 0. The 30-second picture

A classical bit is 0 or 1. A **qubit** can be in a superposition of 0 and 1, can be **entangled** with other qubits, and collapses to one outcome when **measured**. A **quantum circuit** is a sequence of gates on qubits, ending with measurements. **Shots** are repeated runs; the result is a count of how often each bitstring appeared.

| Idea | Plain meaning |
|---|---|
| Qubit | A two-state quantum system |
| Superposition | Amplitudes on both 0 and 1 |
| Entanglement | Two qubits behave as one joint system |
| Measurement | Collapses the state and returns a classical bit |
| Gate | An operation that changes the qubit state |
| Circuit | Gates + measurements on qubits |
| Shots | Number of repeated runs |
| Simulator | A classical program that imitates a quantum computer |

---

## 1. Gates used in the practicals

| Gate | Qiskit call | Plain meaning |
|---|---|---|
| Hadamard | `qc.h(q)` | Puts a definite qubit into an equal superposition |
| Pauli-X | `qc.x(q)` | Bit flip: 0 ↔ 1 |
| Pauli-Z | `qc.z(q)` | Phase flip; changes the sign of the 1 part |
| S gate | `qc.s(q)` | 90° phase rotation |
| T gate | `qc.t(q)` | 45° phase rotation |
| Y rotation | `qc.ry(angle, q)` | Rotates the qubit by a chosen angle |
| CNOT | `qc.cx(control, target)` | Flips the target when the control is 1; creates entanglement |
| Toffoli / MCX | `qc.mcx(controls, target)` | Flips the target only when all controls are 1 |
| QFT | `QFT(n)` | Quantum Fourier transform on n qubits |

**Rule of thumb:** H creates spread, X flips, Z changes phase, CNOT links qubits, measurement reads them.

---

## 2. Circuit anatomy

```python
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 2)     # 2 qubits, 2 classical bits
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

sim = AerSimulator()
result = sim.run(transpile(qc, sim), shots=1024).result()
print(result.get_counts())
```

- Qubits hold quantum states; classical bits hold measurement results.
- `transpile` adapts the circuit to the simulator's gate set.
- `shots` controls how many times the circuit is run.
- `get_counts()` returns a dictionary like `{"00": 512, "11": 512}`.

**Qiskit bit order:** the rightmost bit is qubit 0 (little-endian). Read bitstrings carefully.

---

## 3. The six practicals in plain words

### A1 — 16-qubit random number generator

Apply H to all 16 qubits, then measure. Each qubit gives 0 or 1 with equal probability, so the 16-bit result is random. One shot gives one 16-bit number.

**Viva line:** "Hadamards create an equal superposition of all 2^16 bitstrings; measurement collapses it to one random bitstring."

### A2 — 3-qubit bit-flip error correction

Encode one logical qubit into three physical qubits: `a|0> + b|1>` becomes `a|000> + b|111>`. If one qubit flips, the other two still agree; two ancilla measurements give a **syndrome** that identifies the flipped qubit, and a conditional X corrects it.

**Viva line:** "The three-qubit code uses majority voting; the syndrome tells us which qubit flipped, and a conditional gate fixes it."

### A3 — Tarrataca's quantum production system (3-puzzle)

The 3-puzzle is a 2×2 board with one blank. A move is a rule: up, down, left or right. The circuit puts all rule sequences of a fixed depth into superposition, uses an oracle to mark sequences that reach the goal, and Grover diffusion amplifies them.

**Viva line:** "It is Grover search over possible move sequences: the oracle recognizes a solved puzzle and diffusion amplifies the solution."

### A4 — Quantum teleportation

A Bell pair is shared between the sender and receiver. The sender performs a Bell measurement on the state to send and their half of the pair, obtaining two classical bits. The receiver applies X and/or Z depending on those bits and recovers the state.

**Viva line:** "Teleportation sends the quantum state, not the physical qubit; two classical bits tell the receiver which correction to apply."

### A5 — Randomized benchmarking

Apply a random sequence of gates, then the inverse sequence. If the gates were perfect, the qubit returns to its starting state. Noise makes the survival probability fall as the sequence grows. Repeating for different lengths estimates the average gate error.

**Viva line:** "Random gates plus their inverse should return to the start; the decay of the survival probability measures noise."

### A6 — 5-qubit quantum Fourier transform

Prepare a state, apply QFT, and measure. QFT maps computational-basis states to Fourier-basis states; it is built from Hadamards, controlled phase rotations and swaps. It is the key ingredient in phase estimation and Shor's algorithm.

**Viva line:** "QFT is the quantum version of the Fourier transform; it turns phase information into measurable bit patterns."

---

## 4. Noise and simulators

| Term | Meaning |
|---|---|
| AerSimulator | Local classical simulator of quantum circuits |
| Noise model | A rule that adds errors to gates/measurements |
| Depolarizing error | With some probability, replace the state with a mixed state |
| Bit-flip error | Flip 0 ↔ 1 |
| Phase-flip error | Change the sign of the 1 part |
| Amplitude damping | Energy loss toward the ground state |
| NISQ | Noisy Intermediate-Scale Quantum: current limited hardware |

**Important:** `AerSimulator()` without a noise model is ideal. A5 explicitly adds depolarizing noise.

---

## 5. Common viva questions

| Question | Plain answer |
|---|---|
| What is a qubit? | A two-state quantum system that can be in superposition. |
| What does a Hadamard gate do? | Creates an equal superposition of 0 and 1. |
| What is entanglement? | A joint state that cannot be split into independent qubit states. |
| What does CNOT do? | Flips the target when the control is 1; creates entanglement. |
| What happens on measurement? | The state collapses to one basis state and returns a classical bit. |
| What are shots? | Repeated runs used to estimate the probability distribution. |
| Why transpile? | To rewrite the circuit for the simulator/backend gate set. |
| What is a Bell state? | A maximally entangled pair, such as `(|00> + |11>)/sqrt(2)`. |
| How does teleportation work? | Bell pair + Bell measurement + two classical bits + conditional X/Z. |
| Does teleportation copy the state? | No; the original is destroyed. |
| What is a syndrome? | The ancilla measurement pattern that identifies an error. |
| What is the 3-qubit code? | Majority-vote encoding that corrects one bit flip. |
| What is QFT used for? | Phase estimation, period finding and Shor's algorithm. |
| How does Grover work? | Oracle marks the solution; diffusion amplifies it; about sqrt(N) iterations. |
| What is randomized benchmarking? | A noise-estimation method using random gates and their inverse. |
| Simulator vs real hardware? | Aer is a classical simulation; hardware has real noise and limited connectivity. |
| What is NISQ? | The current era of noisy, medium-sized quantum devices. |

---

## 6. Traps examiners love

| Trap | Correct answer |
|---|---|
| "Superposition means the qubit is both 0 and 1 at once." | It has amplitudes for both; measurement gives one outcome. |
| "Measurement can be undone." | Measurement collapses the state; it is not reversible. |
| "More shots change the circuit." | Shots only improve the estimate of the same distribution. |
| "Noise is always present in Aer." | Only when you pass a noise model. |
| "Grover needs N iterations." | About sqrt(N) iterations; too many reduces success. |
| "Teleportation copies the qubit." | The original is destroyed; no-cloning prevents copying. |
| "CNOT is a classical XOR." | It is a quantum gate that can create entanglement. |
| "QFT is the same as a classical FFT." | It acts on quantum amplitudes and is reversible. |
| "A simulator proves hardware performance." | It ignores real device noise and connectivity. |

---

## 7. Last-minute "say this" lines

- **RNG:** "Hadamards on all qubits create a uniform superposition; one measurement gives a random bitstring."
- **Error correction:** "Encode in three qubits, measure the syndrome, and apply the correction."
- **Tarrataca:** "Grover search over move sequences; the oracle marks solved puzzles."
- **Teleportation:** "A Bell pair and two classical bits transfer the state; the original is destroyed."
- **Randomized benchmarking:** "Random gates plus their inverse should return to the start; noise makes the survival probability decay."
- **QFT:** "Hadamards, controlled phase rotations and swaps; it converts phase information into measurable bits."
