#String Palindrome
a=input()
c=a[::-1]
print(f"reverse of {a} is {c}")
if(a==c):
    print("palindrome")
else:
    print("Not palindrome")
