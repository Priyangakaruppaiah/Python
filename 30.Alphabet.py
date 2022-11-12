# only print alphabets and remove all the special characters and digits
n=str(input())
n1=len(n)
p=' '
for i in n:
    if i in ('a','v','c','g','b','n','m','z','s','d','f','j','k','l','q','w','e','r','t','y','u','i','o','p','Q','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','M','L','N','B','V','C','X','Z'):
        p=p+i
print(p)

'''
OUTPUT:
adsg5&@vshat
 adsgvsat
'''
