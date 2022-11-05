list=[34,78,65,3,87,7,1]
n=len(list)
k=66
for i in range(n):
    for j in range(i+1,n):
        if(list[i]+list[j]==k):
            print(list[i],list[j])

#OUTPUT:
#65 1
