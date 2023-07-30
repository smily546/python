height=int(input("enter the height:"))
if height>3:
    print("can ride")
    age=int(input("enter the age:"))
    if age<12:
        print("please pay 50 rs")
    elif age<30:
        print("please pay 100 rs")
    else:
        print("no need to pay")
else:
    print("can't ride")
