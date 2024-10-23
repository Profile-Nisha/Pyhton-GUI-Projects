# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Main function
def main():
    try:
        # Input from the user
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        
        # Adding the numbers
        result = add_numbers(number1, number2)
        
        # Displaying the result
        print(f"The sum of {number1} and {number2} is {result}.")
        
    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
