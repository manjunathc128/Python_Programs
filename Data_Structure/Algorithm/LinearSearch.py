""" Linear Search Algorithm : Linear Search algorithm works based on the principle of sequential searching .
In this algorithm the control will traverse through given sequence by comparing every value of the sequence to check the given key is present or not """ 

def Linear_search(arr,key):
    for index in range(len(arr)):
        if arr[index] == key:
            return index
    else:
        return "key Doesnot Exist"
arr=[2,3,4,5,5,6,7,4,3,5,6]        
print(Linear_search(arr,5))  
