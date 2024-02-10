'''
Write a Python program to read
a string as an input and count occurrences 
of all characters within a string
'''
a=input()
l=set(a)
for i in l:
    print(f'occurance of {i} is {a.count(i)}')
