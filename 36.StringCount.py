# count the characters in given string
a=input("enter the string:")
n=len(a)
c=1
e=''
if(1>n+1):
    print(a,c)
else:   
    i=0
    while(i<n):
        c=1
        for j in range(i+1,n):
           if(a[i]==a[j]):
               c=c+1
       
           else:
                break
        print(a[i],c,end=" ")
        i=i+c
