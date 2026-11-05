"""Practical 2 - Tackle Noise with Error Correction (3-qubit bit-flip code).

Aim
    Encode one logical qubit into three physical qubits, inject a bit-flip
    error on the middle qubit, detect the error with two ancilla qubits, and
    correct it conditionally.

Prints
    Measurement counts for the corrected logical qubit (the '0' outcome should
    dominate when the correction works).

Qiskit components
    QuantumCircuit, Ry, CX, X, conditional if_test, measurement, AerSimulator,
    transpile.
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


def main() -> None:
    qc = QuantumCircuit(5, 3)

    # --- Encode: one logical qubit -> three physical qubits (|000> + |111> part)
    qc.ry(1.0, 0)
    qc.cx(0, 1)
    qc.cx(0, 2)

    # --- Inject a bit-flip error on qubit 1
    qc.x(1)

    # --- Detect: two ancilla qubits measure the parity of neighbouring pairs
    qc.cx(0, 3)
    qc.cx(1, 3)
    qc.cx(0, 4)
    qc.cx(2, 4)

    qc.measure(3, 0)
    qc.measure(4, 1)

    # --- Correct: the syndrome tells us which qubit flipped
    with qc.if_test((qc.clbits[0], 1)):
        with qc.if_test((qc.clbits[1], 0)):
            qc.x(1)

    with qc.if_test((qc.clbits[0], 0)):
        with qc.if_test((qc.clbits[1], 1)):
            qc.x(2)

    with qc.if_test((qc.clbits[0], 1)):
        with qc.if_test((qc.clbits[1], 1)):
            qc.x(0)

    qc.measure(0, 2)

    sim = AerSimulator()
    result = sim.run(transpile(qc, sim), shots=1024).result()
    counts = result.get_counts()
    print("Error correction results:", counts)
    print("Interpretation: the corrected logical qubit is mostly measured as 0.")


if __name__ == "__main__":
    main()
