'''
Write a Python program to merge characters of two different string in to a single string by taking characters alternatively.

If the strings are of unequal lengths, then all the remaining characters are to be put at the end of the new string.
'''
a=input()
b=input()
l1=len(a)
l2=len(b)
res=""
if(l1<=l2):
    for i in range(l1):
        res=res+a[i]+b[i]
    res=res+b[l1:]  
    print(res)
else:
    for i in range(l2):
        res=res+a[i]+b[i]
    res=res+a[l2:] 
    print(res)
