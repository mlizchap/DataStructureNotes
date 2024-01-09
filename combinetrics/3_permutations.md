## Overview
Permutations involve taking a list of numbers and rearranging them to get every possible order of those numbers.

## Process
Let's look at the example of getting all the possible permutations of 1, 2, 3.  We'll start with 1 and work our way up.  1 is the only permution we have of 1 so we don't need to do anything to it.  Next we'll take 2 and get all the permutations of 1 and 2 and end up with 1,2 and 2,1, we get this by adding 1 to the beginning and end of 2.  Finally when adding 3 we'll add it to the beginning, middle, and end of 1,2 and 2,1 resulting in [3,1,2],
[1,3,2], [1,2,3], [3,2,1], [2,3,1], [2,1,3].

[PIC]

## Recursive Algorithm
Let's look at the example [1, 2, 3] again.  Iterativlely call the number of items until we reach the last item.  

```python
def permutations(nums):
    def helper(i):   
      if i == len(nums):
          return [[]]
      
      resPerms = []
      perms = helper(i + 1)
```

[PIC]

At the top of the callstack we have an empty array and then we'll slowly go down the callstack as we build up this array even more. We'll iterate through the current array items, make a copy of each, and then add each new number to each index of the array.  
```python
def helper(i):   
  # ...
  resPerms = []
  perms = helper(i + 1) # will be [] at the top of the callstack and then build out as we go down 
  for p in perms:
      for j in range(len(p) + 1):
          pCopy = p.copy()
          pCopy.insert(j, nums[i])
          resPerms.append(pCopy)
  return resPerms
```

[PIC]