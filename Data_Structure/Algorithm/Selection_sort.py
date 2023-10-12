"""
selection sort: The selection sort is comparision based sorting algorithm where elements are sorted by assuming 
minimum element and swappinhg with current minimum after the each pass.

IN selection sort the swapping takes places only after completing entire pass .

Time complexity

Bestcase: O(n^2)
worstcase: O(n^2)
averagecase: O(n^2)

"""
#asscending order

def selection_sort(arr, n):
    for i in range(1,n):
        minelement=i-1
        for j in range(i,n):
            if arr[minelement] > arr[j]:
                minelement = j
        arr[i-1],arr[minelement] = arr[minelement],arr[i-1]
arr=[23,14,12,1,13,16,3,7]
selection_sort(arr,len(arr))        
print(arr)

# descending order

def selection_sort(arr, n):
    for i in range(1,n):
        minelement=i-1
        for j in range(i,n):
            if arr[minelement] < arr[j]:
                minelement = j
        arr[i-1],arr[minelement] = arr[minelement],arr[i-1]
arr=[23,14,12,1,13,16,3,7]
selection_sort(arr,len(arr))        
print(arr)
