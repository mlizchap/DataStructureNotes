
## Overview
Dijkstras algorithm is similar to BFS but deals with weighted paths.  For example, let's say we have point A and it has 2 seperate paths to B and C.  While it takes just one edge to get to either, the different weights can deal with other factors we want to take into consideration such as time, distance, etc.  

[PIC]

## Implementation
The implementation is similar to BFS, but since BFS involves all of the paths having equal weights we use a queue in this data structure.  When we use weighted paths we want to indicate that some paths have precidence over the other and thus use a priority queue, also know as a heap, over a regular queue.

[PIC]

For this example we'll look at a weighted graph and get the shortest path from A to each of the nodes.

[PIC]

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
- create an adjacency map -> key: source, value: [destination, weight]
- create a heap and add the starting source to it with a weight of 0
- create an empty map for the shortest values -> key: source, value: shortest weight from source (note: will start out empty)
- while loop: (while the min heap contains values)
  - pop off the min value, if the value is not in the shortest map, add it
  - get the neighbors of the values popped off and add the value of the popped heap + the neighbors weighted value and add to heap (will repeat this cycle)
- return the values in shortest map

## Illustrative Steps
1. Make an adjacency map
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





  