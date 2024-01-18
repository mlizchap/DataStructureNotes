
## Overview
Dijkstras algorithm is similar to BFS but deals with weighted paths.  For example, let's say we have point A and it has 2 seperate paths to B and C.  While it takes just one edge to get to either, the different weights can deal with other factors we want to take into consideration such as time, distance, etc.  

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/9d9229f2-3b10-4c7a-8e8e-6c8b720e5fd7)

## Implementation
The implementation is similar to BFS, but since BFS involves all of the paths having equal weights we use a queue in this data structure.  When we use weighted paths we want to indicate that some paths have precidence over the other and thus use a priority queue, also know as a heap, over a regular queue.

For this example we'll look at a weighted graph and get the shortest path from A to each of the nodes.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/82baaa21-74b8-4288-990d-0e0966166a4a)

The answers will be as follows:
```
A: 0
B: 7
C: 3
D: 11
E: 5
```

Let's take a look at how we get this answer.

## Steps
- Create an **adjacency map** consisting of each nodes neighbors and weights
  - key: source
  - value: [destination, weight]
- Create a **min heap** that will contain the shortest paths at the top
  - each node will consist of: `<source, weight>`
  - add the starting source to it with a weight of 0
- Create an empty **shortest values map**
  - key: source, value: shortest weight from source (note: will start out empty)
- Begin a **while loop**: (while the min heap contains values)
  - pop off the min value, if the value is not in the shortest map, add it
  - get the neighbors of the values popped off and add to the min heap
    - add the value of the popped heap + the neighbors weighted value and add to heap (will repeat this cycle)
- Return the values in shortest map

## Illustrative Steps
1.  Create a function consisting that takes in an array of edges, a source, and a number telling us how many nodes are in the graph.  The edge will contain an array consisting of the [0] source, [1], distance and [2] weight.  The source will be the starting node we are trying to get the distances to.


```python
adj = {}

for source, dest, weight in edges:
  if adj.get(source):
    adj[source].append([dest, weight])
  else:
    adj[source] = [[dest, weight]]
```

1. Make an adjacency map.  The keys will be each of their nodes, and the values will be arrays with the first index the neighbor node value and the second index the weight.  For example, A's neighbors are B and C, A to B has a weight of 10 and A to C has a weight of 3.

[PIC]

```python

```

2. Create a min heap and add the starting node as well as create a shortest mapping.  This will eventually hold the shortest weighted paths from each node from the starting node.

3. Create a while loop.  In this while loop we will (1)
```python

```

Let's take a look at what happens in each loop.
Loop 1
We'll check if A is in the shortest map.  It is not so we add it.  We then add it's neighbors to the heap.  Normally we'll add the current weight + the neighbors weight, but since A is 0 we'll just add the B and C values, 7 and 10 respectively.
[PIC]

Loop 2
Next we'll pop from the min heap and get the values `<C,3>`.  C does not have a shortest value so we add it.  





  
