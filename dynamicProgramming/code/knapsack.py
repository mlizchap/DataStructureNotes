# recursion - brute force
def knapsack1(profit, weight, capacity):
  def dfs(i, profit, weight, capacity):
    if (i == len(profit)):
      return 0
    
    # without next profit
    maxProfit = dfs(i + 1, profit, weight, capacity)

    # with next profit
    newCapacity = capacity - weight[i]
    # print(newCapacity)
    if (newCapacity >= 0):
      currProf = profit[i] + dfs(i + 1, profit, weight, newCapacity)
      maxProfit = max(currProf, maxProfit)

    return maxProfit
  
  return dfs(0, profit, weight, capacity)

capacity = 8
profit = [4, 4, 7, 1]
weight = [5, 2, 3, 1]

ans = knapsack1(profit, weight, capacity)

# recursion - with memoization

# bottom up approach
# def knapsack2(profit, weight, capacity):
#   currCapacity = capacity
#   result = 0

#   for i in range(len(profit)):
#     currResult = currCapacity - weight[]