# "A magic index in an array A[0..n-1] is defined to be an index such that A[i] = i.
# Given a sorted array of distinct integers,
# write a method to find a magic index, if one exists, in array A.

my_array = [10, 9, 8, 3]


def main(my_array):
    for value in range(0, len(my_array)):
        if my_array[value] == value:
            return value


print(main(my_array))

