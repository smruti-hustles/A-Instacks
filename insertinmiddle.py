'''
Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1.
'''
s1=input()
s2=input()
l1=len(s1)
if l1%2==0:#even lrngth
   res=s1[0:(l1//2)]+s2+s1[(l1//2):l1]
else:
    res=s1[0:(l1//2)+1]+s2+s1[(l1//2)+1:l1]
print(res)     
