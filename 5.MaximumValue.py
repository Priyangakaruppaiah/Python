//Find the maximum value in array
n=int(input("enter the number"))
a=[]
for i in range(0,n):
    m=int(input("enter the number"))
    a.append(m)
    i=+1
m=a[0]
i=1
if(m<a[i]):
    m=a[i]
    i=i+1
print ("Maximum vakue is:",m)    
