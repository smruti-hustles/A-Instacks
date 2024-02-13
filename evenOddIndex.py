'''
Write a Python program to print characters present at even index and odd index positions.
'''
a=input()
e=""
o=""
for i in range(len(a)):
    if i%2!=0:
        e=e+a[i]
    else:
        o=o+a[i]
print(e)
print(o)
