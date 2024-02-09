'''
Write a python program to arrange the string characters such that all the lowercase letters should come first followed by all the uppercase letters in each string. If the string contains anything other than alphabets ignore those characters.
'''
str=input()
u=""
l=""
for i in str:
    if(i.islower()):
        l=l+i
    elif(i.isupper()):
        u=u+i 
res=l+u        
print(f'first upper then lower are={res}')     
