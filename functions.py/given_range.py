# Define a function named 'test_range' that checks if a number 'n' is within the range 3 to 8 (inclusive)
def test_range(n):
    # Check if 'n' is within the range from 3 to 8 (inclusive) using the 'in range()' statement
    if n in range(3, 9):
        # If 'n' is within the range, print that 'n' is within the given range
        print(f"{n} is in the range")
    else:
        # If 'n' is outside the range, print that the number is outside the given range
        print("The number is outside the given range.")

# Call the 'test_range' function with the argument 5
test_range(5)