# Practical 6 — 5-qubit Quantum Fourier Transform (Viva Theory)

> **30-second answer:** Prepare a simple 5-qubit input (`H` on qubit 0, `X` on qubit 1), apply the **Quantum Fourier Transform**, and measure. The QFT maps the computational-basis amplitudes into the frequency basis; the measurement is spread across many 5-bit outcomes.

## 1. MOST LIKELY — Core of the Experiment (High Yield)

**Aim:** Implement and observe the 5-qubit Quantum Fourier Transform in Qiskit.

**Circuit**
1. Prepare an input state: `H(0)` puts qubit 0 in a superposition; `X(1)` sets qubit 1 to `|1>`.
2. Apply `QFTGate(5)` to all five qubits.
3. Measure all five qubits and run 1024 shots.

**Key Qiskit calls**
```python
from qiskit.circuit.library import QFTGate

qc = QuantumCircuit(5, 5)
qc.h(0)
qc.x(1)
qc.append(QFTGate(5), range(5))
qc.measure(range(5), range(5))
```

**Expected output**
- The counts are spread over many 5-bit strings, for example `{'00000': 73, '11110': 58, ...}`.
- There is no single dominant answer because the QFT converts the input pattern into a **frequency-domain** distribution.
- The exact counts vary per run; the spread and symmetry matter more than one number.

**Viva Q&A**
1. **What is the Quantum Fourier Transform?** The quantum analogue of the discrete Fourier transform; it maps computational-basis amplitudes to frequency-basis amplitudes.
2. **What does it do geometrically?** It changes the basis by applying phase rotations and Hadamards, revealing periodic structure.
3. **Why five qubits?** Five qubits give 2^5 = 32 amplitudes, enough to see the transform on a small register.
4. **What input state is used?** `H` on qubit 0 and `X` on qubit 1; a simple state that produces a visible spread.
5. **Why is the output spread out?** The QFT distributes amplitude across frequencies; measuring collapses it to one sample.
6. **What is the inverse QFT used for?** Reading out phases in phase estimation and Shor's algorithm.
7. **Where is the QFT used?** Phase estimation, order finding, Shor's factoring algorithm, period finding, and quantum simulations.
8. **How does QFT differ from the classical DFT?** It acts on quantum amplitudes in superposition and can be exponentially more compact; the classical DFT processes an explicit vector.
9. **What is the gate cost?** The standard QFT uses about `n²` gates for `n` qubits (Hadamards plus controlled phase rotations).
10. **Why measure after the QFT?** Measurement gives a sample from the frequency distribution; repeated shots estimate the distribution.
11. **What is the role of controlled phase gates?** They encode the relative phases that represent frequency components.
12. **Can you see the full Fourier spectrum in one shot?** No; one measurement gives one outcome, so you need many shots to estimate the distribution.

## 2. LIKELY — Syllabus Theory Around This Practical

### Unit II: Quantum Architecture and the QFT
- **Quantum Fourier Transform:** the core transform behind phase estimation and factoring.
- **Phase estimation:** estimates the eigenvalue phase of a unitary operator.
- **Order finding and factoring:** Shor's algorithm reduces factoring to order finding, which uses phase estimation and the QFT.
- **Period finding:** the QFT reveals periodicity in a superposition.
- **Hidden subgroup problem:** a general framework for many quantum algorithms.

### Unit III: Quantum Algorithms
- **Deutsch–Jozsa, Simon, Shor, Grover:** the standard quantum algorithm family.
- **Interference:** the QFT is built from Hadamards and phase gates that create constructive and destructive interference.

**Likely Q&A**
- *What is phase estimation?* A procedure that estimates the phase of a unitary's eigenvalue using the QFT.
- *Why is the QFT central to Shor's algorithm?* It converts periodic information into measurable frequency peaks.
- *What is a controlled phase gate?* A two-qubit gate that adds a phase to the target only when the control is 1.
- *What is the difference between QFT and Hadamard transform?* The Hadamard transform is the 1-qubit case; the QFT adds controlled phase rotations between qubits.
- *What is period finding?* Finding the repeating period of a function; the QFT turns the period into a frequency.
- *Why is the QFT not a full speedup by itself?* Reading the output and preparing useful input states are part of the algorithm; the QFT is one component.

## 3. LEAST LIKELY — Stretch / Edge Cases

- **Approximate QFT:** dropping small phase rotations reduces gate count with little loss.
- **Gate depth:** the standard QFT is `O(n²)` gates; on hardware, connectivity and noise limit the usable size.
- **Inverse QFT:** used to uncompute phases in phase estimation.
- **Measurement collapse:** one shot gives one sample; the full spectrum needs many shots.
- **QFT vs classical FFT:** the quantum version acts on amplitudes, not on an explicit data array; the speedup depends on the surrounding algorithm.
- **Hardware noise:** phase errors degrade the interference pattern; error mitigation and fault tolerance are needed.

**If you remember only one thing:** the QFT is a basis change that turns hidden periodicity into measurable frequency peaks, and it is the engine behind phase estimation and Shor's algorithm.
