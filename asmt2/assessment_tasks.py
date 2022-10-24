'''task 3'''
'''Write a function that takes in a non-empty array of integers that 
are sorted in ascending order and returns a new array of the same 
length with the squares of the original integers also sorted in 
ascending order'''

# numbers = [1, 2, 3, 5, 6, 8, 9]
# result = [ i**2 for i in numbers]
# print(result)

'''task 8'''
# A Write a SQL query to find the maximum order (purchase) amount for
# each customer.


# SELECT customer_id,MAX(purch_amt)
# FROM orders
# GROUP BY customer_id;

# B. The customer ID should be in the range 3002 and 3007 (begin and
# end values are included.)

# SELECT customer_id,MAX(purch_amt)
# FROM orders
# WHERE customer_id Between 3002 and 3007
# GROUP BY customer_id;

# C. Filter the rows for maximum order (purchase) amount is higher than
# 1000.

# SELECT customer_id,MAX(purch_amt)
# FROM orders
# HAVING MAX(purch_amt)>1000;
# GROUP BY customer_id;

# D. Return customer id and maximum purchase amount.

# SELECT customer_id,MAX(purch_amt)
# FROM orders
# HAVING MAX(purch_amt);


'''task 9'''

'''Write a function that takes in a non-empty array of distinct integers
and an integer representing a target sum. If any two numbers in the
input array sum up to the target sum, the function should return
them in an array, in any order. If no to numbers sum up to the target
sum, the function should return an empty array.
● Note   that   the   target   sum   has   to   be   obtained   by   summing   two
different integers in the array. You cannot add a single integer to
itself in order to obtain the target sum.
● You can assume that there will be at most one pair of numbers
summing up to the target sum.'''

# my_numbers = [3, 5, -4 ,8, 11, 1, -1, 10, 6]
# target_sum = 10
# from itertools import combinations
#
# def function(target_sum, i):
#     result = []
#     numbers = [3, 5, -4 ,8, 11, 1, -1, 10, 6]
#     result = [combo for combo in combinations(numbers, i) if sum(combo) == target_sum]
#     return result
#
# print(function(10, 2))

