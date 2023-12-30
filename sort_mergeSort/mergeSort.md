## Overview
Merge sort involves recursively breaking down the array until it is 1 element and then building the array back up.

## Breaking Down the Elements
To break down the array, we'll start with the array and then continuosly change the start, middle, and end pointers.  For each call stack, there are 2 functions that are recursively called.  One changes the end pointer to be closer to the start, while the other moves the start pointer to be closer to the end.  Once the 2 pointers meet, the base case is met and the array is returned.
[PIC1]

```python
# Implementation of MergeSort
def mergeSort(arr, s, e):
    # base case: the start and end pointers are the same
    if e - s + 1 <= 1:
        return arr

    # recalculates the mid pointer for each call stack
    m = (s + e) // 2

    # changes the end pointer to go towards the start pointer until they meet
    mergeSort(arr, s, m)

    # changes the start pointer to go towards the end pointer until they meet
    mergeSort(arr, m + 1, e)
    
    # ../
```

## Building the Array Back Up
After breaking down the elements, we'll start to build the array back up using the merge function.  The merge function will sort the array in place and return the newly sorted array. The causes the next callstack to have an array that is partially sorted depending on where the pointers are until we reach the top of the call stack.
[PIC2]

```python
# Implementation of MergeSort
def mergeSort(arr, s, e):
    # ..

    # after the items are broken down, we'll call merge as we build up our array
    merge(arr, s, m, e)
    
    # ..
```

## The Merge Function
The merge function involves taking an array that is sorted on the left and right sides and sorting it in place until the array passed in is sorted from the start to end pointer.  
[PIC3]

Since we are mutating the array passed in, we'll want to create copies for the left and right sides.  The left will go from the start to middle index, while the right will go from the element after the middle index to the end.
```python
# Merge in-place
def merge(arr, s, m, e):
    # Copy the sorted left & right halfs to temp arrays
    L = arr[s: m + 1]
    R = arr[m + 1: e + 1]

    # ...
```

Next we'll create the indexes for the array.  We'll have one for the left array, one for the right array and then one for the array passed in.  For the left and right array pointers we'll start at the first item and for the array pointer we'll start at the start index.

```python
def merge(arr, s, m, e):
    # ...

    i = 0 # index for L
    j = 0 # index for R
    k = s # index for arr

    # ...
```

Next we'll create a while loop to iterate across the left and right array copies.  As long as both the left and right pointers are within the range of the array we'll contiue the loop.  Each loop will compare the left and right array items at their respective pointers.  For the item that is less we'll increment it's pointer, replace the item at the current array index, and increment the array index.
```python
def merge(arr, s, m, e):
    # ...

    # Merge the two sorted halfs into the original array
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # ...
```

Since the while loop asserts that the indexes are within range of both the left and right arrays, we might be left with values of one array that has not been sorted.  We'll create 2 while loops, one for each side, so that if one does have remaining items this loop will take care of it.Each while loop will perform the same functionality as the first while loop - we replace the array element with the current index of the left or right copy and then increment the copy index as well as the array index.
```python
# Merge in-place
def merge(arr, s, m, e):
    # ...

    # One of the halfs will have elements remaining
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
```

## Time complexity
TODO: add time complexity 



