# Remove duplicate in given string
n=[1,3,6,3,4,5,4,6,7]
n1=len(n)
res = []
for i in n:
    if i not in res:
        res.append(i)
print(str(res))
n1=len(res)
print(n1)

'''
OUTPUT:
[1, 3, 6, 4, 5, 7]
6

'''
