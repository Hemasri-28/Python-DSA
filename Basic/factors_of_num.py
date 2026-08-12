def factors(n):
    result=[]
    for i in range(1,n+1):
        if n%i==0:
            result.append(i)
    return result
n=int(input("Enter a number:"))
print(factors(n))

# Optimal solution
def factors(n):
    result=[]
    for i in range(1,n//2+1):
        if n%i==0:
            result.append(i)
    result.append(n)
    return result
n=int(input("Enter a number:"))
print(factors(n))

# Better and more optimal way
from math import sqrt


def factors(n):
    result=[]
    for i in range(1,int(sqrt(n)+1)):
        if n%i==0:
            result.append(i)
        if n // i != i:
            result.append(n // i)
    return result
n=int(input("Enter a number:"))
print(factors(n))