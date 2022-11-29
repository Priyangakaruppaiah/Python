n=int(input())
asciiv=65
for i in range(0,n+1):
    for j in range(0,n-i):
        print(" ",end=" ")
    for j in range(0,2*i-1):
        alph = chr(asciiv) 
        print(alph,end=" ")
        asciiv=asciiv+1
    print("\n")
 '''
 OUTPUT:
  4
        

      A 

    B C D 

  E F G H I 

J K L M N O P 
  
 '''
