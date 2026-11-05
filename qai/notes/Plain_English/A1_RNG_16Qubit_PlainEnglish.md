# Practical 1 — 16-qubit Random Number Generator in Plain English

> **In one sentence:** We put 16 tiny quantum coins into a "both sides at once" state, then look at all of them together, and the pattern we see is a random 16-bit number.

## The problem in everyday words

A normal computer creates "random" numbers with a formula. If someone knows the formula and the starting seed, they can predict the sequence. We want randomness that is not produced by a formula: we want the unpredictability to come from nature itself.

A quantum bit, or qubit, can be in a blend of 0 and 1. When we measure it, we get one definite answer, but which answer we get is genuinely probabilistic. If we do that with 16 qubits at once, we get a random 16-bit number.

## What the main idea is, without jargon

Imagine 16 coins. Each coin is special: instead of being heads or tails before you look, it is in a haze of both. When you look at all 16 at the same time, each coin lands on heads or tails, and the pattern of all 16 results is your random number.

The **Hadamard gate** is the "put the coin into the haze" operation. Applying it to every qubit creates an equal blend of all possible 16-bit patterns. There are 65,536 possible patterns, and each is equally likely.

**Measurement** is the act of looking. It forces each qubit to choose 0 or 1, and it gives one 16-bit string per shot.

## What the circuit does, step by step

1. Create a circuit with 16 qubits and 16 classical bits (classical bits store the answers).
2. Apply a Hadamard gate to every qubit. Each qubit is now in an equal blend of 0 and 1.
3. Measure every qubit into its classical bit.
4. Run the circuit for one shot. One shot means one full execution and one set of answers.
5. Read the 16-bit string, remove any spaces Qiskit adds, and convert it to a decimal number.

## What the result means

One example run produced `0000111101011101`, which is **3933** in decimal. On another run you will get a different string. That is expected: the circuit is designed to be random.

The important result is not one particular number. It is that the outcomes are spread evenly over the 65,536 possibilities. If you ran the circuit thousands of times and counted the results, each 16-bit pattern should appear roughly equally often (on ideal hardware).

## Why these choices?

- **16 qubits** gives a useful range of numbers and is easy to fit in memory.
- **Hadamards on every qubit** create the uniform superposition, which is what makes every outcome equally likely.
- **One shot** gives one random sample; more shots would give a batch of samples.
- **AerSimulator** lets us run locally without an IBM account; it is ideal and noise-free.
- **Transpile** converts the circuit to the simulator's gate set so it can execute.

## If the examiner asks (plain answers)

**What is a qubit?** A quantum bit that can be in a blend of 0 and 1 until measured.

**What does the Hadamard gate do?** It turns a definite 0 into an equal blend of 0 and 1.

**Why is the number random?** The measurement outcome is probabilistic; the circuit does not follow a predictable formula.

**Why 16 qubits?** Sixteen bits give 65,536 possible numbers.

**What is a shot?** One execution of the circuit and one set of measurements.

**Is this the same as Python's random module?** No. Python's module is pseudo-random and seed-based; this uses quantum measurement.

**Can you get the same number twice?** Yes, by chance, just like rolling the same dice value twice.

**What is `transpile` for?** It adapts the circuit to the backend's gate set.

**One-line takeaway:** 16 Hadamards create all 65,536 possible bit strings at once, and one measurement picks one random 16-bit number.
