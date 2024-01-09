# Given a number n, return all possible combinations of 1 -> n of size 2, including duplicates
# example: n = 3, [1, 2], [1, 3], [2, 1], [2, 3], 
def combinations1(n):
  result = []

  for i in range(1, n + 1):
    for j in range(1, n + 1):
      if (i != j):
        result.append([i, j])

  return result

# Given a number n, return all possible combinations of 1 -> n of size 2. Do NOT include duplicates.
def combinations2(n):
  result = []

  for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
      result.append([i, j])
  
  return result

# Given a number n, return all possible combinations of 1 -> n of size k. Do NOT include duplicates.
def combinations3(n, k):
  result = []
  def dfs(i, currComb):
    if len(currComb) == k:
      result.append(currComb.copy())
      return
    
    # if (i > n):
    #   return
    
    for j in range(i, n + 1):
      currComb.append(j)
      dfs(j + 1, currComb)
      currComb.pop()
  dfs(1, [])
  return result

t = combinations3(4, 5)
print(t)
