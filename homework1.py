numbers_list = [7,8,9,2,3,1,4,10,5,6]
print('numbers_list =',numbers_list[:])

numbers_list.sort()
print('numbers_list =',numbers_list)

numbers_list.reverse()
print('numbers_list =',numbers_list)

numbers_list.sort()
even_numbers_list = numbers_list[1::2]
print('even_numbers_list =',even_numbers_list)

numbers_list.sort()
odd_numbers_list = numbers_list[::2]
print('odd_numbers_list =',odd_numbers_list)

numbers_list.reverse()
multiple_of_3_list = numbers_list[1::3]
print('multiple_of_3_list =', multiple_of_3_list)
