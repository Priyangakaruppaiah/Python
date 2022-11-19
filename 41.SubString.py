# Find the palimdrone in given substring
s=input("Enter the string:")
wor=''
max_len=0
for i in range(0,len(s)):
    for j in range(i+1,len(s)):
        b=s[i:j+1]
        if(b==b[::-1]):
            if(max_len<len(b)):
                max_len=len(b)
                wor=b
print(wor)

'''
OUTPUT:
Enter the string:sdfdsghjjh
sdfds
'''
