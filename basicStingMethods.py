'''
This file conains all the predefined methods of string and their implementations

'''
s="hello"
t="world"
print(s+t)
print(f'contcatanation of {s} and {t} is = {s+t}')
p=input()
q=int(input())
r=str(q)
res1= " ".join([p,r])
res2= "".join([p,r])
print(res1)
print(res2)

'''
a="hello Ggt eiTHi ,H i7tl."
print(a.isupper())
print(a.islower())
print(a.istitle())
print(a.upper())
print(a.lower())
print(a.title()) #converts first letter of each word into uppercase
print(a.capitalize()) #converts the first letter  into uppercase
print(a.swapcase())#converts lower to uppercase and vvice versa
'''
'''
b="1,2,3,546,5,1,24,1"
print(b.replace("1","100")) #it replace all 1 with 100
print(b.replace("1","100",2))#it replace the first two 1 with 100
'''
'''
c='1245'
print(c.isalpha())
print(c.isdigit())
print(c.isspace())
print(c.isalnum())
'''
'''
c='smruti rekha pradhan'
print(c.isalpha())
print(c.isdigit())
print(c.isspace())
print(c.isalnum())
'''
'''
c='smruti rekha pradhan9080'
print(c.isalpha())
print(c.isdigit())
print(c.isspace())
print(c.isalnum())
'''
'''
c='smrutirekhapradhan90'
print(c.isalpha())
print(c.isdigit())
print(c.isspace())
print(c.isalnum())
'''
'''
c='smrutirekhapradhan'
d="   "
print(c.isalpha())
print(c.isdigit())
print(c.isspace())
print(c.isalnum())
print(d.isspace())
'''
'''
e="hey there how are you guys"
print(e.startswith("h"))
print(e.startswith("hey"))
print(e.startswith("hey t"))
print(e.startswith("hey  t"))
print(e.endswith("s"))
print(e.endswith(" guys"))
'''
'''
f="kkldhfbjvgb4576"
print(len(f))
print(max(f))
print(min(f))
'''
'''
g=" jgkhj  "
print(g.strip())
print(g.rstrip())
print(g.lstrip())
'''
'''
h="aaaadfhkutakuh kghguyt k65983"
print(h.count('a'))
print(h.count("aa"))
print(h.count('ghg'))
'''
'''
i="hello"
print(i.center(10,'*'))
print(i.center(20,"-"))
'''
'''
j="rt566"
print(j.casefold())
print(j.encode())
'''
'''
k=",mvbh yt786 v, jiog7y6yh;iy@uyt@vgf"
print(k.split(";"))
print(k.split("@"))
print(k.split(" "))
print(k.split(","))
'''
