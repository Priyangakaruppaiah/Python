a=int(input())
n=(a*2)-1
b1=[]
for i in range(0,n):
    b2=[]
    for j in range(0,n):
        b2.append(0)
    b1.append(b2)
  
s=0
e=n-1
k=1
while(k<=n):
    for i in range(s,e+1):
        for j in range(s,e+1):
            if(i==s or j==e or i==e or j==s):
               b1[i][j]=k
       # print("\n")
    s=s+1 
    e=e-1
    k=k+1
   
for i in range(0,n):
    for j in range(0,n):
        print(b1[i][j],end=" ")
    print("\n")

'''
OUTPUT:
4
1 1 1 1 1 1 1 

1 2 2 2 2 2 1 

1 2 3 3 3 2 1 

1 2 3 4 3 2 1 

1 2 3 3 3 2 1 

1 2 2 2 2 2 1 

1 1 1 1 1 1 1 

'''
