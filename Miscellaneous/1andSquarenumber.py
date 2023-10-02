'''

Given a array of integer elements
1) return element if it is addition of 1 and square of any natural number

'''
# -------------1-----------
def square(po):
    return po*po
    
def secondsquare(k2:int):
    
    
    if 1 + square(k2) == n:
        return [1, k2]
        
    else:
        return secondsquare(k2+1)
        
def firstsquare(k1: int):
    print(secondsquare(k1))
n=26 
firstsquare(0)

#-------------2-------------

def square(po):
    return po*po
    
def checkSquare(k2:int,x):
    
    if square(k2) < x:
    
        if 1 + square(k2) == x:
            return 1
            
        else:
            return checkSquare(k2+1,x)
    else:
        return 0
        
def printSquare(x: int):
    if checkSquare(0,x) == 1:
        print(x)
        

arr=[5,10,17,26,25,126,145] 
for x in arr:
   printSquare(x) 
