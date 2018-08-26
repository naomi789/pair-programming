from math import floor
import random

# "A magic index in an array A[0..n-1] is defined to be an index such that A[i] = i.
# Given a sorted array of distinct integers,
# write a method to find a magic index, if one exists, in array my_array
# tall numbers will be increasing, and no duplicates

# 2018 July 8th
# 2018 July 22nd
# 2018 August 26th

my_array = [2, 3, 4, 5, 6]
other_array = [1, 2, 10, 20, 30]
some_array = [-5, -4, -3, 0, 4, 6]
alt_array = [-5, -4, -3, 0, 1, 6]
another_array = [0, 2, 5]
more_array = [-1, 0, 2]
all_arrays = [my_array, other_array, some_array, alt_array, another_array, more_array]


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
    elif my_array[0] == 0:
        return 0
    elif my_array[-1] == len(my_array) - 1:
        return my_array[-1]
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

def make_test_array(num_times):
    random.seed(num_times * 9999)
    size_array = random.randint(3, 100)
    random_numbers = set()
    min = -50
    max = 50
    for index in range(0, size_array):
        num = random.randint(min, max)
        random_numbers.add(num)
    array = sorted(random_numbers)
    print(array)
    return array


# idk:
# print(simple_solution(my_array))

# original:
# for array in all_arrays:
#     print(binary_search(array))


# real code starts here:
print("automated test cases")
count_passed_test_cases = 0
num_cases = 100
for num_times in range(0, num_cases):
    array = make_test_array(num_times)
    result = binary_search(array)
    if result != False:
        # print(result)
        if array[result] != result:
            assert False
        else:
            count_passed_test_cases += 1
    else:
        for index in range(0, len(array)):
            if index == array[index]:
                assert False
        count_passed_test_cases += 1

print(f"Passed {count_passed_test_cases} out of {num_cases} test cases")

