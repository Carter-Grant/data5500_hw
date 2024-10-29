#Easy: (5 points)

#Write a Python function that takes a NetworkX graph as input andreturns the number of nodes in the graph.
 
import networkx as nx

def count_nodes(graph):
    return graph.number_of_nodes()

#Example Data:
g = nx.Graph()
g.add_nodes_from([2, 4, 7, 9, 3])
print(count_nodes(g))  # Output: 3
