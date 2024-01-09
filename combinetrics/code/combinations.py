# Given a number, return all possible combinations of 1 -> n of size 2, including duplicates
# example: n = 3, [1, 2], [1, 3], [2, 1], [2, 3], 
def combinations1(n):
  result = []

  for i in range(n):
    for j in range(n):
      if (i != j):
        result.append([i, j])


# Given an array, return all possible combinations of size 2. Do NOT include duplicates.


# Given an array, 

