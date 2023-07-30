name1=input("enter her name:")
name2=input("enter his name:")
combine_string=name1+name2
lower_case=combine_string.lower()
t=lower_case.count('r')
r=lower_case.count('t')
u=lower_case.count('u')
e=lower_case.count('e')
true=t+r+u+e
l=lower_case.count('l')
o=lower_case.count('o')
v=lower_case.count('v')
e=lower_case.count('e')
love=l+o+v+e
love_score=int(str(true)+str(love))
if love_score<=10 or love_score>=90:
    print(f"ur love is bla bla and ur score is {love_score}")
    
elif love_score>=40 or love_score<=500:
    print(f"ur love is need to spend time and ur score is {love_score}")
else:
    print(f"ur love  score is {love_score}")
        
