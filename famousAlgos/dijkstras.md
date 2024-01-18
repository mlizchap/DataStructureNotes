
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
1.  Create a function consisting that takes in an array of edges. Each edge will contain an array consisting of the [0] source, [1], destination and [2] weight.  The source will be the starting node we are trying to get the distances to.


```python
adj = {}

for source, dest, weight in edges:
  if adj.get(source):
    adj[source].append([dest, weight])
  else:
    adj[source] = [[dest, weight]]
```

When calling our current example it will look like this:
```python
shortestPaths(
  # edges
  [["a", "b", 10], ["a", "c", 3], ["b", "d", 2], ["c", "b", 4], ["c", "e", 2], ["c", "d", 8], ["d", "e", 5]],
  # source
  "a"
)
```

2. Next we'll make an adjacency map.  The keys will be each of their nodes, and the values will be arrays with the first index the neighbor node value and the second index the weight.  For example, A's neighbors are B and C, A to B has a weight of 10 and A to C has a weight of 3.  Then add do B's neighbor's which is D which has a distance of 2, and so forth.  Also keep in mind that we want to add both the sources and the edges to the adjacency list, not all nodes will have a connecting node (in our case `E`) but we still should add the node to the map with an empty value.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/f56bab02-8838-4168-b4d5-8c365263bb2b)

```python
# create an empty adjacency map
adj = {}

# loop through the edges
for source, dest, weight in edges:
  # since we want to include both the sources and edges in our adj map 
  if not adj.get(dest):
    adj[dest] = []
  # add the source with it's destination and destination's weight value to the map
  if adj.get(source):
    adj[source].append([dest, weight])
  else:
    adj[source] = [[dest, weight]]
```

2. Create a min heap and add the starting node.  This will eventually hold the shortest weighted paths from each node from the starting node.  Note that we want to add the weight first so the minHeap will be populated based on the weight value.
```python
minHeap = [[0, src]]
```

3.  Next we'll create a hash map consisting of the shortest paths to the souce node.  This will start out empty but eventually the key will be the node and the value will be the shortest weighted path to a.
```python
shortest = {}
```

5. Create a while loop.  In this while loop we will:
   (1) pop the min value from the min heap
   (2) check if the min value is in shortest,
     (3) if yes continue,
     (4) if no:
       (5) add the 
   
```python
while minHeap
  # (1) pop the min value from the heap
  weightPopped,nodePopped = heapq.heappop(minHeap)

  # (2) check if popped is in shortest
  if nodePopped in shortest:
    # (3) if yes continue
    continue
  # (4) if not in shortest:
  # (5) add it
  shortest[nodePopped] = weightPopped
  # (6) add it's neighbors to the heap,
  for neighborNode, neighborWeight from adj[nodePopped]:
    # if not in shortest add 
    if neighborNode not in shortest:
      # weight: nodePopped + the neighbor node's weight
      # value: the neighbor nodes' value
      heapq.heappush(minHeap, [adj[weightPopped] + neighborWeight])
```

6. Finally, we'll return the shortest map consisting of the nodes and their corresponding shortest distance to the source passed in.
```python
return shortest
```

## Iterations
Let's take a look at what happens in each loop.
### Loop 1
Entering the first loop our min heap consists of the source node and it's distance of 0 since there is no distance to itself.  Since the shortest map is empty we'll add it to the map.  After we'll grab the neighbor's from A and add their weight's.  Normally we add the popped nodes weight, but in this case the popped node's weight is 0 so the neighbor's weights added to the min heap will be there original weights.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/00683440-e7f4-4809-aedf-99f27bf39403)

### Loop 2
On the second while loop we'll once again pop from the min heap.  This time the node will be C since C's weight of 3 is less than B's weight of 10.  There is no C value in the shortest map so we'll add C to it with a value of 3.  Next we'll add C's neighbor's to the heap.  C has 3 neighbors - B, E, and D. Notice how the heap is rearranged to keep the properties of the heap up to date with the minimum value on top among other things.  Also note that for each of the neighbor's nodes we'll add C's weight of 3 for their total.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/6a67a1f3-36a5-46fd-8cf7-d549efa14419)

### Loop 3
Next we pop off the minimum value E from the heap.  E is not in the shortest map so we add it.  Since E does not have any neighbors to add, the heap will rearrange and <7, B> will be at the top.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/dde94e58-714f-4f86-96fb-973600a9d6a7)

### Loop 4
Now we will pop `<7, B>` from the heap and add it to shortest.  D is B's only neighbor we need to add so we'll add B's weight plus the weight for D to get a total of 9.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/8cb8f423-92cf-4036-be99-9f1d948c760b)

### Loop 5
We now pop `<9, D>` from the heap and add 9 to D's value since it is not in the shortest map.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/531ad68e-d7d3-4d77-86b8-b90ef68bf069)

At this point we have all the values in filled out.  All the while loops going forward will not be continued because of the check in the shortest map will return True and break from the loop.  We can now return the shortest map.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/d25fc022-5602-41d6-8ed6-260e1bd01486)








  
