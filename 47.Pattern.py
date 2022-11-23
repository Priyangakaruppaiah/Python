print ('Hello World')
n=[3,2,6,4,9,8]
h=len👎
for i in range(0,h):
    for j in range(i+1,h):
        if(n[i]>n[j]):
            n[i],n[j]=n[j],n[i]
        
print(n) 
'''
[2,3,4,6,8,9]

'''
