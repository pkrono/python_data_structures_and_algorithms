def binary_search(my_array, target):
    """
    Perform a binary search to find the index of a target element in a sorted array.

    Parameters:
    my_array (list): A list of sorted elements (ascending order) where the target element is to be searched.
    target (int or float): The element to search for within the array.

    Returns:
    int: The index of the target element if found in the array; otherwise, -1.

    The function works by repeatedly dividing the search interval in half. If the value of the target is less than
    the value in the middle of the interval, the interval is reduced to the lower half. Otherwise, it is reduced
    to the upper half. This process continues until the target value is found or the interval is empty.
    """
    left = 0
    right = len(my_array) - 1

    while left <= right:
        middle = (left + right)//2

        middle_element = my_array[middle]

        if target == middle_element:
            return middle
        elif target < middle_element:
            right = middle - 1

        else:
            left = middle + 1

    return -1

print(binary_search([1,2,4,6,8,9,11,30,60,90], 11))
