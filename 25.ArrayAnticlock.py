# Array rotation in anti clockwise
arr=[1,2,3,7,5,78,34,56]
n=len(arr)
k=int(input("Enter the rotation:"))
for i in range(0,k):
    temp=arr[n-1];
    for j in range(n-1,-1,-1):
        arr[j]=arr[j-1]
    arr[0]=temp
print(arr)    

"""
OUTPUT:
Enter the rotation:3
[78, 34, 56, 1, 2, 3, 7, 5]
"""
