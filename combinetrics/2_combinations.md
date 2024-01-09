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

[PIC]

To avoid having duplicates, one thing we can do is go remove the combinations that involve the numbers before our current number. 

With the example `[1, 2, 3, 4]`, for one we would include all numbers.

[PIC]

For `2` we would ignore the combination with 1: 
 
[PIC]
 
For `3` we would ignore combinations with `1` and `2`:

[PIC] 
 
And finally for `4` we would ignore `1`, `2`, and `3` since at this point we already have all possible combinations at this point.

[PIC]

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

[PIC]

### Iterative Approach
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

[PIC]

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

[PIC]

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

[PIC]