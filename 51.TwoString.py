n1=input()
n11=len(n1)
n2=input()
n22=len(n2)
n=min(n11,n22)
k=0
y=0
c=''
for i in range(0,n):
    if(k==0):
        c=c+(n1[i])
        c=c+(n2[i])
        k=1
        y=0
    elif(y==0):
        c=c+(n2[i])
        c=c+(n1[i])
        y=1
        k=0
if(n1>n2):
    for i in range(n,n11):
        c=c+(n1[i])
else:
    for i in range(n,n22):
        c=c+(n2[i])
print(c)

'''
OUTPUT:
hello
program
hprelogloram
'''
