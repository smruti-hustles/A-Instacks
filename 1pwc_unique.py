'''
You are given a task to analyze the uniqueness of characters in a given string. Write a Python program that takes
a string as input and determines the number of unique characters in the string. The program should exclude spaces an
count only non-space characters.
Additionally, the program should provide a list of these unique characters and display the total count.
i/p
happy life
o/p
NO of unique charecters are ['h', 'a', 'y', 'l', 'i', 'f', 'e'] and total they are 7
'''
n=input()
d={}
for char in n:
    if char==' ':
        continue
    if char not in d:
        d[char]=1
    else:
        d[char]+=1
count=0
l=[]
for m,n in d.items():
    if n==1:
        l.append(m)
        count+=1
print(f"NO of unique charecters are {l} and total they are {count}")    
