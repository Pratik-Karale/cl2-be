# Common Syntax & Viva Cheat Sheet
### Information Retrieval (417524B) + Quantum AI (417523A) — Computer Laboratory II

> **How to use this file:** skim Section 0, then jump to the language you are being examined on. Every answer is in one-line "exam answer" form. No LaTeX, no images.

---

## 0. The two toolchains

**IR:** text → tokens → index/features → model → prediction/ranking → metric.

**QAI:** build a `QuantumCircuit` → `transpile` for the simulator → `AerSimulator.run(shots=...)` → read `result.get_counts()`.

| IR step | Typical call |
|---|---|
| Read text | `open(path).read()` |
| Tokenize | `re.findall(r"[a-z]+", text.lower())` |
| Remove stop words | `[w for w in tokens if w not in ENGLISH_STOP_WORDS]` |
| Stem | `PorterStemmer().stem(word)` |
| Build index | `defaultdict(set)` |
| Features | `TfidfVectorizer(...)` |
| Classify | `MultinomialNB().fit(X_train, y_train)` |
| Cluster | `AgglomerativeClustering(n_clusters=3, linkage="ward")` |
| Rank links | PageRank power iteration |
| Crawl | `requests.get` + `BeautifulSoup` |

| QAI step | Typical call |
|---|---|
| Create circuit | `QuantumCircuit(n_qubits, n_clbits)` |
| Put a qubit in superposition | `qc.h(qubit)` |
| Entangle | `qc.cx(control, target)` |
| Rotate | `qc.ry(angle, qubit)` |
| Measure | `qc.measure(qubit, clbit)` |
| Conditional gate | `with qc.if_test((clbit, 1)): qc.x(target)` |
| Simulate | `AerSimulator().run(transpile(qc, sim), shots=1024)` |
| Read results | `result.get_counts()` |

---

## 1. Information Retrieval syntax

### 1.1 Preprocessing
```python
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from nltk.stem import PorterStemmer

tokens = re.findall(r"[a-z]+", text.lower())
filtered = [w for w in tokens if w not in ENGLISH_STOP_WORDS]
stemmed = [PorterStemmer().stem(w) for w in filtered]
```
- Order: **lowercase → tokenize → remove stop words → stem**.
- Stemming cuts a word to a root (`running`, `runs`, `runner` → `run`); lemmatization uses a dictionary and is slower.

### 1.2 Inverted index and Boolean queries
```python
from collections import defaultdict
index = defaultdict(set)
for name, text in docs.items():
    for word in re.findall(r"[a-z]+", text.lower()):
        index[word].add(name)

def search_and(query):
    sets = [index.get(w, set()) for w in re.findall(r"[a-z]+", query.lower())]
    return sorted(set.intersection(*sets))
```
- `index[word]` is the **posting list**: the documents containing that word.
- AND = intersection; OR = union; NOT = difference.

### 1.3 TF-IDF and text classification
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

vec = TfidfVectorizer(stop_words="english")
X_train_vec = vec.fit_transform(X_train)   # fit on training text only
X_test_vec = vec.transform(X_test)         # transform test text
model = MultinomialNB().fit(X_train_vec, y_train)
pred = model.predict(X_test_vec)
```
- `fit_transform` learns the vocabulary/IDF **and** transforms; use it only on training data.
- `transform` applies the learned vocabulary to test/new text.
- TF-IDF = term frequency × inverse document frequency: common words in the corpus get down-weighted.

### 1.4 Bayesian network (pgmpy)
```python
try:
    from pgmpy.models import DiscreteBayesianNetwork
except ImportError:
    from pgmpy.models import BayesianNetwork as DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([("age", "target"), ("sex", "target"), ("target", "cp")])
model.fit(df)
infer = VariableElimination(model)
result = infer.query(variables=["target"], evidence={"age": 1, "sex": 0})
```
- Continuous columns must be **discretized** before fitting.
- Edges show dependence; the query returns a probability table.

### 1.5 Clustering
```python
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.metrics import adjusted_rand_score

dendrogram(linkage(X, method="ward"))
labels = AgglomerativeClustering(n_clusters=3, linkage="ward").fit_predict(X)
ari = adjusted_rand_score(y_true, labels)
```
- Agglomerative = bottom-up merging; divisive = top-down splitting.
- Ward linkage merges clusters that add the least variance.
- ARI compares clusters with known labels; 1 = perfect, 0 = random.

### 1.6 PageRank
```python
d = 0.85
rank = np.ones(n) / n
for _ in range(100):
    rank = (1 - d) / n + d * M @ rank
