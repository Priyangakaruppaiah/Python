# give the month and year and display number of days in particular month
y=int(input("Enter the year:"))
if((y%400==0 and y%100==0)or(y%100!=0 and y%4==0)):
    d={'jan':31,'feb':29,'mar':31,'apr':30,'may':31,'june':30,'july':31,'aug':31,'sep':'30','octo':31,'nov':30,'dec':31}
    m=input("Enter the month:")
    out=d[m]
    print(out)
else:
    d={'jan':31,'feb':28,'mar':31,'apr':30,'may':31,'june':30,'july':31,'aug':31,'sep':'30','octo':31,'nov':30,'dec':31}
    m=input("Enter the month:")
    out=d[m]
    print(out)

    '''
    OUTPUT:
    Enter the year:2002
    Enter the month:feb
    28

    '''
