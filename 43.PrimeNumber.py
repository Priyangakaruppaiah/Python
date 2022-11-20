# prime number
n=[3,4,5,7,34,56,23,11,13,10,6,8,80]
m=len(n)
print(m)
a=[]
for i in range(0,m):
    #c=2
    s=1
    for c in range(2,n[i]):
        if(n[i]%c==0):
            a.append(n[i]) 
            break
print(a)
'''
OUTPUT:
13
[4, 34, 56, 10, 6, 8, 80]

'''
