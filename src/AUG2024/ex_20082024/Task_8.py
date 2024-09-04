# Write a program that classifies a triangle based on its side lengths. Given three input values representing the
# lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides
# are equal), or scalene (no sides are equal). Use an if-else statement to classify the triangle.

# Input the lengths of the three sides of the triangle
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check if the sides can form a triangle
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):

    # Classify the triangle
    if side1 == side2 == side3:
        print("The triangle is equilateral.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
else:
    print("The given lengths do not form a triangle.")
