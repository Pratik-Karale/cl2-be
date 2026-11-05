"""Practical 3 - Tarrataca's Quantum Production System for the 3-puzzle.

Scope note: this practical is marked uncertain in the faculty note; it is
kept here for backup.

Aim
    Model the 3-puzzle (2x2 board, 0 = blank) as a quantum production system.
    A sequence of DEPTH production rules is encoded in qubits; Hadamards put
    all rule sequences in superposition, an oracle marks the sequences that
    reach the goal, and Grover diffusion amplifies them.

Prints
    The marked basis states, the number of Grover iterations, the top
    measurement outcomes, and the decoded move sequence.

Qiskit components
    QuantumCircuit, Hadamard, X, multi-controlled Z (H + MCX + H), Grover
    diffusion, AerSimulator, transpile.
"""

import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

START, GOAL, DEPTH = (3, 1, 0, 2), (1, 2, 3, 0), 3   # board cells: [0 1 / 2 3]
NAMES, SHIFT = ["up", "down", "left", "right"], [-2, 2, -1, 1]


def apply(state, rule):
    """Apply one production rule; return None when the move is illegal."""
    blank = state.index(0)
    target = blank + SHIFT[rule]
    if not 0 <= target < 4 or (rule >= 2 and target // 2 != blank // 2):
        return None
    board = list(state)
    board[blank], board[target] = board[target], board[blank]
    return tuple(board)


def decode(k):
    """Turn a basis-state integer into DEPTH two-bit rule numbers."""
    return [(k >> (2 * i)) & 3 for i in range(DEPTH)]


def reaches_goal(k):
    state = START
    for rule in decode(k):
        state = apply(state, rule)
        if state is None:
            return False
    return state == GOAL


def main() -> None:
    n = 2 * DEPTH
    # Classical check used only to build the quantum oracle.
    marked = [k for k in range(2 ** n) if reaches_goal(k)]
    print("Solutions (basis states):", marked)

    # Oracle: phase-flip every marked basis state.
    oracle = QuantumCircuit(n)
    for k in marked:
        zeros = [i for i in range(n) if not (k >> i) & 1]
        if zeros:
            oracle.x(zeros)
        # Multi-controlled Z: H on the target, MCX, H again.
        oracle.h(n - 1)
        oracle.mcx(list(range(n - 1)), n - 1)
        oracle.h(n - 1)
        if zeros:
            oracle.x(zeros)

    # Diffusion: inversion about the mean.
    diffusion = QuantumCircuit(n)
    diffusion.h(range(n))
    diffusion.x(range(n))
    diffusion.h(n - 1)
    diffusion.mcx(list(range(n - 1)), n - 1)
    diffusion.h(n - 1)
    diffusion.x(range(n))
    diffusion.h(range(n))

    qc = QuantumCircuit(n)
    qc.h(range(n))                       # all rule sequences in superposition
    iterations = int(np.pi / 4 * np.sqrt(2 ** n / len(marked)))
    for _ in range(iterations):
        qc.compose(oracle, inplace=True)
        qc.compose(diffusion, inplace=True)
    qc.measure_all()

    sim = AerSimulator()
    counts = sim.run(transpile(qc, sim), shots=1024).result().get_counts()
    top = dict(sorted(counts.items(), key=lambda item: -item[1])[:3])
    best = max(counts, key=counts.get)

    print("Grover iterations:", iterations)
    print("Top results:", top)
    print("Solution moves:", [NAMES[rule] for rule in decode(int(best.replace(" ", ""), 2))])


if __name__ == "__main__":
    main()
