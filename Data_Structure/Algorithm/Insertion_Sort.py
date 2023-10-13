'''
Insertion sort : Insertion sort in-place sorting algorithm, it compares key element and replace it to its sorted position by swapping its 
previous.

TimeComplexity

BestCase : O(n)
WorstCase: O(n^2)
AverageCase:O(n^2)

'''


def Insertion_Sort(arr,n):
    for passno in range(1,len(arr)):
        i=passno
        while i!=0 and arr[i] < arr[i-1]:
            arr[i],arr[i-1] = arr[i-1],arr[i]
            i-=1
            
arr=[12,45,98,12,78,1,3,4]            
Insertion_Sort(arr,len(arr))            
print(arr)  


def insertion_sort(arr):
   for passno in range(1,len(arr)):
       key=arr[passno]
       i=passno-1
       while i>=0 and key < arr[i]:
           arr[i+1] = arr[i]
           i-=1
       arr[i+1] = key   
           
           
# Example usage
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array is:", arr)
