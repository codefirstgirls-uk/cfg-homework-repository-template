
#Task 3
numbers = [1,2,3,5,6,8,9]

def square_function(numbers):
    return [num * num for num in numbers]



print(square_function(numbers))

'''
Input:
my_numbers = [3, 5, -4 ,8, 11, 1, -1, 6] | target_sum = 10
Output:
[-1, 11] | Numbers can be returned in any order → it does not matter
'''

my_numbers = [3,5,-4,8,1,6]
target_sum = 10
gap_list=[]

def summing_number_to_target(my_numbers, target_sum):
    for number in my_numbers:
        gap = target_sum-number
        if number != gap:
            gap_list.append(gap)
    return gap_list

def comparing_two_lists(my_numbers,gap_list):
    result = [value for value in my_numbers if value in gap_list]
    return result

def main_function():
    print(summing_number_to_target(my_numbers,target_sum))
    print(comparing_two_lists(my_numbers,gap_list))

main_function()



if __name__== '__main__':
    square_function(numbers)
