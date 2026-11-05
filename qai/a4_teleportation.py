"""Practical 4 - Quantum Teleportation.

Aim
    Teleport the state of qubit 0 to qubit 2 using one shared Bell pair
    (qubits 1 and 2) and two classical bits. No physical qubit travels; only
    the quantum state is reconstructed.

Prints
    Measurement counts for the teleported qubit. The output should mostly be
    the same as the original state (here Ry(1.0) prepares a biased state).

Qiskit components
    QuantumCircuit, Ry, H, CX, measurement, conditional if_test (feed-forward
    X and Z), AerSimulator, transpile.
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


def main() -> None:
    qc = QuantumCircuit(3, 3)

    # --- Prepare the unknown state on qubit 0.
    qc.ry(1.0, 0)

    # --- Create a Bell pair on qubits 1 and 2.
    qc.h(1)
    qc.cx(1, 2)

    # --- Bell-basis measurement of qubits 0 and 1.
    qc.cx(0, 1)
    qc.h(0)
    qc.measure(0, 0)
    qc.measure(1, 1)

    # --- Feed-forward corrections on qubit 2 using the two classical bits.
    with qc.if_test((qc.clbits[1], 1)):
        qc.x(2)
    with qc.if_test((qc.clbits[0], 1)):
        qc.z(2)

    qc.measure(2, 2)

    sim = AerSimulator()
    result = sim.run(transpile(qc, sim), shots=1024).result()
    counts = result.get_counts()
    print("Teleportation results:", counts)
    print("Interpretation: qubit 2 reproduces the original Ry(1.0) state.")


if __name__ == "__main__":
    main()
