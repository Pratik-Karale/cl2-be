# CL2 Practicals — BE AI & DS, Semester VII

Runnable lab code and exam notes for Computer Laboratory II:

- **417524B — Information Retrieval**
- **417523A — Quantum Artificial Intelligence**

SPPU 2020 pattern, AY 2026-27.

## Scope note

| Subject | Included | Uncertain / backup |
|---|---|---|
| Information Retrieval | All 7 assignments (P1–P7) | P4 (spam filter) and P5 (agglomerative clustering) are marked as backup because they were the two not covered by the local submissions; keep them ready in case they are asked |
| Quantum AI | All 6 assignments (A1–A6) | A3 (Tarrataca 3-puzzle) is marked as backup per the faculty note |

Per the faculty message: QAI practicals use **Qiskit** (IBM software) and **Google Colab** is allowed. All QAI scripts here use Qiskit with the local **Aer** simulator, so no IBM account, token, or internet connection is needed.

## What is inside

| Folder | Contents |
|---|---|
| `ir/` | 7 runnable Information Retrieval practicals + datasets |
| `qai/` | 6 runnable Quantum AI practicals (Qiskit) |
| `ir/notes/` | Main viva notes and plain-English notes, one per practical |
| `qai/notes/` | Main viva notes and plain-English notes, one per practical |
| `common/` | IR/QAI syntax cheat sheet, IR metrics, QAI concepts |
| `references/` | Sanitized reference PDFs used to build the notes |
| `outputs/` | Generated plots/CSVs (ignored by git) |

Every practical has **two** notes files:

1. `notes/Pn_*.md` or `notes/An_*.md` — code, exact outputs, syllabus theory, likely viva Q&A.
2. `notes/Plain_English/..._PlainEnglish.md` — the same practical explained without math or jargon.

## Quick start

```bash
git clone https://github.com/Pratik-Karale/cl2-be.git
cd cl2-be

python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
```

Run any practical from the repository root, for example:

```bash
python ir/p1_preprocessing.py
python qai/a1_rng_16qubit.py
```

Generated plots and CSV files go to `outputs/`.

## Information Retrieval practicals

| # | Script | Topic |
|---|---|---|
| P1 | `ir/p1_preprocessing.py` | Lowercase, tokenize, stop-word removal, Porter stemming |
| P2 | `ir/p2_inverted_index.py` | Inverted index and AND query retrieval |
| P3 | `ir/p3_bayesian_network.py` | Bayesian network for heart-disease diagnosis |
| P4 | `ir/p4_spam_filter.py` | TF-IDF + Multinomial Naive Bayes spam filter *(backup)* |
| P5 | `ir/p5_agglomerative.py` | Agglomerative hierarchical clustering + dendrogram *(backup)* |
| P6 | `ir/p6_pagerank.py` | PageRank by power iteration, checked against NetworkX |
| P7 | `ir/p7_web_crawler.py` | Web crawler with requests + BeautifulSoup |

Datasets are in `ir/data/`: six small text documents, a heart-disease CSV, an SMS spam CSV, and a sample product CSV. P7 uses <https://books.toscrape.com> when online and a built-in sample page when offline.

## Quantum AI practicals

| # | Script | Topic |
|---|---|---|
| A1 | `qai/a1_rng_16qubit.py` | 16-qubit random number generator |
| A2 | `qai/a2_error_correction.py` | 3-qubit bit-flip error-correction code |
| A3 | `qai/a3_tarrataca_3puzzle.py` | Tarrataca quantum production system for the 3-puzzle *(backup)* |
| A4 | `qai/a4_teleportation.py` | Quantum teleportation with a Bell pair |
| A5 | `qai/a5_randomized_benchmarking.py` | Randomized benchmarking under depolarizing noise |
| A6 | `qai/a6_qft_5qubit.py` | 5-qubit quantum Fourier transform |

All QAI scripts use `qiskit` + `qiskit_aer.AerSimulator`. They run locally and in Google Colab after `pip install qiskit qiskit-aer`.

## Notes and exam preparation

Start with the plain-English file to understand the practical, then read the main note for the code, outputs and likely viva questions. The `common/` folder has:

- `Common_IR_QAI_Syntax_and_Viva.md` — syntax for IR libraries and Qiskit, common traps, and a shared viva bank.
- `IR_Evaluation_Metrics.md` — precision, recall, F1, MAP, nDCG, ARI, silhouette, and other IR metrics.
- `QAI_Concepts_Cheat_Sheet.md` — qubits, gates, circuits, measurement, teleportation, error correction, QFT, Grover, and benchmarking.

## References

The `references/` folder contains sanitized copies of the local practical writeups: names, roll numbers and metadata removed. Original reference code and datasets are from <https://github.com/diveshadivarekar/Practical-Codes> (`sem 7/cl2`).

## Academic use

This repository is for study and revision. The QAI circuits are small teaching examples for the Aer simulator, not hardware benchmarks.
