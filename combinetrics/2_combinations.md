## Overview
Combinations deals with all the possible ways we can group items given a certain length.  

## Combinations of Size 2
For example lets say we have the numbers `[1, 2, 3, 4]` and we want to find all possible combinations of length `2`.  First let's examine a naive approach. For each number we'll grab the other numbers in the array to put at the second index.  
```python
def combinations(n):
  result = []

  for i in range(n):
    for j in range(n):
      if (i != j):
        result.append([i, j])
```

For example, for 1 we'll have `[1, 2]`, `[1, 3]`, `[1, 4]`. For 2 we will have `[2, 1]`, `[2, 3]`, `[2, 4]`, etc. Looking at this approach we can see there are many duplicates since order does not matter.  

[PIC 1]

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

```

## Combinations of Size K