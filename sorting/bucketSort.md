## Overview
Bucket sort is a linear algorithm that involves placing items in an array in their corresponding bucket and then iterating through the buckets and to reorder the array.  In order for this algorithm to work the values within the array need to be a known finite range.

## Example
Let's say we have an array and we know the values can only be 0, 1, or 2 and we want to sort the array.  We'll first organize the elements into buckets, each bucket will have the corresponding count of that element.
[PIC1]

In the example above, the items happen to equal the indexes of the array. For each 0 item we'll add 1 to the 0th index, for the 1 item we'll add to the 1 index, and for the 2 items we'll add to the 2 index.
```python
def bucketSort(arr):
    # Assuming arr only contains 0, 1 or 2
    counts = [0, 0, 0]

    # Count the quantity of each val in arr
    for n in arr:
        counts[n] += 1

    # ...
```

Next we'll want to create our new array.  To do this we'll iterate through our counts and for each item we'll use the value to tell us how many times to add it's value to the new array.  We'll create an index variable that will tell us where to place the value.  Once the value is placed in the array, we'll increment the index.  Note that we will be writing over the original array and then returning it.
```python
    # Fill each bucket in the original array
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    return arr
```