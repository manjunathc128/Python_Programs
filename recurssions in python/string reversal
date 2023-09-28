# string reverse programs

def reversestring(s: str ) -> str: #using slicing approach
    return s[::-1]
print(reversestring('hello'))


def reversestring(s: str,n: int) -> str:   # substitute approach
    i,j=0,n                                # TypeError : str object doesnt support item assignment
    st=s
    while(i<j):
        temp = st[i]
        st[j] = st[i]
        st[i] = temp 
        i += 1    
        j -= -1
    return s  
    
string="hello"

print(reversestring(string,(len(string)-1)))        

def stringreversal(arr,n):                      #recursive approach
    if n == 0:
        return arr[n]
    
    return arr[n] + stringreversal(arr,n-1)
string="hello"   

print(stringreversal(string,(len(string)-1)))




