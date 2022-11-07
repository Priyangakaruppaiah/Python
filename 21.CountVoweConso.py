# count vowels and consonants in given string
str=input()
r=''
s=len(str)
c=0
for i in str:
    if i in('a','e','i','o','u','A','E','I','O','U'):
        i=''
        c=c+1
    r=r+i    
print("Vowels is:",c)
print("Consonants is:",s-c)
