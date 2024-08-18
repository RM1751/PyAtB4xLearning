# Create a program that takes two numbers as input and prints whether the first number is greater than, less than,
# or equal to the second number.
import math

first_number = float(input("Enter the first number :"))
second_number = float(input("Enter the Second number :"))
if first_number > second_number:
    print("Yes first number is greater than second number")
else:
    print("first number number is less than second number  ")

# Develop a Python script that calculates the square and cube of a given number.
given_number = float(input("Enter the number "))
squire = math.pow(given_number, 2)
cube = math.pow(given_number,3)
print(squire)
print(cube)
