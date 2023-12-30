## Overview
An adjacency list is using a hashmap or class to organize the neighbors of nodes in a graph and then using the structure to traverse the graph, either through bfs or dfs.

## An Example
Let's look at an example.  Let's say we have a list of edges in a directed graph:
```python
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
```
Since it is directed, A points to B, but B doesn't point to A, etc.

[PIC #1]

## The adjacency map
To build the adjacency list, we can either create a class or hashmap.  For this example, let's use a hashmap.  We'll want to add all of the nodes to the hashmap.  For the first elements, we'll add the element it is pointing to to an array.  Since it is a directed graph, we'll add the second element, but we won't add any items to the array.
```python
# the hashmap
adjList = {}

for src, dst in edges:
    # we'll create both nodes as values in the list
    if src not in adjList:
        adjList[src] = []
    if dst not in adjList:
        adjList[dst] = []
    # since the graph is directed, we'll only add the value of the neighbor to the list 
    adjList[src].append(dst)
```

As mentioned earlier, we can perform either dfs (depth first search) or bfs (breath first search). Lets look at both in the example.

<!-- DFS EXAMPE -->

<!-- BFS EXAMPLE -->
