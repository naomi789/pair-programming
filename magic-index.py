from math import floor

# "A magic index in an array A[0..n-1] is defined to be an index such that A[i] = i.
# Given a sorted array of distinct integers,
# write a method to find a magic index, if one exists, in array my_array

# 2018 July 8th

my_array = [2, 3, 4, 5, 5, 5, 6]
other_array = [1, 2, 10, 20, 30]
some_array = [-5, -4, -3, -3, 4]


def simple_solution(my_array):
    # this works even if the array is not sorted
    for value in range(0, len(my_array)):
        if my_array[value] == value:
            return value


def binary_search(my_array):
    # this works because the array is sorted
    assert(my_array == sorted(my_array))
    assert(len(my_array) > 0)

    # and there are no duplicates
    assert(len(my_array) == len(set(my_array)))

    if my_array[0] > 0:
        return False
    elif my_array[len(my_array) - 1] < len(my_array) - 1:
        return False
    else:
        if len(my_array) >= 2:
            var = True
            while(var):
                place = floor(len(my_array) / 2)
                if my_array[place] > place:
                    var = False
                    # don't look above, look below


        else:
            pass
            # there is only one thing





# print(simple_solution(my_array))
print(binary_search(my_array))

