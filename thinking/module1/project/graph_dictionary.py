#https://class.coursera.org/algorithmicthink-001/wiki/graph_degree
#
# REPRESENTING DIRECTED GRAPHS
#
# To gain a more tangible feel for how directed graphs are represented as dictionaries in Python, you will create three specific graphs (defined as constants) and implement a function that returns dictionaries corresponding to a simple type of directed graphs. If you are unclear on how to represent a directed graph as a dictionary, we suggest that you review the class notes on graph basics. For this part of the project, you should implement the following:
#
# EX_GRAPH0, EX_GRAPH1, EX_GRAPH2 - Define three constants whose values are dictionaries corresponding to the three directed graphs shown below. The graphs are numbered 0, 1, and 2, respectively, from left to right.
#
# Note that the label for each node should be represented as an integer. You should use these graphs in testing your functions that compute degree distributions.
# make_complete_graph(num_nodes) - Takes the number of nodes num_nodes and returns a dictionary corresponding to a complete directed graph with the specified number of nodes. A complete graph contains all possible edges subject to the restriction that self-loops are not allowed. The nodes of the graph should be numbered 0 to num_nodes - 1 when num_nodes is positive. Otherwise, the function returns a dictionary corresponding to the empty graph.
#

EX_GRAPH0 = {0: set([1, 2]), 1:set(), 2:set()}
EX_GRAPH1 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3]), 3: set([0]), 4: set([1]), 5: set([2]), 6: set()}
EX_GRAPH2 = {0: set([1, 4]), 1: set([2, 6]), 2: set([3, 7]), 3: set([7]), 4: set([1]), 5: set([2]), 6: set(), 7: set([3]), 8: set([1, 2]), 9: set([0, 4, 5, 6, 7])}

# print EX_GRAPH2




def make_complete_graph(num_nodes):
    graph = {}
    for it in range(num_nodes):
        graph[it] = set()
        for i in range(num_nodes):
            if i != it:
                graph[it].add(i)
    return graph












