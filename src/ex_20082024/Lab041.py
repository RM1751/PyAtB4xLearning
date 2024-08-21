# Grade Calculator :
# write a program that calculates and displays the letter grade for a given numerical score
A: 900 - 100
B: 80 - 90
C: 70 - 79
D: 60 - 69
F: 0 - 59
numerical_score = int(input("Enter score :\n"))
grade = "F"
if 900 <= numerical_score <= 100:

    print("your grade is ", "A")
elif 80 <= numerical_score <= 90:
    print("Your grade is", "B")
elif 70 <= numerical_score <= 79:
    print("your grade is ", "C")
elif 60 <= numerical_score <= 69:
    print("your grade is ", "D")
else:
    print("your grade is ", "F")
