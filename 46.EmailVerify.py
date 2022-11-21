# Email verification in python
import re
n=input()
pat = '^[a-z]+[\.]?[a-z0-9]+@[a-z]+[.]\w{2,3}$'
p1='^[a-z]+[\.]?[a-z0-9]+@[a-z]+[.][a-z]+[.]\w{2}$'
if re.match(pat,n) or re.match(p1,n):
    print("Valid Email")
else:
    print("Invalid Email")

'''
OUTPUT:
ghfythvg@@kjehf.com
Invalid Email

'''
    
    
