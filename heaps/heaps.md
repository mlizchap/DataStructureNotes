## Overview
A heap is a type of binary tree that helps us retrieve a minimum (min heap) or maximum (max heap) in constant time.  It is an implementation of the priority queue.

## Properties
Below are the 2 main properties a heap data structure should have.

### 1. Structural
In order for a tree to qualify as a heap, every row should be completely filled except for the last which must be filled contiguosly from left to right.  

If you look at the following examples, all of the rows are completely filled except from the last which doesn't have any "gaps" within any of the nodes, making it a valid heap.  The second example, however, is not a valid heap due to the "gaps" within the second and third rows.  
[PIC 1]

### 2. Order
The next heap property involves the arangement of the elements.  For a min heap the top element should be the minimum value and then every row below should recursivly be an equal or lower value.  The max heap will have the maximum value at the top and then lower values for each row.
[PIC 2]

## Array Implementation
Heap maps can also be implemented as an array.  When creating an array, we need to start with element 1 in order for the math to work out (will discuss later), the first item in the array will be empty and then starting with the second (index 1), each item will hold a value of the heap starting with the topmost and ending with the last element in the bottom row.
[PIC 3]

Once we have created the array, when given an element index we can determine the parent and children of that element using formulas. 
- **Parent**: i / 2
- **Right child**: i * 2 + 1
- **Left child**: i * 2

For example, in the following heap, given the element 19 (index 2) we can determine that it's parent is at index 1 (2/2), it's left child is at index 4 (2 * 2) and int's right child is at index 5 (2 * 2 + 1).
[pic 4]

## Python Methods
While it is possible to build a heap yourself, Python offers a built in implementation of the datastructure called `heapq`.  The important methods are as follows:
- 

## An example
To illustrate the use of a heap, we'll look at the following example - 


## Implementation
TODO: add note and code for the actual implementation


<!-- PYTHON SPECIFIC METHODS -->

<!-- EXAMPLE -->