# find the factorial of a given number n using recursion 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5)) 

# find the factorail of all the number upto given number
