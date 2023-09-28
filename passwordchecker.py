# 

def passwordchecker(s: str, n: int) :
    
    if n < 4 :
        return 0
    if '0' <= s[0] <= '9' :
        return 0
    cap,num = 0,0  
    for char in s :
        if char in ['/', ' ']:
            return 0
        if 'A' <= char <= 'Z':
            cap += 1
        if '0' <= char <= '9':
            num += 1
    
    if num >= 1 and cap >= 1:
        return 1
    else:
        return 0
    
password="A1AA"    
print(passwordchecker(password,len(password)))
