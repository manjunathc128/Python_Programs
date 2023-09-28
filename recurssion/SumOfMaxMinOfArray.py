# find maximum and minimum from arr1 and arr 2 respectively and return their sum value 
def maximum(maxx: int,arr: [],n: int) -> int:
    if n == len(arr)-1:
        if arr[n] > maxx:
            return arr[n]
        return maxx
    var = maxx  
    if arr[n] > maxx:
        var = arr[n]
        return maximum(var,arr,n+1)
    else:
        return maximum(var,arr,n+1)
        
def minimum(minn: int,arr: [],n: int) -> int:
    if n == len(arr)-1:
        if arr[n] < minn:
            return arr[n]
        return minn
    var=minn
    if arr[n] < minn:
        var=arr[n]
        return minimum(var,arr,n+1)
    else:
        return minimum(var,arr,n+1)
    
arr=[2,5,1,4,3]       
print((maximum(arr[0],arr,1))+(minimum(arr[0],arr,1)))
