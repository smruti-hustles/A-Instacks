'''
Write a program to accept an alphanumeric string and sort the characters of the string 
– first alphabets, followed by digits, followed by any other characters.
'''
a=input()
al=""
dig=""
cha=""
for i in a:
    if i.isalpha():
        al=al+i
    elif i.isdigit():
        dig=dig+i
    else:
        cha+=i
print(al+dig+cha)  
