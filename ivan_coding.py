# from collections import defaultdict
import copy 

 # 0 1 2 
 # 3 4 5 
 # 6 7 8


 # 6 3 0
 # 7 4 1
 # 8 5 2

arr = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

arr_width = len(arr) - 1
# assert(len(arr[0]) - 1, arr_width)

second_arr = copy.deepcopy(arr)

print(arr)

for row_index in range(len(arr)): # row in arr:
	for column_index in range(len(arr)): # column in row:
		# print(arr[column_index][row_index])
		print(row_index, column_index, arr[row_index][column_index])
		second_arr[column_index][arr_width - row_index] = arr[row_index][column_index]
		
# print(arr[2][2])
print(second_arr)