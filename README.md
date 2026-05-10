# The Torchbearer

**Student Name:** Stephen Conley
**Student ID:** 130331614
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  It does not compute the order of relics visited, which is important for determining the total cost whilst satisfying the requirements.

- **What decision remains after all inter-location costs are known:**
  The optimal order of relics visited still remains.

- **Why this requires a search over orders (one sentence):**
  There are k! possible orders to visit all relics, and each must be evaluated and compared to optimize cost.
---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| node S | Starting node, needs to begin from this node |
| nodes R | Order visited is unknown, must be able to optimally traverse from any relic to any relic |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | Nested Dictionaries |
| What the keys represent | Outer: source node, Inner: destination node|
| What the values represent | Shortest cost path from source to destination|
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | Dictionary is a hash map |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** Let k equal the magnitude of the relic set. Number of Dijkstra runs equals k + 1.
- **Cost per run:** One Dijkstra run costs O(m log(n))
- **Total complexity:** Total complexity is (k+1)*(m log(n)) = O(km log(n))
- **Justification (one line):** Dijkstra is ran k + 1 times, each costing O(m log(n)). k + 1 is simplified to k.

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  For nodes already in the finalized set, the distance is the lowest value possible to the destination.

- **For nodes not yet finalized (not in S):**
  For nodes not in the finalized set, the distance is the lowest value found using exlusively nodes from the finalized set as intermediate steps from source to destination.

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  The starting node has the shortest path of 0, with source and destination being itself.
  All other nodes have no discovered paths using finalized nodes, so all node distances are set to infinity.

- **Maintenance : why finalizing the min-dist node is always correct:**
  Since paths are built using only finalized, true shortest paths, the path to the new node is always correct.
  Since all edge weights are nonnegative, no future path can decrease the distance.

- **Termination : what the invariant guarantees when the algorithm ends:**
  The invariant guarantees that all nodes are in the finalized set and their distances are their true shortest path.

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

Correct distances allow the accurate comparison of the total cost to traverse different possible routes.

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** The failure mode for greedy is choosing a locally optimal path that creates a less optimal path later.
- **Counter-example setup:** 
| From \ To | B   | C   | D   | T   |
|-----------|-----|-----|-----|-----|
| S         | 3   | 5   | 8   | --  |
| B         | --  | 100 | 20  | 1   |
| C         | 4   | --  | 100 | 1   |
| D         | 15  | 5   | --  | 100 |

- **What greedy picks:** Greedy route:    S -> B -> D -> C -> T   total fuel: 3 + 20 + 5 + 1 = 29
- **What optimal picks:** Optimal route:  S -> D -> C -> B -> T   total fuel: 8 + 5 + 4 + 1 = 18
- **Why greedy loses:** It chooses to traverse to B first, but the distances to the other nodes with B as a source are significantly less optimal. Traversing to B last is most optimal.

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- It must explore all possible relic visitation orders and compare them to find the minimum total cost.

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | currLocation | node | current node in route |
| Relics already collected | visitedRelics | set[node] | collection of already traversed relic nodes in this search |
| Fuel cost so far | totalCost | int | total fuel so far|

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | set |
| Operation: check if relic already collected | Time complexity: O(1) |
| Operation: mark a relic as collected | Time complexity: O(1) |
| Operation: unmark a relic (backtrack) | Time complexity: O(1) |
| Why this structure fits | It needs to check, add, and remove constantly, so a hash map works best for speed. |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** The worst case is O(k!)
- **Why:** Any relic can be visited in any order, so there are k options at first, then k-1, then k-2, and so on until 1.

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** The best total cost so far.
- **When it is used:** It is used to compare the current route's total cost with the best so far total cost.
- **What it allows the algorithm to skip:** It allows it to discard the current route the moment it exceeds the best so far cost, as it can't decrease.

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** The current location, which relics have already been visited, the current running cost, and distances to relics or the destination are known.
- **What the lower bound accounts for:** It estimates the remaining traversal cost to get an idea of how viable the current route is.
- **Why it never overestimates:** It must never overestimate as it could potentially prune a route that is actually optimal.

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- Pruning is safe as long as it never overestimates the remaining cost. If there is already a true cost path that is cheaper than the current cost combined the estimated cost, it is safe to discard that route search and continue.

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
