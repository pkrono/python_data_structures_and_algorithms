def linear_search(my_array, target):
    for i in range(len(my_array)):
        if my_array[i] == target:

            return i

    return None

print(linear_search([5,3,1,9,2], 2))
