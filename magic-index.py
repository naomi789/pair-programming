from math import floor

# "A magic index in an array A[0..n-1] is defined to be an index such that A[i] = i.
# Given a sorted array of distinct integers,
# write a method to find a magic index, if one exists, in array my_array

# 2018 July 8th
# 2018 July 22nd 

my_array = [2, 3, 4, 5, 6]
other_array = [1, 2, 10, 20, 30]
some_array = [-5, -4, -3, 0, 4, 6]
alt_array = [-5, -4, -3, 0, 1, 6]


def simple_solution(my_array):
    # this works even if the array is not sorted
    for value in range(0, len(my_array)):
        if my_array[value] == value:
            return value


def helper_binary_search(lower_bound, upper_bound, my_array):
    should_continue = True

    place = floor(lower_bound + (upper_bound - lower_bound) / 2)


    if my_array[place] == place:
        should_continue = False
        lower_bound = place
        upper_bound = place

    elif lower_bound + 1 == upper_bound:
        return False, -1, -1
    
    elif my_array[place] > place:
        # don't look above, look below
        upper_bound = place

    elif my_array[place] < place:
        # look above
        lower_bound = place





    return should_continue, lower_bound, upper_bound


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
            should_continue = True
            lower = 0
            upper = len(my_array) - 1
            while should_continue:
                should_continue, lower, upper = helper_binary_search(lower, upper, my_array)
            if lower == -1:
                return False
            if lower == upper:
                return lower



        else:
            pass
            # there is only one thing





# print(simple_solution(my_array))
print(binary_search(alt_array))

