size = int(input("Enter the size of the pattern: "))

# Ensure the size is a positive integer
while size <= 0:
    print("Please enter a positive integer.")
    size = int(input("Enter the size of the pattern: "))

# Initialize the row counter for the while loop
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print the asterisks for the current row
    for _ in range(size):
        print("*", end="")

    # Print a newline after each row
    print()

    # Move to the next row
    row += 1
