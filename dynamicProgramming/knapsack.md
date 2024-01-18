## The problem
The knacksack problem involves inputs of a maximum capacity and 2 corresponding arrays, one being the profit and the other being the weight.  We can use each item 0 times or one time.  We return the max profit number.
```
captity = 8
weight = [4, 4, 7, 1]
profit = [5, 2, 3, 1]
```

## Recursive - Brute Force
One way to think of this problem is to create a decision tree. You can either add an item or not add an item.  For example, when looking each item we have the decision to either add it or not add it.

[PIC]


### Code
To start the code we'll want to create a function that accepts the profit, weight, and capacity.  For this example we'll use recursion and each time change the index and capacity, so we'll have an inner function that accepts the same args but just change the capacity.  Outside of the inner call we'll 

```python
def knapsack(profit, weight, capacity):
  def dfs(ind, profit, weight, capacity):
    # inner code here

  dfs(0, profit, weight, capacity)
```

Next let's look at the base case.  Each time we go down the tree we will go to the next index in the array and stop when we are out of bounds.  We will return 0 since we are not at a valid profit number.
```python
def dfs(ind, profit, weight, capacity):
  if (ind == len(profit)):
    return 0
```

Next let's look at the code to not add the number.  In this example everything will stay the same except for the index.  Since the result of the recursive call will return the profit, we'll assign the value of the function call to a variable we'll call `maxProfit`.
```python
def dfs(ind, profit, weight, capacity):
  # ...
  maxProfit = dfs(ind + 1, profit, weight, capacity)
```

We'll then want to recursively see what happens when we add an additional item at each recursive call.  To do this we'll first subtract the item's weight from the capacity to get what would be the newCapacity.  We only want to end up making this call if the newCapacity is less than or equal to the current capacity so we'll do a check first.
```python
def dfs(ind, profit, weight, capacity):

  # ...
  newCapacity = capacity - weight[ind]
  if (newCapacity <= capacity):
    # make call here
```

Now let's think of the call we want to make.  The arguments that will change will be the index, just as in our previous call and in addition the newCapacity will be passed in as the capacity.
```python
def dfs(ind, profit, weight, capacity):
  # ...
  if (newCapacity <= capacity):
    dfs(ind + 1, profit, weight, newCapacity)    
```

Next we want to figure out our new profit.  Since we recursively return the maxProfit, assign the result of the function call plus the profit at our new index. We'll then get the max of this profit and our previous profit and return this value. 
```python
def dfs(ind, profit, weight, capacity):
  # ...
  if (newCapacity <= capacity):
    p = profit[ind] + dfs(ind + 1, profit, weight, newCapacity)    
    maxProfit = max(maxProfit, p)

  return maxProfit
```