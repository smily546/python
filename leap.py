year=int(input("enter a year:"))
if year %4==0:
    print("it is a leap year")
    if year %100==0:
       print("it is not aleap year")
       if year%400==0:
           print("it's a leap year")
       else:
           print("it's not leap year")
    else:
        print("aleap year")
else:
    print("it is not a leap year")
