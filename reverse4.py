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

'''
Write a Python program to access each character of a string in both forward and backward directions by using the while loop
'''
a=input()
b=a[::-1]
for i in a:
    print(i,end=" ")
print("")    
for i in b:
    print(i,end=" ") 
