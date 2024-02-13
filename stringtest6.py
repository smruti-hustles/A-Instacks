'''
Write a Python program to create a new string made up of the first 2 and last 2 characters of a given string.
'''
n=input()
l=len(n)
print(n[0:2]+n[(l-2):l])

'''
Write a Python program to create a new single string from two given strings, by swapping the first two characters of each string.

Order while printing – 1st string followed by the 2nd string value without any space in between.
'''
n=input()
m=input()
a1=m[0:2]+n[2:]
a2=n[0:2]+m[2:]
print(a1+a2)

'''
Write a program to remove an element from the specified index position and return the new string.
'''
print('enter string')
s=input()
print('enter index')
n=int(input())
res=s[0:n]+s[n+1:]
print(res)

'''
Write a Python program to create a new string from a String where the first and last chars have been exchanged.
'''
s=input()
l=len(s)
print(s[-1]+s[1:l-1]+s[0])

'''
Write a Python program to remove the elements in the Odd index position and return the new String.
'''
s=input()
e=""
for i in range(len(s)):
  if i%2!=0:
    e=e+s[i]
print(e)    


    










