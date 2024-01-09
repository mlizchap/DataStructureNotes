## Overview
Combinations deals with all the possible ways we can group items given a certain length.  

## Combinations of Size 2
For example lets say we have the numbers `[1, 2, 3, 4]` and we want to find all possible combinations of length `2`.  First let's examine a naive approach. For each number we'll grab the other numbers in the array to put at the second index.  
```python
def combinations1(n):
  result = []

  for i in range(1, n + 1):
    for j in range(1, n + 1):
      if (i != j):
        result.append([i, j])

  return result
```

For example, for 1 we'll have `[1, 2]`, `[1, 3]`, `[1, 4]`. For 2 we will have `[2, 1]`, `[2, 3]`, `[2, 4]`, etc. Looking at this approach we can see there are many duplicates since order does not matter.  

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/f3c0dbcb-14c3-4564-8657-93caec19413c)


To avoid having duplicates, one thing we can do is go remove the combinations that involve the numbers before our current number. 

With the example `[1, 2, 3, 4]`, for one we would include all numbers.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/4317f0dd-91a1-42a9-972d-1c5f2beb823b)


For `2` we would ignore the combination with 1: 
 
![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/7b8a3bf0-5fab-4071-8c37-14eb4b4bbcc8)

 
For `3` we would ignore combinations with `1` and `2`:

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/792272db-a4ba-4854-aba5-38837df5dc46)

 
And finally for `4` we would ignore `1`, `2`, and `3` since at this point we already have all possible combinations at this point.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/f4ba3c58-082c-4448-9832-92fd1ec0a8e4)


The code would look something like this:
```python
def combinations2(n):
  result = []

  for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
      result.append([i, j])
  
  return result
```

## Combinations of Size K
Next let's add a layer of complexity to the problem and make the output size a variable instead of 2.  Looking at our example `[1, 2, 3, 4]` we'll get all possible combinations of size 3 instead of 2 without duplications.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/0e4e9a3a-e89d-4af5-9a0b-1a2a308b0816)

### Recursive Code
At this point recursion might be the most elegant solution but before we get there let's look at the problem iteratively.  We'll create an inner dfs function that takes in an index and an array conisting of our current combination that we will eventually push to an outer result array.
```python
def combinations(n, k):
  result = []
  dfs(ind, currComb)
  return result
```

Next let's look into our dfs function and create a base case.  When the length of the current combination is equal to K. At this point we'll push our current combination to our result
```python
def dfs(ind, currComb)
  if (len(currComb) == k):
    result.append(currComb)
    return
```

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/afdc1b46-c3bc-43b5-a7b1-aaa0fb36b094)


Next, let's look at our for loop.  
- outer loop: in this loop we'll start with 1 and go to n.
- inner loop: this will consist of our callstack, we'll start with whatever index we're on and end when we get to k.  

```python
def dfs(ind, currComb)
  # ...

  # outer loop: will go from 1 -> n
  for i in range(ind, n + 1):
    currComb.append(i)

    # inner loop: will go from 1 -> k
    dfs(i + 1, currComb)
```

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/3b2d4983-47cb-4f2a-b10d-0787f45cf511)


Finally, we need to think about the point where we get to the end of our recursive calls but we want to branch out more in the previous call stack.  This is where backtracking comes in handy. We do this by popping off the last value of our current array.  For example, in our first callstack of dfs([1], 3) -> dfs([1, 2], 3) -> dfs([1, 2, 3], 3) we want to go back to 2 so we can eventually return `[1, 2, 4]` so we'll pop off the last value `3`.
```python
def dfs(ind, currComb)
  # ...
  for i in range(ind, n + 1):
    currComb.append(i)
    dfs(i + 1, currComb)
    # backtrack to get to previous callstack
    curr.pop()
```

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/e7f9fe31-c176-4eb6-991f-8db267c6b209)
