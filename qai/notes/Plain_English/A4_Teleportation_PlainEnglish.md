# Practical 4 — Quantum Teleportation in Plain English

> **In one sentence:** We move a fragile quantum state from one qubit to another using a shared entangled pair and two ordinary bits of information.

## The problem in everyday words

Suppose you have a quantum state that you cannot copy and cannot physically ship. You want the same state to appear somewhere else. Quantum teleportation lets you do that: the original is destroyed, and an identical state is recreated at the destination.

It sounds like science fiction, but it follows a clear recipe: share an entangled pair, measure the original together with one half of the pair, send two classical bits, and apply two simple corrections.

## What the main idea is, without jargon

Imagine two friends, Alice and Bob, who share a pair of magic gloves. The gloves are linked: whatever happens to one is connected to the other. Alice also has a fragile vase (the unknown quantum state) that she cannot copy or mail.

Alice does a special measurement that mixes the vase with her glove. The measurement gives one of four possible results, and it destroys the vase. She phones Bob two bits: "00", "01", "10", or "11".

Depending on those two bits, Bob applies one of four simple fixes to his glove. When he is done, his glove holds the exact state of the vase. The vase itself never traveled; only the two-bit phone call plus the shared link made the transfer possible.

## What the circuit does, step by step

1. Prepare the unknown state on qubit 0 using a small rotation.
2. Create an entangled Bell pair on qubits 1 and 2.
3. Mix qubit 0 with qubit 1 and measure both. This is the Bell-basis measurement.
4. The two measurement results are the two classical bits.
5. If the second bit is 1, apply an X gate to qubit 2. If the first bit is 1, apply a Z gate.
6. Measure qubit 2. It now matches the original state.

## What the result means

The example run produced counts like `000: 201`, `011: 199`, and so on. Qiskit prints the highest classical bit first, so the first character is the teleported qubit.

The first character was 0 about **77%** of the time. That matches the original rotation, which gives about 77% zeros and 23% ones. The other two characters are the random Bell-measurement outcomes. The important point is that the destination qubit reproduces the original probabilities.

## Why these choices?

- **Ry(1.0)** prepares an easy-to-see state that is not simply 0 or 1.
- **A Bell pair** provides the entanglement that links the two ends.
- **Two classical bits** carry the measurement outcome; without them Bob cannot choose the right correction.
- **X and Z corrections** fix the bit and phase differences caused by the measurement.
- **A simulator** lets us test the protocol without hardware noise.

## If the examiner asks (plain answers)

**Does the qubit travel?** No; only the state is recreated.

**Does this break the no-cloning rule?** No; the original is destroyed, so there is still only one copy.

**Is it faster than light?** No; the two classical bits must reach the receiver.

**Why two bits?** The Bell measurement has four possible outcomes.

**What are the corrections?** X fixes a bit flip, Z fixes a phase flip.

**Why is the first character the teleported qubit?** Qiskit lists the highest classical bit first.

**Can it teleport any state?** Yes, any unknown single-qubit state.

**What is a Bell pair?** Two qubits that are entangled so their outcomes are linked.

**One-line takeaway:** a shared entangled pair plus two classical bits can move an unknown quantum state, but the original is destroyed and the classical bits are essential.
