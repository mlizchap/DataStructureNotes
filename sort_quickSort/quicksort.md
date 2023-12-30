## Overview
Quicksort is similar to merge sort but instead of dividing the array down the middle, we'll pick a pivot index as our partition

## Steps 
To start, we'll choose a pivot and assign a left pointer to the end pf the array.
[PIC1]

```python
def quickSort(arr, s, e):
    pivot = arr[e]
    left = s # pointer for left side
```

Next we'll iterate through the array comparing the current index to the pivot.  If the current item is less than the pivot, we'll swap the item with the left pointer.  Otherwise we'll just move on with our main index.
```python
def quickSort(arr, s, e):
    # ...

    # Partition: elements smaller than pivot on left side
    for i in range(s, e):
        if arr[i] < pivot:
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left += 1

    # ...
```

After we exit out of our for loop, our pivot index will still be at the end of the array.  Since the left pointer is used to swap the lesser values, we can swap this out with the pivot. This way all of the items to the left will be less than the pivot and to the right will be greater.
```python
arr[e] = arr[left]
arr[left] = pivot
```

So far we have only gone through one iteration. All of the items to the left of the pivot will be less than it and to the right will be greater, but the items to the left and right are not necessarily in order.  To get the items in the correct order we'll recursively call the quicksort function until there is only one item, or the start index meets up with the end index.
```python
def quickSort(arr, s, e):
    # base case, end and start indexes meet up
    if e - s + 1 <= 1:
        return

    # ...

    # recursively call quicksort on the left and right sides
    quickSort(arr, s, left - 1) # left side
    quickSort(arr, left + 1, e) # right side

    return arr
```