```
- `M[j][i] = 1 / outlinks(i)` if page `i` links to `j`.
- Damping `d` = probability of following a link; `(1-d)/n` is the random-jump term.
- Power iteration repeats until the scores stop changing.

### 1.7 Web crawler
```python
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

html = requests.get(url, timeout=10).text
soup = BeautifulSoup(html, "html.parser")
for card in soup.select("article.product_pod"):
    title = card.h3.a["title"]
    price = card.select_one(".price_color").text
    link = urljoin(url, card.h3.a["href"])
next_page = soup.select_one("li.next a")
```
- `select` uses CSS selectors; `select_one` returns the first match.
- `urljoin` turns relative links into absolute URLs.
- Respect `robots.txt`, add delays, and set a timeout.

---

## 2. Quantum AI syntax (Qiskit)

### 2.1 Circuit basics
```python
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 2)      # 2 qubits, 2 classical bits
qc.h(0)                        # superposition on qubit 0
qc.cx(0, 1)                    # CNOT: entangle 0 and 1
qc.measure([0, 1], [0, 1])     # qubit -> clbit

sim = AerSimulator()
counts = sim.run(transpile(qc, sim), shots=1024).result().get_counts()
print(counts)
```
- `QuantumCircuit(n, m)` = `n` qubits + `m` classical bits.
- `shots` = number of repeated runs; `counts` = how many times each bitstring appeared.
- `transpile` rewrites the circuit for the target simulator/backend.
- Qiskit displays bitstrings with the **rightmost bit = qubit 0** (little-endian).

### 2.2 Gates used in the practicals

| Gate | Call | What it does |
|---|---|---|
| Hadamard | `qc.h(q)` | Creates superposition |
| Pauli-X | `qc.x(q)` | Bit flip (quantum NOT) |
| Pauli-Z | `qc.z(q)` | Phase flip |
| Phase | `qc.s(q)` | 90° phase |
| T gate | `qc.t(q)` | 45° phase |
| Rotation | `qc.ry(angle, q)` | Rotates around the Y axis |
| CNOT | `qc.cx(c, t)` | Entangles control and target |
| Toffoli / MCX | `qc.mcx(controls, target)` | Multi-controlled X |
| QFT | `QFT(n)` | Quantum Fourier transform |

### 2.3 Classical conditions
```python
with qc.if_test((qc.clbits[1], 1)):
    qc.x(2)
```
- The gate is applied only when the measured classical bit equals 1.
- Used in teleportation and error correction.

### 2.4 Noise and benchmarking
```python
from qiskit_aer.noise import NoiseModel, depolarizing_error

noise = NoiseModel()
noise.add_all_qubit_quantum_error(depolarizing_error(0.02, 1), ["h", "s", "sdg"])
sim = AerSimulator(noise_model=noise)
```
- Depolarizing noise randomly replaces the state with a mixed state.
- Randomized benchmarking applies random gates, then their inverse; survival probability falls as the sequence grows.

### 2.5 QFT and Grover helpers
```python
from qiskit.circuit.library import QFT
qc.compose(QFT(5), inplace=True)

