# Practical 6 — 5-qubit Quantum Fourier Transform in Plain English

> **In one sentence:** We take a small quantum pattern, pass it through a quantum version of a prism, and look at the frequency ingredients that come out.

## The problem in everyday words

A musical chord is a mix of notes. If you pass it through a prism-like analyzer, you can see which frequencies are present. The Fourier transform does the same job for signals: it turns a pattern over time into a pattern over frequencies.

The Quantum Fourier Transform is the quantum version of that idea. It takes the amplitudes of a quantum state and rearranges them into a frequency-style description. It is a key ingredient in phase estimation, period finding, and Shor's factoring algorithm.

## What the main idea is, without jargon

Imagine a row of five lamps, each of which can be bright or dim in a quantum blend. The QFT does not simply copy the lamps; it mixes their brightnesses in a careful pattern so that repeating structures become easy to spot.

A useful picture is a prism: white light goes in, and a rainbow of frequencies comes out. The QFT is the prism for quantum amplitudes. It uses Hadamard gates and controlled phase rotations to create interference, and the interference pattern encodes the frequency content.

## What the circuit does, step by step

1. Create five qubits.
2. Put qubit 0 into a superposition with a Hadamard gate.
3. Set qubit 1 to 1 with an X gate.
4. Apply the five-qubit QFT gate to all five qubits.
5. Measure all five qubits.
6. Repeat the experiment many times and collect the counts.

## What the result means

The counts are spread over many five-bit strings, such as `00000`, `11110`, `00110`, and so on. No single answer dominates. That is expected: the QFT turns the input pattern into a frequency distribution, and a measurement gives one sample from that distribution.

The spread and symmetry of the counts are the interesting part. They show that the input has been transformed, not simply copied. On a perfect simulator, the distribution reflects the mathematical Fourier transform of the input state.

## Why these choices?

- **Five qubits** give 32 amplitudes, enough to see the transform without a huge circuit.
- **`H` on qubit 0 and `X` on qubit 1** create a simple, non-trivial input pattern.
- **The QFT gate** is the standard library implementation, so the circuit stays short and readable.
- **1024 shots** give a reasonable estimate of the output distribution.
- **A simulator** lets us see the ideal transform without hardware noise.

## If the examiner asks (plain answers)

**What is the QFT?** The quantum version of the Fourier transform; it changes the basis to reveal frequency content.

**What does it do to a state?** It mixes amplitudes with phase rotations and Hadamards, producing a frequency-style pattern.

**Why is it useful?** It is the engine behind phase estimation, period finding, and Shor's algorithm.

**Why is the output spread out?** The transform distributes amplitude across many frequencies; measurement picks one sample.

**Can you see the whole spectrum in one shot?** No; you need many shots to estimate the distribution.

**What is the inverse QFT?** The reverse transform, used to read out phases in algorithms.

**How many gates does it need?** Roughly the square of the number of qubits for the standard construction.

**Does the QFT alone solve a hard problem?** No; it is a component. The surrounding algorithm must prepare the input and interpret the output.

**One-line takeaway:** the QFT is a quantum prism: it turns hidden periodicity into a measurable frequency pattern.
