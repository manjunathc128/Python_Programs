"""
Bubble sort algorithm : Bubble Sort is a simple comparison-based sorting algorithm. 
It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. 
The pass through the list is repeated until the list is sorted. 

After first pass we can sort only one element to its sorted position .


Time complexity 
Bestcase : O(n)
worstcase : O(n^2)
averagecase: O(n^2)

"""
# Asscending order
def Bubble_sort(arr):
    n=len(arr)
    
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
arr=[23,12,5,3,24]                
Bubble_sort(arr)
print(arr)

#descending order
def Bubble_sort(arr):
    n=len(arr)
    
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] < arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
arr=[23,12,5,3,24]                
Bubble_sort(arr)
print(arr)
