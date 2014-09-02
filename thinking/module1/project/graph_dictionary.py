"""
Algorythms homework no 1
"""


EX_GRAPH0 = {0: set([1, 2]), 1:set([]), 2:set([])}
EX_GRAPH1 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3]), 3: set([0]), 4: set([1]), 5: set([2]), 6: set([])}
EX_GRAPH2 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3, 7]), 3: set([7]), 4: set([1]), 5: set([2]), 6: set([]), 7: set([3]), 8: set([1, 2]), 9: set([0, 3, 4, 5, 6, 7])}


def make_complete_graph(num_nodes):
    """Function wich makes graph from no of nodes"""
    graph = {}
    for node in range(num_nodes):
        graph[node] = set()

        for item in range(num_nodes):
            if item != node:
                graph[node].add(item)
    return graph


def compute_in_degrees(digraph):
    """Function compues in-degrees of digram"""
    graph = {}
    for item in digraph:
        graph[item] = 0
        for node in digraph:
            if node != item:
                for node_it in digraph[node]:
                    if node_it == item:
                        graph[item] +=1

    return graph


def in_degree_distribution(digraph):
    """Function compues in-degrees distribution"""
    graph = {}
    for node in digraph:
        graph[node] = 0
        for nnode in digraph:
            if nnode != node:
                for item in digraph[nnode]:
                    if item == node:
                        graph[node] += 1


    result = {}
    for item in range(len(digraph)):
        result[item] = 0
    for item in graph:
        result[graph[item]] += 1

    keys = set();
    for item in result:
        if result[item] == 0:
            keys.add(item)

    for value in keys:
        del result[value]

    return result
