"""Practical 1 - 16-qubit Random Number Generator.

Aim
    Put 16 qubits into an equal superposition with Hadamard gates and measure
    them. The measured 16-bit string is a hardware-random number.

Prints
    One random 16-bit string (0/1 per qubit) and its decimal value.

Qiskit components
    QuantumCircuit, Hadamard gate, measurement, AerSimulator, transpile.
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


def main() -> None:
    qc = QuantumCircuit(16, 16)

    # H on every qubit creates an equal superposition of all 2^16 bit strings.
    qc.h(range(16))
    qc.measure(range(16), range(16))

    sim = AerSimulator()
    # One shot = one random 16-bit sample.
    result = sim.run(transpile(qc, sim), shots=1).result()
    bitstring = list(result.get_counts())[0]

    # Qiskit may return the bits with spaces between registers.
    clean = bitstring.replace(" ", "")
    print("Random 16-bit number:", bitstring)
    print("As a 16-character bit string:", clean)
    print("Decimal value:", int(clean, 2))


if __name__ == "__main__":
    main()
