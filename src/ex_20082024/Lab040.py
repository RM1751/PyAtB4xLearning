# find maximum number between three number
num1 = input("Enter num1 :\n")
num2 = input("Enter num2 :\n")
num3 = input("Enter num3 :\n")

if num1 > num2 and num1 > num3:
    print("maximum number is ", num1)
elif num2 > num1 and num2 > num3:
    print("maximum number is ", num2)
else:
    print("maximum is ", num3)
# using max function
result = max(num1, num2, num3)
print("maximum of number is ", result)
