'''
Given an array of integer elements, n denoting  size of an array and integer k 
return 0 if no element has integer k in it. 
return element that has maximum occurance of integer k in it .
using recursions
'''


# k = int(input())
# s=str(input())

k = 0
arr = ['2992','2221321112222','0', '220002','22232']

# arr=s.split(" ")
# print(arr)

for i in range(len(arr)):
    arr[i] = int(arr[i])
    
print(arr)

arr1=[]
def K_counter(arrayElement,count):
    
    count=count
    if arrayElement == 0:
        return arr1.append(count)
    if arrayElement % 10 == k:
        count=count+1
        return K_counter(arrayElement//10,count)
    else:
        return K_counter(arrayElement//10,count)
        
for y in arr: 
    if y != 0:
        K_counter(y,0)   
    else:
        arr1.append(0)
    
max=0  
var=None
print(arr1)
for x in arr1 :
    if x > max:
        max =x  
        var=arr1.index(x)
        
print(arr[var])
