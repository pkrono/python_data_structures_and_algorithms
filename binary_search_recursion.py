def binary_search_recursion(my_array, target):
    """
    Perform a binary search to find the index of the target value in a sorted array.

    Parameters:
    my_array (list): A list of sorted elements.
    target (any): The element to search for in the array.

    Returns:
    int: The index of the target if found, otherwise -1.
    """

    left = 0
    right = len(my_array) - 1
    result = recursion_helper(my_array, target, left, right)
    return result

def recursion_helper(my_array, target, left, right):
    """
    Helper function to perform the recursive binary search.

    Parameters:
    my_array (list): A list of sorted elements.
    target (any): The element to search for in the array.
    left (int): The left boundary of the current search range.
    right (int): The right boundary of the current search range.

    Returns:
    int: The index of the target if found, otherwise -1.
    """

    if left > right:
        return -1

    middle = (left + right) // 2
    middle_element = my_array [middle]

    if target == middle_element:
        return middle

    elif target < middle_element:
        right = middle - 1
        return recursion_helper(my_array, target, left, right)
    else:
        left =  middle + 1
        return recursion_helper(my_array, target, left, right)

print(binary_search_recursion([1,2,4,6,8,9,11,30,60,90], 11))