# Grover iteration count
iterations = int(np.pi / 4 * np.sqrt(N / number_of_solutions))
```
- QFT maps computational-basis states to Fourier-basis states; it is the key step in phase estimation and Shor's algorithm.
- Grover gives a quadratic speed-up: about `sqrt(N)` iterations instead of `N`.

---

## 3. Common traps

### IR traps

| Trap | Correct statement |
|---|---|
| Using test data in `fit_transform` | Fit the vectorizer on training text only; `transform` the test text. |
| Stemming before removing stop words | Either order works, but stop-word removal before stemming is the usual pipeline; be consistent. |
| Treating a posting list as a list | It is a set/dictionary of document IDs; use set operations for Boolean queries. |
| Forgetting to discretize continuous columns | Bayesian networks in pgmpy need discrete values. |
| Using accuracy alone on spam data | Spam is imbalanced; report precision, recall and F1. |
| Confusing clustering with classification | Clustering has no labels; ARI needs labels only for evaluation. |
| PageRank with dangling pages | A page with no outlinks needs its rank distributed; otherwise mass is lost. |
| Crawling without limits | Respect robots.txt, use timeouts, and do not hammer a site. |

### QAI traps

| Trap | Correct statement |
|---|---|
| Measuring too early | Measurement collapses the state; measure only at the end. |
| Forgetting `transpile` | Run the transpiled circuit on the simulator/backend. |
| Confusing qubits and classical bits | Gates act on qubits; measurements write to classical bits. |
| Expecting one exact bitstring | Quantum results are probabilistic; read the counts distribution. |
| Thinking a simulator uses real hardware | AerSimulator is a local classical simulation, not IBM hardware. |
| Adding noise without a noise model | Noise appears only when you pass a `NoiseModel` to the simulator. |
| Too many Grover iterations | More than ~`sqrt(N)` iterations reduces the success probability. |
| Treating superposition as "both at once" literally | It is a probability amplitude state; measurement gives one outcome. |

---

## 4. Shared viva bank

### 4.1 IR fundamentals

| Question | Answer |
|---|---|
| What is information retrieval? | Finding relevant unstructured information (text, images, audio) for a user's need. |
| IR vs data retrieval | IR is ranked, approximate and relevance-based; database retrieval is exact and structured. |
| What is an inverted index? | A word → posting-list map that lets the system find documents containing a term quickly. |
| Boolean vs vector model | Boolean gives exact matching; the vector model ranks by similarity. |
| TF-IDF | Term frequency × inverse document frequency; rewards words that are frequent in a document but rare in the corpus. |
| Cosine similarity | Dot product divided by the product of vector lengths; measures the angle between document vectors. |
| Precision vs recall | Precision = correct positives ÷ predicted positives; recall = correct positives ÷ actual positives. |
| F1-score | Harmonic mean of precision and recall. |
| MAP | Mean of average precision across queries; rewards relevant documents ranked high. |
| nDCG | Discounted gain divided by ideal gain; rewards relevant results at the top. |
| Naive Bayes assumption | Features are conditionally independent given the class. |
| Bayesian network | A graph of variables with conditional probability tables; edges encode dependence. |
| Hierarchical clustering | Builds a tree of clusters by merging (agglomerative) or splitting (divisive). |
| PageRank | Ranks pages by the number and quality of incoming links; solved by power iteration. |
| Web crawler | Downloads pages and follows links to collect documents; must respect robots.txt. |

### 4.2 QAI fundamentals

| Question | Answer |
|---|---|
| What is a qubit? | A two-state quantum system that can be in a superposition of 0 and 1. |
| Superposition | A state with amplitudes on both 0 and 1; measurement gives one outcome with some probability. |
| Entanglement | A joint state that cannot be written as independent states of the parts. |
| What does a Hadamard gate do? | Turns a definite state into an equal superposition. |
| What does CNOT do? | Flips the target when the control is 1; creates entanglement. |
| What is measurement? | It collapses the quantum state to a basis state and returns a classical bit. |
| What are shots? | The number of repeated circuit executions used to estimate the result distribution. |
| What is transpile? | Rewriting a circuit into the gate set of a target simulator/backend. |
| Bell state | A maximally entangled two-qubit state such as `(|00> + |11>)/sqrt(2)`. |
| Quantum teleportation | Transfer a qubit state using a Bell pair and two classical bits; the original state is destroyed. |
| Quantum error correction | Encode one logical qubit in several physical qubits and correct errors from syndrome measurements. |
| 3-qubit bit-flip code | Encodes `a|0> + b|1>` as `a|000> + b|111>`; majority vote corrects one bit flip. |
| QFT | Quantum Fourier transform; maps computational basis to Fourier basis; used in phase estimation and Shor. |
| Grover's algorithm | Searches an unsorted space in about `sqrt(N)` steps using an oracle and diffusion. |
| Randomized benchmarking | Estimates average gate error by applying random sequences and their inverse, then measuring survival. |
| NISQ | Noisy Intermediate-Scale Quantum: current devices with limited qubits and no full error correction. |

---

## 5. Last-minute "say this" lines

- **IR preprocessing:** "Lowercase, tokenize, remove stop words, then stem; the goal is to reduce vocabulary while keeping meaning."
- **Inverted index:** "A word-to-document map; Boolean AND is the intersection of posting lists."
- **Spam filter:** "TF-IDF converts text to numbers, Multinomial Naive Bayes classifies it, and I report precision, recall and F1 because spam is imbalanced."
- **Bayesian network:** "Nodes are variables, edges are dependencies, and variable elimination answers diagnosis queries."
- **Clustering:** "Agglomerative clustering merges the closest clusters; the dendrogram shows the merge order and ARI checks against known labels."
- **PageRank:** "A page is important if important pages link to it; power iteration solves the damping equation."
- **Crawler:** "Requests fetches the page, BeautifulSoup parses product cards and links, and the next link drives the crawl."
- **Qiskit:** "Build the circuit, transpile for Aer, run with shots, and read the counts distribution."
- **Teleportation:** "A Bell pair plus two classical bits transfers the state; the original is destroyed."
- **Error correction:** "Encode in three qubits, measure the syndrome, and apply the correction."
- **QFT:** "Hadamards plus controlled phase rotations plus swaps; it is the Fourier transform over amplitudes."
- **Grover:** "Oracle marks the solution, diffusion amplifies it, and about sqrt(N) iterations find it."
