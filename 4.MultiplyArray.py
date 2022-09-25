//Python program to multiply array elements
n=int(input("enter the list"))
a=[]
c=0
while(c<n):
    b=int(input("enter the number"))
    a.append(b)
    c=c+1
e=a[0]
p=1
f=a[p]
while(p<n):
    g=0
    h=1
    f=a[p]
    while(h<=f):
        g=g+e
        h=h+1
    e=g
    p=p+1
print(g)
