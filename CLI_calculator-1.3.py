# A more advanced CLI calculator with history feature. 
print("Thanks for using my calculator!")
print("You can perform addition, subtraction, multiplication, and division.\n")

# Define functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

# Start the main loop
while True:
    print("\nChoose your operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("6. History")

    choice = int(input("Make you choice between 1 - 6: "))


    history = []  # To store all past results

    # Only ask for numbers if the choice is valid
    if choice in [1, 2, 3, 4]:
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue  # Restart the loop

        if choice == 1:
            result = add(a, b)

        elif choice == 2:
            result = subtract(a, b)

        elif choice == 3:
            result = multiply(a, b)

        elif choice == 4:
            result = division(a, b)

        print("Result:", result)

        #Let's save all our calculations
        operators = ['+', '-', '*', '/']
        history.append(f"{a} {operators[choice-1]} {b} = {result}")



    elif choice == 5:
        print("Goodbye! Thanks for using my calculator. I am still working on improvements.")
        break  # Exit the loop

    elif choice == 6:
        if history:
            print("\nCalculation History:")
        for i, record in enumerate(history, start=1):
            print(f"{i}. {record}")
        
        else:
            print("You haven't performed any operation yet.")

    else:
        print("Invalid choice! Please enter 1, 2, 3, 4, or 5.")
