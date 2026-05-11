# Development Log – The Torchbearer

**Student Name:** Stephen Conley
**Student ID:** 130331614

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [05/09/2026]: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

I plan to fill out the README file first to grasp an understanding of the problem and what is being asked before I start coding anything.
After I complete that, I plan to implement the code in the order that the README follows. I expect that writing the search algorithm is the hardest part, 
as comparison and storage should be more straight forward. I plan to test with small sets that include some edge cases and confirm it functions logically.

After doing part 6 from the README, the pruning algorithm seems the most complex, with estimating the remaining cost without ever overestimated being the most troublesome in concept.

---

## Entry 2 – [Date]: [Short description]

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

One bug was that for the lower bound pruning it would search for the lowest next path to all relics, including those that had already been visited. I resolved it by limiting the search to only unvisited nodes.

---

## Entry 3 – [Date]: [Short description]

_Your entry here._

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 0.2 |
| Part 2: Precomputation Design | 2.5 |
| Part 3: Algorithm Correctness | 1.0 |
| Part 4: Search Design | 0.5 |
| Part 5: State and Search Space | 1.0 |
| Part 6: Pruning | .8 |
| Part 7: Implementation | |
| README and DEVLOG writing | 5 |
| **Total** | |
