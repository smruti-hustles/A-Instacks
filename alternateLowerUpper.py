n=input()
res=""
for i in range(len(n)):
    if i%2==0:
      res=res+n[i].lower()
    else:
      res=res+n[i].upper()    
print(res)  
