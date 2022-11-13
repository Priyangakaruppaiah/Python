# Reverse a words in given sentence
s="Geeks for is Geeks"
s1=s.split(" ")
n=len(s1)
for i in s1:
    s2=i[::-1]
    print(s2)
    
'''
OUTPUT:
skeeG
rof
si
skeeG
'''
