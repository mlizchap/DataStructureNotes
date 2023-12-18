"""
Description: return the []
args: matrix
return: the number of possible paths


                     0,0
              /    /     \
            1,0  -1,0    0,-1      
"""

# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

def numberPaths(grid):
  # dfs helper function
  def dfs(grid, r, c, visit):
      # get number of rows, columns to determine boundries
      ROWS, COLS = len(grid), len(grid[0])
      print(r, c)
      if (
          # out of bounds
          min(r, c) < 0 or
          r == ROWS or c == COLS or
          # in the visit set
          (r, c) in visit or 
          # equal to 1
          grid[r][c] == 1
        ):
          return 0
      # we're at the last node (bottom right)
      if r == ROWS - 1 and c == COLS - 1:
          return 1

      # add the visited to the set
      visit.add((r, c))

      count = 0
      # go all the way down, each node will be added to the visit set
      count += dfs(grid, r + 1, c, visit)
      # go all the way up, each node will be added to the visit set
      count += dfs(grid, r - 1, c, visit)
      # go all the way right, each node will be added to the visit set
      count += dfs(grid, r, c + 1, visit)
      # go all the way left, each node will be added to the visit set
      count += dfs(grid, r, c - 1, visit)

      # at this point we are at a node that has reached the end or has exhausted all options, we need to backtrack
      visit.remove((r, c))
      return count

  return dfs(grid, 0, 0, set())

numberPaths(grid)
