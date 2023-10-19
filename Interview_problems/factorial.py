# find the factorial of a given number n using recursion 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5)) 

# find the factorail of all the number upto given number using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
    
num = int(input("enter the number: " ))   

for val in range(2,num+1):
    print(factorial(val))
