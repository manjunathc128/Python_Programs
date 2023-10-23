def factorial(n,memo={}):
    if n in memo:
        return memo[n]
    if n < 2 :
        return 1
    memo[n] = n * factorial(n-1)
    print(memo[n])
    return memo[n]
print(factorial(7))  
