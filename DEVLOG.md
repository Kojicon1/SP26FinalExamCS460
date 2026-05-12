# Development Log – The Torchbearer

**Student Name:** Stephen Conley
**Student ID:** 130331614


---

## Entry 1 – [05/09/2026]: Initial Plan


I plan to fill out the README file first to grasp an understanding of the problem and what is being asked before I start coding anything.
After I complete that, I plan to implement the code in the order that the README follows. I expect that writing the search algorithm is the hardest part, 
as comparison and storage should be more straight forward. I plan to test with small sets that include some edge cases and confirm it functions logically.

After doing part 6 from the README, the pruning algorithm seems the most complex, with estimating the remaining cost without ever overestimated being the most troublesome in concept.

---

## Entry 2 – [05/10/2026]: [Pruning bug]


One bug was that for the lower bound pruning it would search for the lowest next path to all relics, including those that had already been visited. I resolved it by limiting the search to only unvisited nodes.

---

## Entry 3 – [05/12/2026]: [Tidying up]

Cleaned up spacing and added some comments to pruning algorithm. Ensured consistency with the code and README file.

---

## Entry 4 – [05/12/2026]: Post-Implementation Reflection


Implementation of the individual dijkstra run I feel content with. The order searching algorithm took significantly longer, and I probably could have spent more time on the preparation and planning phase to make the process easier and faster. 

---

## Final Entry – [05/12/2026]: Time Estimate


| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 0.5 |
| Part 2: Precomputation Design | 2.5 |
| Part 3: Algorithm Correctness | 1.0 |
| Part 4: Search Design | 1.0 |
| Part 5: State and Search Space | 1.0 |
| Part 6: Pruning | 1.5 |
| Part 7: Implementation | 3.0 |
| README and DEVLOG writing | 3 |
| **Total** | 13.5 |
