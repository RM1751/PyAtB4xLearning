# Write program to calculate Area OF circle if redius is given
import math

radios = int(input("Enter the radios of the circle\n"))
print(radios)
print(math.pi)
Area = math.pi * math.pow(radios, 2)
print(f"Area of circle is =>, {Area:.2f}")
