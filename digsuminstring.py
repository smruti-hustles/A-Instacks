'''
find sum of digits of the numbers in the string
'''
s=input()
c=0
for i in s:
    if(i.isdigit()):
        c=c+int(i)
print(c)        
