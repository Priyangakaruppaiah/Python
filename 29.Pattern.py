# pattern
def pattern(n):
    num=65
    for i in range(0,n):
        for j in range(i+1,n+1):
           ch=chr(num)
           print(ch)
        num+=1   
        print('\r')    
n=5
pattern(n)

'''
OUTPUT:
  A A A A A
  B B B B
  C C C
  D D
  E
  '''
