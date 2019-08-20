# https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt


#Question 2
#Level 1
#
#Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320


age = input("input Num:")

int_age = int(age) + 1
result = 1

for i in range(1, int_age):
    result = result * i
    print(i, ":",result)

