## Overview of Each
<!-- describe subsets, combinations, permutations -->

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
Now let's look at how to code this.  We can either code out the iterative or recursive approach.

### Recursive
For the recursive approach we'll start with an empty set, then we'll either 
