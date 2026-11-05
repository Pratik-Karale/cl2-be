"""Practical 5 - Randomized Benchmarking Protocol.

Aim
    Measure how quickly gate errors accumulate. For each sequence length, build
    a random sequence of Clifford gates (H and S), append the inverse sequence
    (so the ideal result is |0>), run it under a depolarizing noise model, and
    record how often the final measurement is still 0.

Prints
    Survival probability for sequence lengths 1, 2, 4 and 8. Survival should
    fall as the sequence gets longer.

Qiskit components
    QuantumCircuit, H, S, Sdg, measurement, AerSimulator, NoiseModel,
    depolarizing_error, transpile.
"""

import random

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error


def main() -> None:
    random.seed(42)                 # reproducible random gate sequences

    noise = NoiseModel()
    error = depolarizing_error(0.02, 1)
    noise.add_all_qubit_quantum_error(error, ["h", "s", "sdg"])
    sim = AerSimulator(noise_model=noise)

    shots = 100
    for length in [1, 2, 4, 8]:
        successes = 0
        for _ in range(shots):
            gates = [random.choice(["h", "s"]) for _ in range(length)]
            qc = QuantumCircuit(1, 1)

            for gate in gates:
                getattr(qc, gate)(0)
            for gate in reversed(gates):        # inverse sequence
                inverse = "h" if gate == "h" else "sdg"
                getattr(qc, inverse)(0)

            qc.measure(0, 0)
            result = sim.run(transpile(qc, sim, optimization_level=0), shots=1).result()
            if result.get_counts().get("0", 0) == 1:
                successes += 1

        print(f"Length {length}: Survival = {successes / shots:.2f}")


if __name__ == "__main__":
    main()
