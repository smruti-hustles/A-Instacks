'''
Write a Python program to read 2 string values from the user and check 
whether all the characters of String1 are present in String2.
'''
a=input()
b=input()
l1=set(a)
l2=set(b)
if l1.issubset(l2):
    print("all the characters of String1 are present in String2.")
else:
    print("all the characters of String1 are not present in String2.")  
