def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)): 
  
        if arr[i] == target: 
            return i 

    return -1   


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    low = 0
    high = len(arr) - 1
    mid_index = 0
  
    while low <= high: 
  
        mid_index = (high + low) // 2
        mid_value = arr[mid_index]

        if mid_value == target:
            return mid_index
        elif target < mid_value:
            high = mid_index - 1
        else:
            low = mid_index +1

    return -1  # not found
