
# try:
#
#     a = int(input("Ent the num1")) # ValueError: invalid literal for int()
#     b = int(input("Ent the num2"))
#     c = a / b # ZeroDivisionError: division by zero - Lab149.py", line 3
#     print("Result Div is ", c)
# except Exception as e:
#     print(e)


while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
