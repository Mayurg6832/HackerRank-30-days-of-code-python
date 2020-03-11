def factorial(n):
    if n!=1:
        p=n*factorial(n-1)
        return p
    elif n==1:
        return 1
n=int(input())
print(factorial(n))
