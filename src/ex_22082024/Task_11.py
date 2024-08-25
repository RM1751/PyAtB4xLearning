# Get the number of terms in the Fibonacci series from the user
n = int(input("Enter the number of terms: "))

# Initialize the first two terms of the Fibonacci series
a, b = 0, 1

print("Fibonacci Series:")

# Generate and print the Fibonacci series
for i in range(n):
    print(a, end=" ")  # Print the current term
    a, b = b, a + b    # Update the values of a and b

print()  # Print a newline at the end
