# pattern_drawing.py

# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop to iterate through rows
while row < size:
    # Use for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")  # stay on the same line
    print()  # move to the next line after each row
    row += 1

