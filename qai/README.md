# Quantum AI — 417523A

Six runnable Qiskit practicals. Run from the repository root:

```bash
python qai/a1_rng_16qubit.py
python qai/a2_error_correction.py
python qai/a3_tarrataca_3puzzle.py
python qai/a4_teleportation.py
python qai/a5_randomized_benchmarking.py
python qai/a6_qft_5qubit.py
```

| Script | What it demonstrates |
|---|---|
| `a1_rng_16qubit.py` | Hadamards on 16 qubits → measurement → random 16-bit number |
| `a2_error_correction.py` | 3-qubit bit-flip code, ancilla syndrome detection and correction |
| `a3_tarrataca_3puzzle.py` | Tarrataca quantum production system, Grover search over rule sequences |
| `a4_teleportation.py` | Bell pair + conditional X/Z → quantum teleportation |
| `a5_randomized_benchmarking.py` | Random gate sequences, inversion, survival probability under noise |
| `a6_qft_5qubit.py` | 5-qubit quantum Fourier transform on a prepared state |

## Qiskit and Colab

- Uses `qiskit` + `qiskit_aer.AerSimulator`.
- No IBM Quantum account, token, or internet connection is required.
- In Google Colab: `!pip install qiskit qiskit-aer`, then run the script body or paste the code into a cell.
- Results are probabilistic; the scripts print counts rather than asserting exact bitstrings.

## Scope note

**A3 (Tarrataca 3-puzzle)** is marked **backup** per the faculty note. The other five are confirmed.

## Notes

- `notes/An_*.md` — circuit, code, representative outputs, syllabus theory, likely viva Q&A.
- `notes/Plain_English/An_*_PlainEnglish.md` — the same practical without math or notation.
