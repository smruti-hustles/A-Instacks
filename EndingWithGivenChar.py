#Program to print the words ending with letter given letter. 
s=input()
t=input()
s1=s[::-1]
if(len(t)==1):
    if(t==s1[0]):
        print("yes")
    else:
        print("no")
else:
    print("give the second letter a character that is length only 1")
