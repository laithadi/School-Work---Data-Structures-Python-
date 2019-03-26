''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-02-11 
...................................................
'''

from Graph import Graph, Edge
from prims import prims

data = (
    ('A', 'B', 3), ('A', 'C', 3), ('B', 'A', 3), ('B', 'C', 4), ('B', 'H', 6), ('C', 'A', 3), ('C', 'B', 4), ('C', 'D', 3),
    ('C', 'E', 6), ('D', 'C', 3), ('D', 'G', 7), ('E', 'C', 6), ('E', 'F', 7), ('E', 'G', 4), ('F', 'E', 7), ('F', 'H', 3), 
    ('F', 'I', 5), ('G', 'D', 7), ('G', 'E', 4), ('G', 'I', 9), ('H', 'B', 6), ('H', 'F', 3), ('H', 'I', 4), ('I', 'F', 5),
    ('I', 'G', 9), ('I', 'H', 4)
)

edges = []
for i in data:
    edge = Edge(i[0], i[1], i[2])
    edges.append(edge)
graph = Graph(edges)
node = graph.node_names()
edges, total = prims(graph, "A")
for i in edges:
    print(i)
print("Total Distance: {}".format(total))
