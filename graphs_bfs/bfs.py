"""
Example: shortest path, 
- Given a M X N matrix, determine the shortest path from the upper right element to the bottom left.  
- A 1 represents an item you cannot travel across, 0 is ok
0 0 1
0 1 1
0 0 0
- Has one shortest path
"""
from collections import deque
def shortestPath(grid):
  # define the rows and columns
  ROWS, COLS = len(grid), len(grid[0])

  # create the set for keeping track to of the visited items
  visit = set()

  # create the queue for going thru the items level by level
  queue = deque()

  # go through the queue, each loop is a level
  level = 0
  while queue:
    
    # loop thru the queue
    for i in range(len(queue)):
      
      # pop off the next item off
      r, c = queue.popleft()

      # if we're at the last item: return 1 to add to the path
      if r == ROWS - 1 or c == COLS - 1:
        return 1

      # get all the elements neighbors, (up | down | left | right)
      neighbors = [[0,1], [0,-1], [1, 0], [-1,0]]

      # loop through the items popped off
      for dr, dc in neighbors:

        # if the element is out of bounds, visited, or equal to 1, break out of loop
        if (min(r + dr, c + dc) < 0 or
          r + dr == ROWS or
          c + dc == COLS or
          r + dr in visit or
          c + dc in visit or
          grid[r + dr][c + dc] == 1):
            continue
          
        # add the items that are in bound, not visited, and not 1 to the queue
        queue.append((r, c))

        # add the items to the visited set
        visit.add((r, c))

        # each loop represents a level
        level += 1
          

