"""Practical 6 - 5-qubit Quantum Fourier Transform (QFT).

Aim
    Prepare a simple 5-qubit input state, apply the QFT, and measure. The QFT
    maps computational-basis amplitudes into the Fourier (frequency) basis; it
    is the core of phase estimation, Shor's algorithm and many quantum
    algorithms.

Prints
    Measurement counts after the QFT.

Qiskit components
    QuantumCircuit, H, X, QFT library gate, measurement, AerSimulator,
    transpile.
"""

from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import QFTGate
from qiskit_aer import AerSimulator


def main() -> None:
    qc = QuantumCircuit(5, 5)

    # A simple input state: qubit 0 in |+>, qubit 1 in |1>.
    qc.h(0)
    qc.x(1)

    qc.append(QFTGate(5), range(5))
    qc.measure(range(5), range(5))

    sim = AerSimulator()
    result = sim.run(transpile(qc, sim), shots=1024).result()
    counts = result.get_counts()
    print("QFT results:", counts)
    print("Interpretation: the QFT turns the input pattern into frequency-domain outcomes.")


if __name__ == "__main__":
    main()
