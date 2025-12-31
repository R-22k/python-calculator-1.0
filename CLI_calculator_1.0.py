#A simple calculator that performs basic arithmetic calculations.
a = float(input("Enter an integer of your choice: "))
b = float(input("Another one:"))

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def division(a,b):
    return a / b

print("Addition:", add(a,b))
print("Subtraction: ", subtract(a,b))
print("Multiplication: ", multiply(a,b))
print("Division: ", division(a,b))