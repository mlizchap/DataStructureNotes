## Subsets
Subsets deals with taking a set and determining the potential subsets of that set.  According to set theory we must take into consideration the following factors:
- a subset can be empty
- a subset can (usually) not have dups
- the order doesn't matter

For example, `{}` is a valid set and `{1, 2}` is the same as `{2, 1}`.

Let's look at the following subset `{1, 2, 3}` and lets say we want to get a set consisting of all the possible subsets (a.k.a. the power set).  We would get the following solution: `{{}, {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}}`.  Let's look at a way to arrive at this solution by creating a decision tree. 

Since an empty set can be a subset of any set we'll start with that.  From there we will create branches for only the first item in the set, `1`.  For this branch we will either add 1 to the set or not add 1.  So the power set of `{1}` will be either `{}` or `{1}`.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/be5cccba-5e76-46ca-851e-f3c3533fa5b9)

Next let's compound our previous work to get the second item in the set, `{2}`.  For every set in the previous set, we'll either add 2 or not have 2.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/197b0880-53e1-427a-9732-26df9d45b61e)

Finally, we'll take our sets from the previous example and either add `{3}` or not add `{3}`. Since this is the last number in the set, the last branch will represent all possible sets.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/6eec019b-36e6-4847-9e08-666024a3ba06)


Note that each item in the set will have 2 possibilities and then those possibilities compound upon one another.  Because of this this means there will be 2^n possibilities.  So in the exampe `{1, 2, 3}` there are 8 possibilities (2^3).

## Code
Now let's look at how to code this.  We'll look at this example - https://leetcode.com/problems/subsets, where we take in an array and then find all the possible subsets of that array. We can either code out the iterative or recursive approach.

### Recursive
For the recursive approach we'll start with an empty set, or an empty array, and then iteratively add to the array.  To know which item to add to the array we'll keep track of an index.
```python
def subsets(arr):
  result = []

  # helper function to recursively build up the sets
  def dfs(arr, ind):
    # recursively iterate through the array here
    # ...

  dfs([], 0)
  return result
```
Next we'll want to recursively build the potential sets using the helper dfs function. We'll update the array by adding another item using the index.  Increment the index to have the next index for the next callstack.
```
def dfs(arr, ind):

```
![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/7f21cf64-5243-41dc-98fd-c9cc8f30a467)

We can't have a recursive function without a base case so let's add that.  We'll want to end when the callstack when the length of the array equals the size of the original set.  After we reach this point we'll use backtracking and traverse through the callstack to reach our final answer.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/d71c475b-999d-4c41-a6dc-0efd5b1fd820)

Let's consider the base case
```python
def subsets(arr, ind):
  # BASE CASE
  if (ind == len(arr):
    result.push(arr)
    return
  
  arr = arr + [arr[ind]]
  ind += 1
  dfs(arr, ind)
```

With our currently algorithm for each level we only have one item.  We want to update that to where for each item added we'll have 2 options, to add the new item or to not add it.  We can achieve this through backtracking.  After the first recursive call, when we have exhausted all of our options, we'll pop from our current array to get the option without the item.  Notice how the calls look the same but they will achieve different results due to the popping of the array.

```python
def subsets(arr, ind):
  # ...

  dfs(arr, ind)
  # BACKTRACK
  arr.pop()
  dfs(arr, ind)
```

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/8a04cad6-0b32-4601-bbc6-03463e7d97d4)

Finally, after the callstack is finished calling, we'll exit out of the function and return the result.  Notice how the end result will be the values at the bottom of the tree.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/cc68cbb6-2b85-4e71-9981-6e4636f15003)

## Iterative
Next let's look at the iterative approach.  This one is a little more straight forward in my opinion.  We'll create a result array and begin with an empty set. We'll then iterate the length of the array and each iteration we'll also loop through the items in our result.  Since Python's arrays are by reference we'll want to create a copy of it before we loop through it.  

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/f8d3257d-a01e-4884-adef-8850ff886b4d)

Notice how each iteration we'll take a copy of our previous result and either keep the item or make a new array with the new item until we get our final result.
