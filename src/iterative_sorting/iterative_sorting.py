# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j


        # TO-DO: swap
        # Your code here
        if smallest_index != i:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    n = len(arr) - 1
    sorted_list = False 
  
    while not sorted_list:
        sorted_list = True 
        for i in range(0, n): 
            if arr[i] > arr[i+1]:
                sorted_list = False
                arr[i], arr[i+1]  = arr[i+1], arr[i]
    return arr 



 


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
