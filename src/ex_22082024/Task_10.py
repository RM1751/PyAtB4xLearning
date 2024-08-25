# Write factorial program

n = int(input("Enter a Number: "))
factorial = 1
for i in range(n, 1, -1):
    factorial = factorial * i

# Include the last number 1 in the output string and finalize the calculation


print(f"factorial of {n} = ", factorial)
