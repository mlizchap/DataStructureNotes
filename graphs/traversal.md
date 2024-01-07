## Overview
Let's look at 2 common ways to traverse a graph - DFS and BFS.  Graphs are a network of nodes and it is important to have ways of determining the relationships between these nodes and potentially go from one node to the next.

## DFS vs BFS
Depth first search goes level by level while breadth first search visits neighboring nodes before going to the next level.

[PIC]

While the order of directions are different, both methods involve traversing from one node to the next.

Both methods usually involve having some sort of visit set.  This helps us keep track of nodes visited to avoid visiting a node more than once.

### DFS
DFS is usually done in a recursive manner, each callstack contains the potential directions a node can have.  We'll first create our base cases, indicating that a direction is no longer valid or we have reached our destination.  If none of the base case criteria is met, we'll move along to adding the node to the visit set and then recursively calling the dfs functions for our neighboring nodes.  

In the example below, we'll travel as far down as we can before attempting the other directions.
```python
def dfs(grid, r, c, visit):
    # base cases: out of bounds, visited, destination reached, etc.

    visit.add((r, c))

    count = 0

    # potential directions we can travel, in this case it's up, down, left, right
    count += dfs(grid, r + 1, c, visit) # DOWN
    count += dfs(grid, r - 1, c, visit) # UP
    count += dfs(grid, r, c + 1, visit) # RIGHT
    count += dfs(grid, r, c - 1, visit) # LEFT

    # for backtracking
    visit.remove((r, c))

    # final count
    return count
```
Note that in this example we have a method to remove the current node from the visit set after all of the dfs functions are called.  For example, let's say we traverse the following graph and hit a deadend when we go down. At our current spot, if we go left or down we will be out of bounds. The right node is a blocking node so we are unable to go there.  By removing the current node we'll be able to go back to a previous callstack to examine potential options.

[PIC]

TODO: Write about the count variable

### BFS
Next let's look at BFS.  Unlike DFS which involves going deep before going wide, we'll want to traverse wide before going deeper into the graph.  This implementation usually involve some sort of queue.  

We'll first create a queue and add the first node to the queue.  We'll then create a while loop and keep it iterating as long as the queue has values.  Each iteration involves popping off the nodes in the queue, processing these nodes, and then adding back the potential valid neighboring nodes.

[PIC]

```python
# Shortest path from top left to bottom right
def bfs(grid):
    # create a queue and set, add first item to each

    length = 0
    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            # 1. process current node (r,c) here

            # 2. get the valid neigbors and add to queue
            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]] # potential directions
            for dr, dc in neighbors:
                # if the direction leads to an invalid position - continue

                # else: add node to queue and visit set
                queue.append((r + dr, c + dc))
                visit.add((r + dr, c + dc))
        
        # each while loop represents a level in the graph
        length += 1
```

## Example: Number of Islands
Let's look at a common algorithm and examine how we could solve it with both DFS or BFS - https://leetcode.com/problems/number-of-islands/.  In this problem we are given an m X n matrix with 0 and 1 values.  The 1 represents land and the 0 represents water.  We want to return the number of islands.  An island is connected by 1s either horizantally or vertically and is surrounded by water and/or the border.

[PIC]

Both methods have similar concepts.  We'll want to traverse the grid and look for a "1" value that has not been visited. Once we find a valid one 

```python
# create a bfs or dfs helper function.  This function takes in a row and columns and traverses the graph by visiting the neighboring 1s and adding them to a visit set.  Once all of the valid ones have been visited, we'll return 1.

def numberOfIslands(matrix):
  # create variables for visited, numbOfIslands, and the rows and column indexes
  # traverse the grid and find a 1 that has not been visited
    # use this value to enter the bfs or dfs helper function
    # add one to numOfIslands after exiting the function
  # return the number of islands
```

## Adjacency Lists
An adjacency list is a way of mapping a nodes relationship to other nodes.  This list usually consist of a hash map with the key being the vertex of a node and the values being the vertices the node is connected to.  

[PIC]

This map tells you which neighboring nodes you can traverse to.  In the previous example, number of islands, we are given a matrix and we are not always sure which direction is a valid direction.  With adjacency lists we do not have to worry about these boundaries.

### BFS


