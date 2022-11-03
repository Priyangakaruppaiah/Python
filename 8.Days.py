//Find the number of days in a given month
n=int(input("Enter the month:"))
year=int(input("Enter the year:"))
if((year%400==0 and year%100==0)or(year%400==0 and year%100==0)):
    if(n==2):
        printf("The days is:29")


if(n==2):
    print("The days is:28")
if(n==1 or n==3 or n==5 or n==7 or n==8): 
    print("the days is:31")
else:
    print("the days is:30")

    
