#Find the exponent
base=int(input())
expo=int(input())
result=base
if(expo!=0):
    for i in range(expo-1):
        result=result*base

else:
    result==1
print(result) 
        
