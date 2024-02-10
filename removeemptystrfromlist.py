'''
Write a Python program to remove empty strings from the list of strings.
'''
n=eval(input())   
l=[]
for i in n:
    if i!='' and i!=None:
        l.append(i)
print(l) 
