# Find the difference in given list
a=[1,4,7,9]
n=len(a)
for i in range(0,n-1):
    for j in range (i+1,i+2):
        if(a[i]<a[j]):
            c=1
            b=a[i]
            for k in range(b,a[j]-1):
                print(c+b,end=" ")
                c=c+1
        else:
            break
'''
OUTPUT:
2 3 5 6 8
'''
