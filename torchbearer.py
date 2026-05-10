"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: ___________________________
Student ID:   ___________________________

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    """
    explanation = "A single shortest path run from S is not enough since it does not compute and compare the order of relics visited, " \
    "which is necessary for lowest total cost whilst satisfying the requirements." \
        "\nAfter all inter-location costs are known, the order of relics to traverse are stil unknown." \
        "\nThis requires a search over orders since there are k! possible orders to visit, and each " \
        "must be compared to find the true lowest total cost."
    return explanation


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.
    """
    source = set()
    source.add(spawn)
    source.add(exit_node)
    for i in len(relics):
        source.add(relics[i])
    pass


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    """
    inTree = {}
    distList = {} # storage of the minimum cost from source to every node in graph
    parent = {}
    dist = 0 # current route cost from source to current node
    weight = 0



    for node in graph:
        inTree[node] = False
        distList[node] = float('inf')
        parent[node] = None
    
    distList[source] = 0
    currentNode = source
    while inTree[currentNode] == False:
        inTree[currentNode] = True
        if (currentNode != source):
            weight = weight + dist
        for neighbor, weight in graph[currentNode]:
            if (distList[neighbor] > (distList[currentNode] + weight)):
                distList[neighbor] = distList[currentNode] + weight
                parent[neighbor] = currentNode
        
        dist = float('inf')
        for node in graph:
            if (inTree[node] == False and dist > distList[node]):
                dist = distList[node]
                currentNode = node
    return distList


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    """
    dist_table = {}
    dist_table[spawn] = run_dijkstra(graph, spawn)
    for node in relics:
        dist_table[node] = run_dijkstra(graph, node)

    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    text = " For nodes already in the finalized set, the distance is the lowest value possible to the destination." \
    "For nodes not in the finalized set, the distance is the lowest value found using exlusively nodes from the finalized set as intermediate steps from source to destination." \
    "The starting node has the shortest path of 0, with source and destination being itself. All other nodes have no discovered paths using finalized nodes, so all node distances are set to infinity." \
    " Since paths are built using only finalized, true shortest paths, the path to the new node is always correct. Since all edge weights are nonnegative, no future path can decrease the distance." \
    " The invariant guarantees that all nodes are in the finalized set and their distances are their true shortest path." \
    "Correct distances allow the accurate comparison of the total cost to traverse different possible routes."
    return text


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    """
    text = "The failure mode for greedy is choosing a locally optimal path that creates a less optimal path later.\n" \
    "| From / To | B   | C   | D   | T   |\n" \
    "|-----------|-----|-----|-----|-----|\n" \
    "| S         | 3   | 5   | 8   | --  |\n" \
    "| B         | --  | 100 | 20  | 1   |\n" \
    "| C         | 4   | --  | 100 | 1   |\n" \
    "| D         | 15  | 5   | --  | 100 |\n" \
    "Greedy route:    S -> B -> D -> C -> T   total fuel: 3 + 20 + 5 + 1 = 29\n" \
    "Optimal route:  S -> D -> C -> B -> T   total fuel: 8 + 5 + 4 + 1 = 18\n" \
    "Greedy chooses to traverse to B first, but the distances to the other nodes with B as a source are significantly less optimal. Traversing to B last is most optimal. " \
    "The algorithm must explore all possible relic visitation orders and compare them to find the minimum total cost."

    return text


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    pass


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    #_run_tests()
    print(explain_search())
    
