## Overview
Breath First Search (BFS) involves going level by level.  

Given a 2d matrix, we start with the upper lefthand element, get the neighbors of that element and 

## Procedure
In order to iterate through the matrix we need the rows and columns.

Since we are going to iterate through the matrix, we'll need get the amount of rows and columns.
```python
ROWS, COLS = len(grid), len(grid[0])
```

Next we'll create a queue and a visit set.  The visit set will keep track of the nodes visited, while the queue will be used as a way of processing the nodes.
```python
visit = set()
queue = dequeue()
```

We'll start by adding the upper left node of the matrix to the queue.  We'll also add it to the set since we want to add the nodes 
```python
queue.append((0, 0))
visit.add((0, 0))
```
![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/401c47d9-c9af-45e6-b281-a72bb41ee3d4)


Create a while loop in the queue.  Each loop we'll pop off the first element in the queue, get the neighbors and then iterate through the neighbors until all of the elements have been processed.
```python
while queue:
    for i in range(len(queue)):

        # current node
        r, c = queue.popleft()
```
In the current example, since we added `(0,0)` to the queue we'll process that first.  


We'll take the node that we just popped and get all of it's neighbors. In the case of going up, down, left, right we'll add 1 or -1 to each row and column.
```python
neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
```
![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/1e5936f5-0fd5-40bf-9831-3179b654df94)


Going left and right will either result in (1) an out of bounds direction, (2) hit a visited node, or (3) give us another node for the queue. In cases of the out of bounds or visited node, we'll want to break out of the loop.  Otherwise, if we hit a valid node, we'll want to add that node to the queue and visit set.
```python
for dr, dc in neighbors:
    if (
      # (1) out of bounds
      min(r + dr, c + dc) < 0 
      or r + dr == ROWS
      or c + dc == COLS

      # (2) a visited node
      or (r + dr, c + dc) in visit:
    ):
      continue
      
      # (3) hit a valid node, add to the queue and visit set
      queue.append((r + dr, c + dc))
      visit.add((r + dr, c + dc))
```

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/faf07156-f03e-4096-ad10-b45ace73f484)

In the pic above, going up or left will result in out of bound locations, while right and down will reach the neighbors `(0,1)` and `(1, 0)`. We will add these nodes to the visited set and add them to queue.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/2b2c319f-6e89-45d4-a944-3e359d8b1356)

We'll then make another loop and process the items in the queue.  

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/536de8a2-bd45-447f-9798-745ad5ea716c)

In order to traverse the entire graph, we'll continue this process until we get to the end of the queue.  By the time we get to `(2,2)` it's neighbors all of it's neighbors will be visited, causing us to have nothing to add to the queue and break out of the loop.