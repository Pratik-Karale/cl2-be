# Practical 5 — Randomized Benchmarking Protocol (Viva Theory)

> **30-second answer:** Apply random Clifford sequences (`H`, `S`) of increasing length, append the inverse sequence so the ideal result is `0`, and run under a **2% depolarizing noise model**. The survival probability falls from **0.97** at length 1 to **0.88** at length 8, showing how gate errors accumulate.

## 1. MOST LIKELY — Core of the Experiment (High Yield)

**Aim:** Measure average gate error using the randomized benchmarking (RB) protocol.

**Protocol**
1. Build a random sequence of Clifford gates (`H` and `S`).
2. Append the inverse sequence (`H` undoes `H`; `Sdg` undoes `S`) so the ideal output is `|0>`.
3. Add a depolarizing error of 2% to every `H`, `S` and `Sdg` gate.
4. Run one shot and record whether the measurement is `0`.
5. Repeat for many shots and for sequence lengths 1, 2, 4, 8.
6. The survival probability should decrease with length; the decay rate estimates the average error per gate.

**Key Qiskit calls**
```python
from qiskit_aer.noise import NoiseModel, depolarizing_error
noise = NoiseModel()
noise.add_all_qubit_quantum_error(depolarizing_error(0.02, 1), ["h", "s", "sdg"])
sim = AerSimulator(noise_model=noise)
```

**Expected output**
- Length 1: survival **0.97**
- Length 2: survival **0.96**
- Length 4: survival **0.92**
- Length 8: survival **0.88**

The exact numbers vary slightly with the random seed and shots, but the downward trend is the point.

**Viva Q&A**
1. **What is randomized benchmarking?** A protocol that estimates the average error of a gate set by running random sequences and measuring how often the ideal output survives.
2. **Why random sequences?** Randomness averages out coherent errors and makes the result depend on the average gate error, not one special circuit.
3. **Why append the inverse?** The ideal final state is known (`0`), so any deviation is due to noise.
4. **Why does survival decrease with length?** Each gate adds a chance of error; longer sequences accumulate more errors.
5. **What is a depolarizing error?** With probability `p`, the qubit state is replaced by a completely mixed state; it is a simple noise model.
6. **Why use `H` and `S`?** They are Clifford gates, which are easy to invert and sufficient for a basic RB experiment.
7. **What does survival probability mean?** The fraction of shots that return the expected `0`.
8. **How do you estimate error per gate?** Fit the survival curve (usually an exponential) and extract the decay constant; the average error is related to the decay.
9. **Why 100 shots?** More shots reduce statistical uncertainty; 100 is enough for a classroom demonstration.
10. **What is the difference between RB and tomography?** RB gives an average error rate; tomography reconstructs the full process, which is much more expensive.
11. **Why seed the random generator?** To make the sequence reproducible for comparison.
12. **What does RB not capture?** It gives an average, not which specific gate or error type is responsible.

## 2. LIKELY — Syllabus Theory Around This Practical

### Unit II: Quantum Architecture
- **Noise and mixed states:** real devices are not perfectly isolated; errors are modeled by noisy channels.
- **Universal gate sets:** Clifford gates plus a non-Clifford gate (such as `T`) form a universal set.
- **Measurement:** readout errors add to gate errors.

### Unit V: Quantum Information Processing
- **Noise models:** bit flip, phase flip, depolarizing, amplitude damping.
- **Fault tolerance:** error rates must be below a threshold for error correction to help.
- **Benchmarking:** RB, interleaved RB, gate set tomography, process tomography.

**Likely Q&A**
- *What is a Clifford gate?* A gate that maps Pauli operators to Pauli operators; `H`, `S`, `X`, `Y`, `Z`, `CX` are examples.
- *Why is RB important?* It gives a hardware-independent estimate of average gate performance.
- *What is interleaved RB?* Insert the gate under test between random Clifford gates to estimate its specific error.
- *What is SPAM error?* State preparation and measurement error; RB is designed to be robust to it.
- *What is a noise model?* A mathematical description of how errors act on qubits.
- *What is the threshold theorem?* Below a certain physical error rate, error correction can make computation arbitrarily reliable.

## 3. LEAST LIKELY — Stretch / Edge Cases

- **Clifford-only limitation:** standard RB benchmarks Clifford gates; non-Clifford gates need interleaved RB.
- **SPAM sensitivity:** RB reduces but does not eliminate state-preparation and measurement errors.
- **Gate-dependent noise:** the average error may hide a bad gate.
- **Leakage:** qubits can leave the computational subspace, which simple RB does not model.
- **Scalability:** full RB on many qubits is expensive; simultaneous RB benchmarks many qubits at once.
- **Alternatives:** cross-entropy benchmarking (XEB), cycle benchmarking, gate set tomography.

**If you remember only one thing:** randomized benchmarking sends random gates plus their inverse through a noisy device and uses the survival probability to estimate average gate error.
