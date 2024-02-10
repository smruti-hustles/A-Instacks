'''
Write a Python program to remove from the given string and replace each punctuation with a # symbol.
'''
n=input()
for i in n:
    if not i.isalpha() and not i.isdigit() and not i.isspace():
       n = n.replace(i,"#")
print(n)   
