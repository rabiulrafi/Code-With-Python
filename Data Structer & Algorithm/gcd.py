#Naive Method (Recursion)

# def hcfnaive(a,b):
#     if b==0:
#         return a
#     else:
#         return hcfnaive(b,a%b)
# nk= input().split()
# n = int(nk[0])
# k = int(nk[1])
# print(f"Gcd of {n} and {k} is:  {hcfnaive(n,k)}")


# Euclidian Method
def computeGCD(x, y):
    while (y):
        x, y = y, x % y
        print(f"{x}-{y}")
    return x

print("The gcd of 60 and 48 is : ", end="")
print(computeGCD(35, 15))

