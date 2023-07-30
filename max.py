numbers=input("enter the list numbers :")
num_list=numbers.split()
count=0
for num in num_list:
    count+=1
print(f"the count of these numbers:{count}")    
for i in range(count):
   num_list[i]=int(num_list[i])
max=num_list[0]
for number in num_list:
    if number > num_list:
        max=number
print(f"the max is {max}")        
