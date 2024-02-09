'''
Given a string of odd length greater than or equal to 7, return a string made of the middle three chars of a given String. And if the string length is less than 7, return the original string value itself as the output.
'''
s=input()
l=len(s)
d=l//2
if l%2!=0:
  if l<7:
    print(s)
  else:   
    print(s[d-1:d+2])
else:
  print("take string of odd length")
    
    
    
