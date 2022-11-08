n=int(input())
s=0
for i in range(1,(n//2)+1):
    rem=n%i
    if(rem==0):
        s=s+i
if(s==n):
    print("perfect number")
else:
    print("Not perfect number")
