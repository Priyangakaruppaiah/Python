# Rotate middle elements in list except first and last digit
a=[2,4,6,7,8]
n=len(a)
k=int(input("enter the rotatin"))
for i in (0,n):
    t=a[n-2]
    for j in range(n-2,0,-1):
        a[j]=a[j-1]
    a[1]=t 
print(a)    

'''
OUTPUT:
enter the rotatin3
[2, 6, 7, 4, 8]
'''
