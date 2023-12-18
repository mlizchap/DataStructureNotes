## Overview
DFS involves going one direction at a time in order to traverse the graph.  Usually done in a recursive manner.

## Steps
For this example we'll explore an algorithm that takes a matrix and determines the number of possible unique paths from the upper left corner to the bottom right corner.  You can go from one square to the next if it's directly above, below, to the left, or to the right AND a "0" value.  In the following example, the number of unique paths are 2.
[PIC #1]

Let's create the boundaries for the grid.  In order to get the bottom outer bounds, we'll get the rows and columns and then identify our boundries. 
```python
ROWS, COLS = len(grid), len(grid[0])
```

 Next we need to write out all of the possible ending outcomes for the paths. These will be the base cases. They will be (1) if the row or column indexes are out of bounds (2) if we reach a visited node (3) if we reach a one, or (4) if we reach our destination - the bottom right corner.
```python
if (
    # out of bounds
    min(r, c) < 0 or
    r == ROWS or c == COLS or
    # in the visit set
    (r, c) in visit or
    grid[r][c] == 1
  ):
    return 0
# we're at the last node (bottom right)
if r == ROWS - 1 and c == COLS - 1:
    return 1
```
Next we want to add the row and column that we are currently on to the visit set. 
```python
visit.add((r, c))
```

Next we'll set our count to 0.  We then create our recursive calls.  In this example we'll be going left, right, up, and down, so 4 calls in total. 
```python
count = 0
count += dfs(grid, r + 1, c, visit)
count += dfs(grid, r - 1, c, visit)
count += dfs(grid, r, c + 1, visit)
count += dfs(grid, r, c - 1, visit)
``` 

Let's look at a decision tree representation of this problem. For each node, starting with the upper left `(0,0)`.  The base cases are the conditions described above. For each direction we will recursively go in that direction until we reach a base case. 

[PIC 4]


Now let's look at the actual decision tree.  We'll first start with the actual tree paths of our problem.  Starting with `(0,0)` we'll branch out into our four directions - down, up, right, and left.  Since the down and up directions are invalid (out of bounds and a `1`), we'll go to the right.  Note that if either of the first 2 were valid we would go deeper in the tree before going wide since this is depth first search.
[PIC 3]

Since `(0,1)` is valid we'll recursively look into this node's options.  first we'll go to `(1,1)` since the down direction is first.  We first look at `(2,1)`, which is out of bounds. `(0,1)` is visisted so we reach a dead end there and `(1,0)` is a 1 so we stop there.  This leaves us to the final direction which is `(1,2)`.  Since this is the bottom, right node we'll return 1 since we reached our final desitination.

[PIC 5]
Now that we're at the end of the path, we'll want to backtrack in order to find other potential paths.  We do this by removing the current node from the visited list after all the available paths are exhausted.  

```python
count = 0
count += dfs(grid, r + 1, c, visit)
count += dfs(grid, r - 1, c, visit)
count += dfs(grid, r, c + 1, visit)
count += dfs(grid, r, c - 1, visit)

# backtrack
visit.remove((r, c))
```

In this example we'll go back to `(1,1)`.  All of the paths are not available here so again we will backtrack again to `0,1`.  
[PIC #7]

Since we are going down first, we'll look at `0,2`.  This node is in bound and not visited so we'll countinue here.  Finally we see we are at a bottom right node so we'll end here.  After a few more backtracking rounds, we'll realize we have exhausted all options and return 2 as our answer.
```python
count = 0
count += dfs(grid, r + 1, c, visit)
count += dfs(grid, r - 1, c, visit)
count += dfs(grid, r, c + 1, visit)
count += dfs(grid, r, c - 1, visit)

# backtrack
visit.remove((r, c))
return count
```
[PIC #8]
