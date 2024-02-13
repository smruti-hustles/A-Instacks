'''
Write a Python program to reverse a String if the length of the String is a multiple of 4. 
And if it is not display -1 as the result.
'''
a=input()
l=len(a)
if(l%4==0):
    print(a[::-1])
else:
    print(-1)
