''' 
...................................................
CP164 - Data Structures 

Author: Laith Adi 

ID: 170265190    

Email: Adix5190@mylaurier.ca

Updated: 2019-02-11 
...................................................
'''
from Priority_Queue_array import Priority_Queue

def prims(graph, start_node):
    """
    -------------------------------------------------------
    Applies Prim's Algorithm to a graph.
    Use: edges, total = prims(graph, node)
    -------------------------------------------------------
    Parameters:
        graph - graph to evaluate (Graph)
        start_node - name of node to start evaluation from (str)
    Returns:
        edges - the list of the edges traversed (list of Edge)
        total - total distance of all edges traversed (int)
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    total = 0
    edges = []
    nodes = []
    nodes.append(start_node)
    for edge in graph.edges_by_node(start_node):
        pq.insert(edge)
    while len(nodes) < len(graph):
        edge = pq.remove()
        node_name = edge.end
        if node_name not in nodes:
            nodes.append(node_name)
            edges.append(edge)
            total += edge.distance
            for edge in graph.edges_by_node(node_name):
                if edge.end not in nodes:
                    pq.insert(edge)
    return edges, total

    