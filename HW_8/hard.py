#Hard: (10 points)
#2. Write a Python function that takes a NetworkX graph as input and 
# returns the number of nodes in the graph that have a degree greater than 5.

import networkx as nx

def count_over_5_nodes(graph, threshold=5):
    return sum(1 for node in graph.nodes() if graph.degree(node) > threshold)

g = nx.Graph()
g.add_nodes_from([2, 4, 7, 9, 3])
g.add_edges_from([
    (4, 2), (4, 3), (4, 7), (4, 9),
    (2, 3), (2, 7), (2, 9),  
    (3, 7), (3, 9), 
    (4, 2), (4, 7), (4, 9), (4, 3), (4, 4), (4, 2)
])
print("The number of nodes with degree >5 is:", count_over_5_nodes(g))

#CHAT GPT Q: my code isn't counting values over 5 correctly, how can I troubleshoot this?
#A:the issue with your code is that the graph you created has nodes but no edges. As a result, all the nodes have a degree of 0. To count nodes with a degree greater than 5, you need to add edges between the nodes.
#Here’s how you can modify your code to include edges and test the function properly