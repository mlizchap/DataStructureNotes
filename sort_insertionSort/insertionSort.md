## Overview
Insertion sort is a O(n^2) in-place sorting algorithm that involves creating an outer for loop that compares 2 elements at a time and an inner while loop that swaps elements until the array up to the current index is sorted.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/4eb05da9-5ef2-4fcf-9c55-c5d129c923e4)

## Steps
We'll first start by creating a for loop through the array starting with the second item.  For each iteration we'll start off with creating a second index at the item before `i`. We'll call this index `j`.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/fda303f9-26a4-4c18-83e5-11d46504c7b5)

```python
def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        # ...
```
Next we'll want to compare our previous pointer to our current pointer.  If the previous element is greater than the current element, we'll want to enter an inner while loop.  As long as the previous item is greater than the current we'll keep swapping until we reach the beginning of the array and proceed to the next item in the outer loop.

```python
# while we haven't reached the first element and the previous item is less than current
while j >= 0 and arr[j + 1] < arr[j]:
    # arr[j] and arr[j + 1] are out of order so swap them 
    tmp = arr[j + 1]
    arr[j + 1] = arr[j]
    arr[j] = tmp
    j -= 1
```

Finally we'll return the array after we break out of the outer for loop.
```python
def insertionSort(arr):
    for i in range(1, len(arr)):
      # ...
    return arr
```
## An example
Let's look at the unsorted array `[2, 3, 4, 1, 6]`.  We'll start by creating a for loop starting with the second item and compare it to the previous item each loop.  For the first 2 iterations the previous item is less than the current so we'll just continue our outer loop without any swapping.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/b88eb616-f7ec-40d9-965e-0ef0e0df35f3)


On the third loop we come across an instance where the previous item (4) is larger than the current item (1).  Since 1 is less than all of the items before it, we'll want to continue swapping until we reach the beginning of the array.

![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/46600e75-d825-48d1-b19b-dd7bb3e1b785)


Finally, we get to the last item, which is already sorted.  We'll then break out of the outer for loop and return the now sorted array.
![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/6974598e-c2c4-460b-a5d4-dc7f36c0cc6a)

