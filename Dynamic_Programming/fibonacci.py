# Fibonacci of given index number  in the series using Dynammic Programming and recursion 

# Time complexity : O(2n)   without DP 2**n
# space complexity : O(n)   without DP n

def fibonacci(n,memo={}):
    if n in memo:
        return memo[n]
    if n <= 2 :
        return 1
    memo[n] = fibonacci(n-1,memo) + fibonacci(n-2,memo)
    return memo[n]

print(fibonacci(50))    
