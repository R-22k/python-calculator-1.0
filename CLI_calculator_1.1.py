#A little bit advanced calculator that performs operations based on user choice
print("Let's work with the simplest of algebraic operations.")
print("Choose your operation of choice:")
print("""Do take note of the following:
      1 signifies Addition
      2 signifies Subtraction
      3 signifies Multiplication
      4 signifies Division
""")

a = float(input("Enter an integer of your choice: "))
b = float(input("Another one:"))

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"


choice = int(input("Please enter your choice of operation: "))

if choice == 1:
    result = add(a,b)
    print("Answer: ", result)
elif choice == 2:
    result = subtract(a,b)
    print("Answer: ", result)
elif choice == 3:
    result = multiply(a,b)
    print("Answer: ", result)
elif choice == 4:
    result = division(a,b)
    print("Answer: ", result)
else:
    print("Invalid choice. Do try again.")
