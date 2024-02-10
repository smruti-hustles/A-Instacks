'''
Write a Python program to take 2 string as input and create a new string by mixing the 1st char of string one with the last character of string two and next the 2nd character of string one with the last before character of string two and so on. 
If any characters are left out, put them at the end of the newly created string.

'''
a=input()
b=input()
a1=b[::-1]
l1=len(a)
l2=len(a1)
s=""
if l1<l2:
    for i in range(l1):
       s+=a[i]+a1[i]
    s+=a1[l1:l2]  
else:
    for i in range(l2):
       s+=a[i]+a1[i]
    s+=a[l2:l1]
print(s)    

    
