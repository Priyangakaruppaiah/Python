#Remove the vowels in given string and count the consonants
n=str(input("enter the string:"))
p=""
r=""
for i in n:
    if i in('a','e','i','o','u','A','E','I','O','U',' '):
      i=" "
    p=p+i
  #  p=p+i 
print(p) 
for i in range(0,len(p)):
    for j in range(i+1,len(p)):
        c=0
        if(p[i]!=' '):
            c=p.count(p[i])
        if p[i] not in r:
           r=' '+p[i] 
           print(r,c)
