'''
Rabiul Rafi
CSE'16
Prime Factorization using Sieve of Eratosthenes approaches
e.g: 12--> 2,2,3 or 2^2*3
timeComplixity: O(√N/ln(√N)+log2(N):)
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
    prime_list =[]
    for i in range(2,n+1):
        if prime[i]==True:
            prime_list.append(i)

    factors = []
    for i in prime_list:
        if(n%i==0):
            while(n%i==0):
                n/=i
                factors.append(i)

    print(factors)

if __name__ == '__main__':
    n= int(input())
    SieveOfEratosthenes(n)

