# #Create a program , take 2 inputs from the user num1, num2 and give them
# max
# pow num1 to num2
# sub, mul, sum, div.
# Format your out with f{""}

num1 = int(input("Enter number1 : "))
num2 = int(input("Enter number2 : "))
print(num1)
print(type(num1))
print(num2)
print(type(num2))
maximum_number = max(num1, num2)
print("Maximum of number is :", maximum_number)
print(type(maximum_number))
power_number = pow(num1, num2)
print("power of number :", power_number)
subtract = num1 - num2
print("subtract of number is :", subtract)
multiply = num1 * num2
print("multiplication of number is :", multiply)
divide = num1 / num2
print("dividend of  number is ", divide)
print("Formated_num1 is : ", f"{num1: .5f}")
print("Formated_num2 is : ", f"{num2: .5f}")
