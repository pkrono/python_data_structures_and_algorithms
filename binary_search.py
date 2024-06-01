def binary_search(my_array, target):
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
