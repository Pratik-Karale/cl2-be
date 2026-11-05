# Practical 2 — Error Correction in Plain English

> **In one sentence:** We store one fragile quantum message in three copies, deliberately break one copy, work out which copy broke, and repair it.

## The problem in everyday words

Quantum information is delicate. A stray gate, heat, or noise can flip a qubit from 0 to 1. If we want a useful quantum computer, we need a way to notice and fix these mistakes.

A simple idea from classical computing is repetition: say the same thing three times, and if one copy is different, trust the majority. Quantum information cannot be copied exactly, but we can **encode** one logical qubit into three physical qubits in a way that spreads the information across them.

## What the main idea is, without jargon

Imagine a message written on three cards. One card gets smudged. You compare the cards in pairs: if two agree and one differs, the odd one out is the damaged card. You rewrite it and continue.

In the quantum version:
- Three physical qubits hold one logical qubit.
- Two extra "helper" qubits check the parity of neighbouring pairs. A parity check asks, "do these two agree or disagree?" without revealing the actual message.
- The pattern of agreements and disagreements is called the **syndrome**. It tells you which qubit flipped.
- A conditional gate then flips the damaged qubit back.

## What the circuit does, step by step

1. Prepare a quantum state on qubit 0.
2. Copy it into a three-qubit code using two controlled-NOT gates.
3. Deliberately apply an X gate to qubit 1, simulating a bit-flip error.
4. Use two helper qubits to compare qubit 0 with qubit 1, and qubit 0 with qubit 2.
5. Measure the two helpers. Their results form the syndrome.
6. Apply a conditional X gate to the qubit indicated by the syndrome.
7. Measure the repaired logical qubit.

## What the result means

In the example run, the corrected qubit was measured as 0 about **75%** of the time and 1 about **25%** of the time.

That is not a failure. The original state was prepared with a rotation that already gives roughly 77% zeros and 23% ones. The code preserved those probabilities; it did not force the qubit to a fixed value. The important point is that the deliberate error was detected and corrected, so the state survived.

## Why these choices?

- **Three qubits** are the smallest repetition code that can correct one bit flip.
- **Two helper qubits** give enough parity information to identify which of the three data qubits changed.
- **Conditional gates** apply the repair only when the syndrome says it is needed.
- **A small rotation** creates a state that is visibly probabilistic, so you can see that the code preserves it.
- **A simulator** lets us test the logic without extra hardware noise.

## If the examiner asks (plain answers)

**Why three qubits?** Two copies cannot tell you which one is wrong; three allow a majority decision.

**What is a syndrome?** The pattern of parity-check results that identifies the error.

**Why use helper qubits?** They check the data qubits without measuring the message directly.

**What error does this fix?** A single bit flip. It does not fix a phase flip or two flips at once.

**Why is the answer not always 0?** The original state was a blend of 0 and 1, and the code preserves that blend.

**What is a logical qubit?** A qubit encoded across several physical qubits for protection.

**Can we copy a qubit to make copies?** No, the no-cloning theorem forbids exact copying of an unknown state; encoding is not copying.

**What is fault tolerance?** Making sure errors do not spread faster than we can correct them.

**One-line takeaway:** encode one logical qubit in three physical qubits, use parity checks to find the flipped one, and flip it back.
