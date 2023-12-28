import sys

def calculate_square(number):
    return number ** 2

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <number>")
        sys.exit(1)

    # Get the command-line argument (assuming it's a number)
    try:
        number = float(sys.argv[1])
    except ValueError:
        print("Error: Please provide a valid number.")
        sys.exit(1)

    # Calculate the square of the number
    result = calculate_square(number)

    # Display the result
    print(f"The square of {number} is: {result}")

if __name__ == "__main__":
    main()
