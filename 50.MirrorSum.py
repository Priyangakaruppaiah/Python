s=0
a=[]
for i in range(0,n1):
    s=0
    while(n[i]>0):
        r=n[i]%10
        s=(s*10)+r
        n[i]=n[i]//10
    a.append(s)
a.sort()
print(a)
'''
OUTPUT:
[29, 32, 43, 54, 78]
'''
