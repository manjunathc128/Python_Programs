# The below binary search algorithm search the key position either in left subarry or right subarray. Not in given array

def Binary_search(arr,key):
    low=0
    high=len(arr)
    
    mid=[(low + high) // 2 ] + 1
    
    
    if key == arr[mid]:
        return mid
    elif key < arr[mid]:
        return Binary_search([low:mid],key)
    elif Key > arr[mid]:
        return Binary_search([mid:high],key)
arr=[1,2,3,4,5,6,7]
print(Binary_search(arr,4))
 
# The below binary Search algorithm will search for element abd return index of element in given original array

def binary_Search(arr,key,low=0,high=None):
    if high == None:
        high = len(arr)-1
    
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == key:
        return mid
        
    elif key < arr[mid]:
        return binary_Search(arr,key,low,mid-1)
        
    elif key > arr[mid]:
        return binary_Search(arr,key,mid+1,high)
    
print(binary_Search([1,2,3,4,5,6,7,],7))   


