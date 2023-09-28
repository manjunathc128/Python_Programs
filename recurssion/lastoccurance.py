# recursive approach to find index of last occurance of given value in an array 

#a= [ ]
def lastocccurance(arr: [], M: int, n: int,a) -> int:                # input : [2,3,4,2,1]
    if arr[n] != M :                                                 # output : 3 
        if n == len(arr)-1:
            return n
            
        return lastocccurance(arr,M,n+1,a)
            
    if arr[n] == M:
        a.append(n) 
        if n == len(arr)-1:
            return n
        return lastocccurance(arr,M,n+1,a)
        
arr=[2,2,1,1,0,0,0,0,0,2]
a=[]
print(lastocccurance(arr,2,0,a))   
print(a)
print(a[-1])
