# (!) Not operator Example for int
a = 10
b = 20
result = (a != b)
print(result)

# Ternary Operator
my_age = int(input("Enter your Age :"))
print("i will go to Goa" if my_age >= 18 else "i can not go , Stay home")
# OR we can write this code below formate as wll
if my_age > 18:
    print("i can go Goa ")
else:
    print("You can not go , stay Home")
    # OR we can write this code below formate as wll
print("i will go to Goa" if int(input("Enter your Age :")) >= 18 else "i can not go , Stay home")

My_score = int(input(" Enter your score of English suibject :"))
#print(if My_score >50 "i am pass" else " i am fail") # this is not correct syntax
print("i am pass" if My_score >50  else " i am fail")
 


