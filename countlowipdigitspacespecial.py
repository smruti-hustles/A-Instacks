'''
Write a Python program to count all the Lowercase, Uppercase, Digits and Special symbols from a given string.

'''
str=input()
u=0
l=0
d=0
s=0
spe=0
for i in str:
    if(i.isupper()):
        u=u+1
    elif(i.islower()):
        l=l+1    
    elif(i.isdigit()):
        d=d+1 
    elif(i.isspace()):
        s=s+1  
    else:
        spe=spe+1
print(f'total uppercases {u}')     
print(f'total lowercases {l}')  
print(f'total digit {d}')   
print(f'total spaces {s}')  
print(f'total special symbols {spe}')   
