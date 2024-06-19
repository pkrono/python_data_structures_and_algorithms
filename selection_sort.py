def selection_sort(arr):
    """
    Sorts an array of numbers in ascending order using the selection sort algorithm.
    
    Selects the smallest element from an unsorted list in each iteration and
    places the element at the beginning of the unsorted list

    Parameters:
    arr (list): A list of numerical elements to be sorted.

    Returns:
    None: The function sorts the list in place and does not return any value.

    Example:
    >>> arr = [20, 12, 10, 15, 2]
    >>> selection_sort(arr)
    >>> print(arr)
    [2, 10, 12, 15, 20]
    """
    
    for index in range(len(arr)):
        min_index = index
        
        for item in range(index + 1, len(arr)):
            if arr[item] < arr[min_index]:
                min_index = item
        #Swap
        arr[index], arr[min_index] =  arr[min_index], arr[index]

arr = [20,12,10,15,2]
selection_sort(arr)
print(arr)