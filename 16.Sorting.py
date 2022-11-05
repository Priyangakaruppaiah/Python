#Sorting without predefined function
list=[54,5632,785,76,7,6,8,74769]
n=len(list)

for i in range(n):
    for j in range(i+1,n):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]

print(list)            
            
