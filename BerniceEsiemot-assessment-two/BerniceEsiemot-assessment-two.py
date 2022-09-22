# 3
numbers = [8, 5, 3, 2, 9, 1, 6]
numbers.sort()

print(numbers)


def square_numbers(squares):
    return squares ** 2


square_iteration = map(square_numbers, numbers)
nums = list(square_iteration)

print(nums)


#  9. TWO NUMBER SUM
my_numbers = [3, 5, -4, 8, 1, -1, 6]


def sum_of_two_numbers(target_sum):
    return sum(target_sum) == 10


two_num_sum = []

for x in range(0, len(my_numbers)):
    for y in range(x + 1, len(my_numbers)):
        if my_numbers[x] + my_numbers[y] == 10:
            numbers = my_numbers[x], my_numbers[y]
            two_num_sum.append(list(numbers))

print("The two numbers that add up to the target sum 10 is:")
print(str(numbers))



