import abc

import numpy as np

class Graph(abc.ABC):
    def __init__(self, numVertices, directed=False):
        self.numVertices = numVertices
        self.directed = directed
    
    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass
    
    @abc.abstractmethod
    def get_indegree(self, v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass
    
    @abc.abstractmethod
    def display(self):
        pass
    
# adjacency matrix
class AdjacencyMatrixGraph(Graph):
    def __init__(self, numVertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(numVertices, directed)
        self.matrix = np.zeros((numVertices, numVertices))
    
    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError('Vertices %d and %d are out of bounds' % (v1, v2))
        
        if weight < 1:
            raise ValueError('An edge cannot have weight < 1')
        
        self.matrix[v1][v2] = weight
        
        if self.directed == False:
            self.matrix[v2][v1] = weight
    
    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError('Cannot access vertex %d' % v)
        
        adjacent_vertices = []
        for i in range(self.numVertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)
        
        return adjacent_vertices
  
    def get_indegree(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError('Cannot access vertex %d' % v)
        
        indegree = 0
        for i in range(self.numVertices):
            if self.matrix[i][v] > 0:
                indegree += 1
        
        return indegree
    
    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]
  
    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i, '-->', v)
    
# adjacency set
class Node:
    def __init__(self, vertexId):
        self.vertexId = vertexId
        self.adjacency_set = set()
    
    def add_edge(self, v):
        if self.vertexId == v:
            raise ValueError('The vertex %d cannot be adjacent to itself' % v)
        
        self.adjacency_set.add(v)
    
    def get_adjacent_vertices(self):
        return sorted(self.adjacency_set)

class AdjacencySetGraph(Graph):
    def __init__(self, numVertices, directed=False):
        super(AdjacencySetGraph, self).__init__(numVertices, directed)
        self.vertex_list = []
        for i in range(numVertices):
            self.vertex_list.append(Node(i))
    
    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError('Vertices %d and %d are out of bounds' % (v1, v2))
        
        if weight != 1:
            raise ValueError('An adjacency set cannot represent edge weights >1')
        
        self.vertex_list[v1].add_edge(v2)
        
        if self.directed == False:
            self.vertex_list[v2].add_edge(v1)
    
    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError('Cannot access vertex %d' % v)
        
        return self.vertex_list[v].get_adjacent_vertices()
  
    def get_indegree(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError('Cannot access vertex %d' % v)
        
        indegree = 0
        for i in range(self.numVertices):
            if v in self.get_adjacent_vertices(i):
                indegree += 1
        
        return indegree
    
    def get_edge_weight(self, v1, v2):
        return 1
  
    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i, '-->', v)

# example to use AdjacencySetGraph
# g = AdjacencySetGraph(4, directed=True)
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(2, 3)

# for i in range(4):
#     print('Adjacent to: ', i, g.get_adjacent_vertices(i))

# g.display()

