## Overview
An adjacency list is using a hashmap or class to organize the neighbors of nodes in a graph and then using the structure to traverse the graph, either through bfs or dfs.

## An Example
Let's look at an example.  Let's say we have a list of edges in a directed graph:
```python
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
```
Since it is directed, A points to B, but B doesn't point to A, etc.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/0a26cd04-ea88-4fa5-9f97-0e8a7efb3135)


## The adjacency map
To build the adjacency list, we can either create a class or hashmap.  For this example, let's use a hashmap.  We'll iterate through the array and create keys for all of the values, both the source and distribution.  We'll map the destination values to the sources.  If an item is a destination but not a source, it will have an empty array for it's value.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/1424b81d-826b-4335-95af-e060daa083a9)



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

## DFS 
Let's look at an example where we want to find the possible paths to a target.  We'll use the graph above and try to find the possible paths from A to E.  As you can see below, there are 2 possible paths.  You can go A -> B -> C -> E or A -> B -> E.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/bebb5a0b-9613-4640-ba7d-241263e3289f)


```python
# Count paths (backtracking)
def dfs(node, target, adjList, visit):
    if node in visit:
        return 0
    if node == target:
        return 1
    
    count = 0
    visit.add(node)
    for neighbor in adjList[node]:
        count += dfs(neighbor, target, adjList, visit)
    visit.remove(node)

    return count
```

The DFS function we will implement will be a recursive call.  We'll start with A and then visit's A's first neighbor B.  Next we'll look at B's first neighbor C.  After we'll go to C's neighbor E.  Notice how if a node has multiple neighbors, we'll first visit the descendents before the sibling nodes.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/a38d1258-52c5-49b7-b2c6-60d38d7542f1)


```python
count = 0
for neighbor in adjList[node]:
    count += dfs(neighbor, target, adjList, visit)
return count
```

We'll also want to use a visit set.  We'll add to the set to prevent visiting the same node twice, and then once all paths are exhausted on a node, we'll remove from the set so we can backtrack.
```python
    visit.add(node)
    for neighbor in adjList[node]:
        count += dfs(neighbor, target, adjList, visit)
    visit.remove(node)
```

Finally, we'll add our base case.  We want to stop when we either hit our target or hit a node that has been visited.
```python
# Count paths (backtracking)
def dfs(node, target, adjList, visit):
    if node in visit:
        return 0
    if node == target:
        return 1
```

The following illustration shows how we go from A to our target and then backtrack in order to reach the target a second time.  As the name implies, we go as deep as possible to reach our target and then backtrack to visit nodes that have unvisited neighbors.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/d8a4a8d9-b560-49b1-9b5f-294fe3a5db7b)

## BFS
Next let's look at an example that uses BFS.  This problem will involve determining the quickest route from A -> E.  Unlike depth first search where we go as deep as possible first, this algorithm will involve going level by level.  To do this we'll create a queue, start with the first node, and while the queue is not empty we'll add and process nodes in teh queue. We'll also use a visit set to keep track of the nodes that have already been visited.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/a428bbb0-75e1-4aae-9160-46474caf49e7)


```python
def bfs(node, target, adjList):
    # create a queue and visit set, add the first node to each
    length = 0
    visit = set()
    visit.add(node)
    queue = deque()
    queue.append(node)

    # while there are items in the queue, pop off the nodes, process the node, and then add the node's neighbors
    while queue:
        for i in range(len(queue)):
            curr = queue.popleft()

            # return the graph length if we reach our goal
            if curr == target:
                return length

            for neighbor in adjList[curr]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)
        length += 1
    return length
```
