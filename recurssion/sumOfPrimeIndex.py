# sum of elemnts in array at prime indicies 

def sumOfPrimeIndices(arr:[], p: int) -> int:
    if p <= len(arr):
        v =findPrime(p)
        return arr[p] + sumOfPrimeIndices(arr,v)
    return 0
    
def findPrime(n:int) -> int:
    if n == 0 or n == 1:
        return n+1
    if n == 2 :
        return n+1
    if n == 3:
        return 5
    if n ==5:
        return 7
    if n ==  7:
        return 11
    if n == 11:
        return 13
    # if n % 2 == 0:
    #     return findPrime(n+1)      
    # else:
    #     return n
array=[10,-12,2,5,3,15,17,21,-3,-4] 

print(sumOfPrimeIndices(array,0))  
