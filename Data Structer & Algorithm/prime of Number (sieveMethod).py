'''
Sieve of Eratosthenes
timeComplixity: O(n*log(log(n)))

firstly we declare a list of size n where we put all the value as True, then we will check all value.
If it is divisable by other prime number we will place prime[i]=False.

'''
import math
def SieveOfEratosthenes(n):

    prime = [True for i in range(n+1)]
    p=2
    while(p*p<=n):
        if prime[p]==True:
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
    for i in range(2,n+1):
        if prime[i]==True:
            print(i, end=' ')

if __name__ == '__main__':
    n= int(input())
    SieveOfEratosthenes(n)

