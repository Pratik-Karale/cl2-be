# Practical 2 — Tackle Noise with Error Correction (Viva Theory)

> **30-second answer:** Encode one logical qubit into **three physical qubits**, inject a bit-flip on the middle qubit, detect the error with **two ancilla parity checks**, and correct it with conditional `X` gates. The corrected qubit keeps the original state: about **77% zeros**, matching the `Ry(1.0)` preparation.

## 1. MOST LIKELY — Core of the Experiment (High Yield)

**Aim:** Demonstrate the 3-qubit bit-flip repetition code: encode, detect a single bit flip, and correct it.

**Circuit in five steps**
1. **Encode:** `Ry(1.0)` prepares a logical state on qubit 0; `CX(0,1)` and `CX(0,2)` copy it into a 3-qubit repetition code.
2. **Error:** `X(1)` flips the middle physical qubit.
3. **Detect:** two ancillas measure parity: ancilla 3 checks qubits 0 and 1; ancilla 4 checks qubits 0 and 2.
4. **Correct:** conditional `X` gates use the two syndrome bits to flip the qubit that changed.
5. **Measure:** read the corrected logical qubit.

**Key Qiskit calls**
```python
qc = QuantumCircuit(5, 3)
qc.ry(1.0, 0); qc.cx(0, 1); qc.cx(0, 2)   # encode
qc.x(1)                                    # inject a bit-flip
qc.cx(0, 3); qc.cx(1, 3)                   # syndrome 1
qc.cx(0, 4); qc.cx(2, 4)                   # syndrome 2
qc.measure(3, 0); qc.measure(4, 1)
with qc.if_test((qc.clbits[0], 1)):
    with qc.if_test((qc.clbits[1], 0)):
        qc.x(1)                            # correct qubit 1
qc.measure(0, 2)
```

**Expected output**
- Example run: `{'001': 771, '101': 253}`.
- The **first character** is the corrected logical qubit in Qiskit's display order (highest classical bit first). About **771/1024 = 75%** are `0`, and **253/1024 = 25%** are `1`.
- This matches `Ry(1.0)`: the original state has P(0) ≈ 0.77 and P(1) ≈ 0.23. The correction preserved the state instead of forcing it to a fixed value.

**Viva Q&A**
1. **Why three qubits?** The repetition code uses three physical qubits to protect one logical qubit; a majority vote can correct one bit flip.
2. **What is a syndrome?** A parity measurement that tells you *which* qubit changed, without revealing the encoded value.
3. **Why ancilla qubits?** They measure parity without directly measuring (and collapsing) the data qubits.
4. **Why conditional `X` gates?** The syndrome selects the qubit to flip back.
5. **Why is the output not 100% zero?** The logical state is a superposition, not a fixed `|0>`; the code preserves its 77/23 probabilities.
6. **Which errors can this code correct?** A single bit-flip (`X`); it cannot correct a phase flip (`Z`) or two simultaneous bit flips.
7. **What is a logical qubit?** A qubit encoded across several physical qubits so that errors can be detected and corrected.
8. **Bit flip vs phase flip?** A bit flip changes 0↔1 (`X`); a phase flip changes the sign of the `|1>` part (`Z`).
9. **What is fault tolerance?** Designing operations so that errors do not spread uncontrollably through the encoded circuit.
10. **Why simulate?** `AerSimulator` lets us test the correction logic without hardware noise; real devices add more error types.
11. **What happens if two qubits flip?** The syndrome becomes ambiguous and the code may "correct" the wrong qubit.
12. **What is the threshold theorem?** If the physical error rate is below a threshold, arbitrarily reliable quantum computation is possible with enough error correction.

## 2. LIKELY — Syllabus Theory Around This Practical

### Unit V: Quantum Information Processing
- **Classical error correction:** encode redundant bits, recover by majority vote; the classical 3-bit code corrects one bit flip.
- **Error model:** bit flips, phase flips, depolarizing noise, measurement errors.
- **Quantum error correction:** no-cloning prevents simple copying; encoding uses entanglement and parity checks.
- **Fault tolerance:** error-corrected gates and circuits that keep errors from spreading.
- **Quantum teleportation and dense coding:** other uses of entanglement.
- **QKD:** quantum key distribution detects eavesdropping through disturbance.

**Likely Q&A**
- *Why can't we copy a qubit?* The no-cloning theorem forbids making an exact copy of an unknown quantum state.
- *What is the difference between detection and correction?* Detection identifies an error; correction reverses it.
- *What is a stabilizer code?* A code defined by parity-check operators whose measurement gives the syndrome (the 3-qubit code is a simple stabilizer code).
- *What is a depolarizing channel?* With some probability, the state is replaced by a random Pauli error.
- *What is the surface code?* A practical 2-D topological code with high threshold and local checks.
- *Why is error correction harder for quantum states?* Measurement collapses the state, and unknown states cannot be copied.

## 3. LEAST LIKELY — Stretch / Edge Cases

- **Phase-flip code:** use `H` to convert phase flips into bit flips, then reuse the same repetition idea.
- **Shor code:** concatenates bit-flip and phase-flip codes to correct both.
- **Steane code:** a 7-qubit CSS code that corrects one arbitrary single-qubit error.
- **Ancilla errors:** a faulty ancilla can produce a wrong syndrome; fault-tolerant circuits must handle this.
- **Multiple errors:** the simple repetition code fails for two flips; larger distance codes are needed.
- **Hardware reality:** readout errors and correlated noise require calibration and flags.

**If you remember only one thing:** the 3-qubit code measures parity to find which qubit flipped, then flips it back, preserving the original superposition.
