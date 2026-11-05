# Practical 6 — PageRank in Plain English

> **In one sentence:** We rank web pages by treating every link as a vote, giving more weight to votes from important pages.

## The problem in everyday words

A search engine finds many pages that mention your query. Which should appear first? One signal is how other pages link to them. A link from an important page should count more than a link from an unimportant page. PageRank turns that idea into a score.

## What the main idea is, without jargon

Imagine five people in a room. Each person points at the people they trust. A person is important if many people point at them, especially if those people are themselves important.

That is circular: importance depends on importance. PageRank solves it by starting everyone with the same score and repeatedly updating:

- Each page shares its score equally among the pages it links to.
- A small random-jump term gives every page a little score, so nobody gets stuck.

After many rounds, the scores stop changing. That is the PageRank.

## What the code does, step by step

1. Define the link graph for pages A, B, C, D and E.
2. Build a table saying how each page divides its vote among its links.
3. Give every page the same starting score.
4. Repeat the update 100 times with damping factor 0.85.
5. Sort the pages by score.
6. Compare the result with networkx's PageRank.

## What the result means

The ranking is:

| Page | Score |
|---|---|
| C | 0.3747 |
| A | 0.3667 |
| B | 0.1858 |
| D | 0.0428 |
| E | 0.0300 |

C wins because it receives links from A, B, D and E. A is close behind because C links to it, and C is important. networkx produces exactly the same numbers, which confirms the implementation.

## Why these choices?

- The damping factor 0.85 is the standard value: follow a link 85% of the time.
- The random-jump term prevents cycles from trapping all the score.
- Power iteration is simple and converges quickly on a small graph.
- networkx provides an independent cross-check.

## If the examiner asks (plain answers)

**What is PageRank?** A link-based importance score for web pages.

**Why is a link a vote?** It suggests the linking page found the target useful.

**What is the damping factor?** The chance of following a link instead of jumping to a random page.

**Why is there a random jump?** So the scores do not get stuck in loops and every page gets a small chance.

**Why is C first?** It has many incoming links from pages that are themselves linked.

**What is a dangling page?** A page with no outgoing links; it needs special handling.

**Does PageRank use the page text?** No, only the link structure.

**One-line takeaway:** PageRank is repeated link-voting with a random jump; important pages pass more importance to the pages they link to.
