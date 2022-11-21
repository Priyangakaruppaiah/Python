# enter the prime number starting to ending in given string
n1=int(input())
n2=int(input())
for i in range(n1,n2):
    c=0
    for j in range(2,i):
        if(i%j==0):
            c=1
    if(c==0):
        print(i)
    
'''
OUTPUT:
3
79
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73

'''


      
