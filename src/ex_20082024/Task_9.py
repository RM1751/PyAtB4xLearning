# Write a program that prints numbers from 1 to 100. # Loop For However, for multiples of 3, print "Fizz" instead of
# the number, and for multiples of 5, print "Buzz." For numbers that are multiples of both 3 and 5, print "FizzBuzz."
# Loop through numbers from 1 to 100
for i in range(1, 100 + 1):
    # Check for multiples of both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Check for multiples of 3
    elif i % 3 == 0:
        print("Fizz")
    # Check for multiples of 5
    elif i % 5 == 0:
        print("Buzz")
    # If not a multiple of 3 or 5, print the number
    else:
        print(i)
