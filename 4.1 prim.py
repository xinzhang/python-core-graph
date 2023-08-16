import priority_dict
from graph import *

def spanning_tree(graph, source):
    distance_table = {}
    for i in range(graph.numVertices):
        distance_table[i] = (None, None)
    
    distance_table[source] = (0, source)

    priority_queue = priority_dict.priority_dict()
    priority_queue[source] = 0

    visited_vertices = set()

    # set of edges where each edge is represented as a string
    # "1->2": is an edge
    spanning_tree = set()

    while len(priority_queue.keys()) > 0:
        current_vertex = priority_queue.pop_smallest()

        # if we have visited this vertex already
        if current_vertex in visited_vertices:
            continue

        visited_vertices.add(current_vertex)

        # if the current vertex is the source, we don't have an edge
        # to add to our spanning tree
        if current_vertex != source:
            # the current vertex is connected by the lwesst weight edge
            last_vertex = distance_table[current_vertex][1]

            edge = str(last_vertex) + "-->" + str(current_vertex)

            if edge not in spanning_tree:
                spanning_tree.add(edge)

        for neighbor in graph.get_adjacent_vertices(current_vertex):
            # the distance to the neighbor is only the weight of the edge
            # connecting the current vertex to it
            distance = graph.get_edge_weight(current_vertex, neighbor)

            # the last recorded distance of this neighbor
            neighbor_distance = distance_table[neighbor][0]

            if neighbor_distance is None or neighbor_distance > distance:
                distance_table[neighbor] = (distance, current_vertex)
                priority_queue[neighbor] = distance

    for edge in spanning_tree:
        print(edge)


g = AdjacencyMatrixGraph(9, directed=False)
g.add_edge(0, 1, 1)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 2)
g.add_edge(1, 4, 3)
g.add_edge(3, 5, 1)
g.add_edge(5, 4, 3)
g.add_edge(3, 6, 1)
g.add_edge(6, 7, 1)
g.add_edge(7, 0, 2)

spanning_tree(g, 1)
