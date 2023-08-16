Plural sight work with graph algo in python

https://app.pluralsight.com/courses/a1891cae-aa6b-4522-843d-ea1442e9386e/table-of-contents

## Establishing precedence
Topological sort
* any ordering of all the graph's vertices that satisfies all precedence relationships

DAG -> Directed Acyclic Graphs
DAGs specify precedence relationships between nodes (no cycle)
* scheduling tasks 
* evaluating expressions
* building neural network models
* computation graphs in neural network

#### Topological sort algorithms O(V+E)
in-degree of a node is the number of directed edges that "directly flow" into that node
1. calculate the node in-degree
2. starts from node has in-degree == 0 
   (if no node has in-degree == 0, graph has a cycle)
3. remove and the node and decrement the in-degree table
4. repeat step 2


## Getting from point A to B
(deliveries from warehouse to customer)

unweighted graphs vs weighted graphs

edge weight determine the cost of a path

### shortest path algorithm
* if all edge weight are equal, use the unweighted shortest path algorithm, find smallest number of hops

working out the distance table for each node

| Node | Distance | Preceding Node |
| ---- | -------- | ---------  |
| A | 0 | A
| B | -1 | - 

distance table -> 3 column array
backtracking -> stack

adjacency matrix -> O(v^2)
adjacency list or set -> O(V+E)

### Dijkstra's algorithm
* if edge weights are unequal, use Dijkstra's algorithm

use distance table and distance is the weight, start from Inf

Queue is priority queue \
Enqueue immediate neighbors in "decreasing order of distance"


## Covering all nodes in a graph
minimal spanning tree
(planning railway lines)

what is spanning tree
* edge = vertex - 1
* can not have cycles
* fully connected 

what is minimum spanning tree of graph
* spanning tree with the lowest weight

#### Algorithm
spanning tree algorithm seek to find the shortest way to cover all nodes

* Prim's algo works for connected graphs (greedy algo)
  Implementation heavily from Dijkstra's algorithm \
  Requires priority queue to find edge with least cost \
  Distance table but with edge weight as the distance \

* Kruskal's algo works even for disconnected graphs






