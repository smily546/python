size=input("enter a size of pizza(s/m/l):")
bill=0
if size=='s' or size=='S':
    bill+=100
    print("small size pizza is 100 rs")
elif size=='m' or size=='M':
    bill+=200
    print("medium size pizza is 200 rs")
else:
    bill+=300
    print("large size pizza is 300 rs")
pepper=input("do you want pepper (y/n)")
if pepper=='y' or pepper=='Y':
   if size=='s' or size=='S':
     bill+=50
     print("we add pepper and for 50 rs")
   else:
       bill+=100
       print("we add pepper and for 100 rs")
cheese=input("do you want pepper (y/n)")
if cheese=='y' or cheese=='Y':
    bil+=20
    print("add cheese for 20 rs")
print(f"the total bill is {bill}")    
       
        
        
