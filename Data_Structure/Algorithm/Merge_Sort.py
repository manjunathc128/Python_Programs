"""
Merge_Sort :  Merge sort works on the principle of divide and conquere where elements are divided into subarrar
until we found 1 element in the array and recursively merge by comparing left and right array elements into parent array .

TimeComplexity
ALl cases: O(n logn)
"""

def divide(a,low,high):
    if low >= high:
        return
    mid = (low+high) // 2
    left=a[:mid+1]
    right=a[mid+1:]
    divide(left,0,len(left)-1)
    divide(right,0,len(right)-1)
    merge(a,left,right)

def merge(a,l,r):
    k,i,j=0,0,0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            a[k]=l[i]
            i+=1
            k+=1
        else:
            a[k]=r[j]
            j+=1
            k+=1
            
    while i < len(l):
        a[k] =l[i]
        i+=1
        k+=1
        
    while j < len(r):
        a[k]=r[j]
        j+=1
        k+=1
        
arr=[4,5,3,1,6,7,2]
n=len(arr)
divide(arr,0,n-1)        
print(arr)        
        
