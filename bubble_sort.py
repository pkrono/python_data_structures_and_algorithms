def bubble_sort(my_array):

    """
    Sorts a list of numbers in ascending order using the bubble sort algorithm.

    Bubble sort is a simple sorting algorithm that repeatedly steps through the list,
    compares adjacent elements, and swaps them if they are in the wrong order. The
    pass through the list is repeated until the list is sorted. The algorithm gets
    its name because smaller elements "bubble" to the top of the list.

    Parameters:
    my_array (list): A list of numbers to be sorted. The list is sorted in place.

    Returns:
    None

    Notes:
    - The function modifies the input list in place and does not return a new list.
    - The time complexity of bubble sort is O(n^2) in the average and worst-case scenarios,
      where n is the number of items being sorted. This makes it inefficient for large lists.
    - Bubble sort is stable; it does not change the relative order of elements with equal keys.
    """
    n = len(my_array)
    for iter in range(n):
        swapped = False #If the flag remains False after a complete pass through the list, the function breaks out of the loop early
        for index in range(0, n - 1 - iter):
            if my_array[index] > my_array[index+1]:
                my_array[index], my_array[index+1] = my_array[index+1], my_array[index]
                swapped = True
        if not swapped:
            break

my_array = [29,10,12,14,37,20,14]
bubble_sort(my_array)
print(my_array)
