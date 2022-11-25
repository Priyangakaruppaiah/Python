# array element rotation in ascending and descending order 
n=int(input("Enter the number:"))
a=[]
for i in range(0,n):
    a.append(int(input()))
print(a)
k=int(input("Enter the rotation"))
for i in range(0,k):
    for j in range(i+1,k):
        if(a[i]<a[j]):
            t=a[i]
            a[i]=a[j]
            a[j]=t
for i in range(k,n):
    for j in range(k+1,n):
        if(a[i]>a[j]):
            t=a[i]
            a[i]=a[j]
            a[j]=t

print(a)
