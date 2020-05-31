import sys


'''
Rabiul Rafi
CSE'16
This function finds factorial of large numbers and prints them
'''

def factorial(n):
    res = [None] * 500
    res[0] = 1
    res_size = 1
    x = 2
    while x <= n:
        res_size = multiply(x, res, res_size)
        x = x + 1
    print(res)
    print("Factorial of given number is")
    i = res_size - 1
    while i >= 0:
        print(str(res[i]),end="")
        i = i - 1

def multiply(x, res, res_size):
    carry = 0  # Initialize carry
    i = 0
    while i < res_size:
        prod = res[i] * x + carry
        res[i] = prod % 10
        carry = prod // 10 # Put rest in carry
        i = i + 1

    while (carry):
        res[res_size] = carry % 10
        carry = carry // 10
        res_size = res_size + 1

    return res_size

factorial(100)