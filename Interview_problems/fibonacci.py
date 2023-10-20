# program to print number upto given fibonacci 
def fibonacci(n):
    fib_list = [0, 1]
    while fib_list[-1] + fib_list[-2] <= n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

# Get user input for the maximum number
num = int(input("Enter a number: "))

# Call the fibonacci function and print the result
result = fibonacci(num)
print("Fibonacci series up to", num, "is:", result)
