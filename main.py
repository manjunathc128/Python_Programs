
# recursive approach to return count of all the n natural numbers that have digit 2 in it    
def remainder(input1,n):
        if n == 0 :                                    # base condition or termination condition 
            return 0
        elif n % 10 != input1:
            return 0 + remainder(input1, n // 10)
        if n % 10 == input1:
            return 1 + remainder(input1, n // 10)
# count=0           
# #for x in range():
# count += remainder(2,2222)
# print(count)        
print(remainder(2,2222))    
        