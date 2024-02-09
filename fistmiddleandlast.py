'''
Given 2 strings, s1, and s2 return a new string made of the first, middle and last char each input strings.

'''

s = input()
t = input()
l1 = len(s)
l2 = len(t)
res = s[0] + t[0] + s[l1//2] + t[l2//2] + s[l1-1] + t[l2-1]
print(res)

    
    
    
