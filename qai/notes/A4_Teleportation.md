# Practical 4 — Quantum Teleportation (Viva Theory)

> **30-second answer:** Teleport the unknown state of qubit 0 to qubit 2 using a shared **Bell pair** and **two classical bits**. A Bell-basis measurement destroys the original state, and conditional `X`/`Z` corrections rebuild it on qubit 2. In the run, the teleported qubit is `0` about **77%** of the time, matching the original `Ry(1.0)` state.

## 1. MOST LIKELY — Core of the Experiment (High Yield)

**Aim:** Transfer an unknown one-qubit state from one qubit to another without moving the physical qubit.

**Circuit in five steps**
1. Prepare the unknown state on qubit 0 with `Ry(1.0)`.
2. Create a Bell pair on qubits 1 and 2: `H(1)`, then `CX(1,2)`.
3. Bell-basis measurement: `CX(0,1)`, `H(0)`, measure qubits 0 and 1 into two classical bits.
4. Feed-forward corrections on qubit 2: `X` if the second bit is 1; `Z` if the first bit is 1.
5. Measure qubit 2; it now holds the original state.

**Key Qiskit calls**
```python
qc = QuantumCircuit(3, 3)
qc.ry(1.0, 0)                 # unknown state
qc.h(1); qc.cx(1, 2)          # Bell pair
qc.cx(0, 1); qc.h(0)          # Bell-basis measurement
qc.measure(0, 0); qc.measure(1, 1)
with qc.if_test((qc.clbits[1], 1)): qc.x(2)
with qc.if_test((qc.clbits[0], 1)): qc.z(2)
qc.measure(2, 2)
```

**Expected output**
- Example counts: `{'000': 201, '011': 199, '010': 192, '001': 199, '101': 59, '110': 58, '111': 67, '100': 49}`.
- Qiskit prints the **highest classical bit first**, so the first character is the teleported qubit.
- First character `0`: 201 + 199 + 192 + 199 = **791/1024 ≈ 77%**. This matches `Ry(1.0)`, which has P(0) ≈ 0.77.
- The other two characters are the random Bell-measurement outcomes.

**Viva Q&A**
1. **What is quantum teleportation?** Transferring an unknown quantum state from one qubit to another using entanglement and classical communication.
2. **Does the physical qubit travel?** No; only the state is reconstructed at the destination.
3. **Why do we need a Bell pair?** Entanglement is the resource that links the source and destination.
4. **Why two classical bits?** The Bell measurement has four possible outcomes; two bits tell the receiver which corrections to apply.
5. **Does teleportation violate no-cloning?** No; the original state is destroyed by the measurement, so there is only one copy.
6. **Is it faster than light?** No; the receiver needs the two classical bits, which travel at or below light speed.
7. **What does `Ry(1.0)` prepare?** A superposition with P(0) ≈ 0.77 and P(1) ≈ 0.23.
8. **Why `X` and `Z` corrections?** `X` fixes a bit flip and `Z` fixes a phase flip, depending on the measurement outcome.
9. **Why is the first character the teleported qubit?** Qiskit orders bit strings from the highest classical bit to the lowest; clbit 2 is the teleported qubit.
10. **Can teleportation send a whole quantum computer?** It can move a state or a gate; building a network of teleported gates is a route to distributed quantum computing.
11. **What would happen without the corrections?** The destination would have the right state only for one of the four measurement outcomes.
12. **What is the role of the Bell measurement?** It entangles the unknown state with the resource and extracts the two bits needed for correction.

## 2. LIKELY — Syllabus Theory Around This Practical

### Unit I: Introduction to Quantum Computation
- **Bell states:** maximally entangled two-qubit states, e.g. `(|00> + |11>) / √2`.
- **Entanglement:** a joint state that cannot be factored into independent qubit states.
- **Measurement in different bases:** measuring in the Bell basis extracts joint information.
- **Quantum circuits:** gates, measurement, and classical feed-forward.

### Unit V: Quantum Information Processing
- **Quantum teleportation:** entanglement + two classical bits move a state.
- **Quantum dense coding:** one qubit can carry two classical bits when shared entanglement is available.
- **Quantum key distribution:** entanglement-based protocols detect eavesdropping.
- **Noise and error models:** real teleportation suffers from imperfect Bell pairs and gate errors.

**Likely Q&A**
- *What is a Bell state?* A maximally entangled pair of qubits.
- *What is the difference between entanglement and superposition?* Superposition is one system in several states; entanglement is a joint property of two or more systems.
- *Why does measurement destroy the original state?* Measurement collapses it; teleportation consumes the state to recreate it elsewhere.
- *What is a classical bit used for in teleportation?* It carries the correction instruction (bit flip / phase flip).
- *What is dense coding?* Using a shared entangled pair to send two classical bits by transmitting one qubit.
- *What is a quantum repeater?* A device that extends entanglement over long distances, important for teleportation networks.

## 3. LEAST LIKELY — Stretch / Edge Cases

- **Imperfect Bell pairs:** noisy entanglement lowers teleportation fidelity.
- **Classical communication delay:** teleportation is not instantaneous.
- **No-cloning:** you cannot keep a copy of the original state.
- **Gate errors:** conditional corrections can themselves fail on hardware.
- **Entanglement distillation:** purify noisy Bell pairs before teleporting.
- **Gate teleportation:** teleport a gate rather than a state, useful for fault-tolerant computing.
- **Relativistic causality:** the protocol respects it because the classical bits are required.

**If you remember only one thing:** a Bell pair plus two classical bits can move an unknown quantum state, but the original is destroyed and the classical bits are essential.
