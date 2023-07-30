height=int(input("enter a height:"))
bill=0
if height>=3:
   print("can ride")
   age=int(input("enter a age:"))
   if age<12:
       bill=50
       print("pay 50 rs")
   elif age<18:
       bill=150
       print("pay 150")
   elif age==18:
       bill=500
       print("500rs")
   else:
     
       print("pay no rs")
   photo=(input("do you want photo:")
   if photo=='y' or photo=='Y':
          bill=bill+50
   print(f"the total billis {bill}"      
       else:
    print("can't ride")
