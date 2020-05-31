'''
Rabiul Rafi
CSE'16
NOD--> stands for Number of divisors
We search all the item's upto sqrt(n)
Time complexity O(sqrt(N))

'''

import math
import datetime
def NOD(n):
    divisors= []
    res= 0
    for i in range(1,math.floor(math.sqrt(n))+1):
        if(n%i==0):
            if(n//i ==i):
                res+=1
                divisors.append(i)
            else:
                divisors.append(n // i)
                divisors.append(i)
                res+=2
    return res,divisors

n = int(input())
res, divisors = NOD(n)
print(f"Number of divisors : {res}")
print(f"Sum of all divisors : {sum(divisors)}")