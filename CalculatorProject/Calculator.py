import time
import os

# --- Mathematical Functions ---
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    # Prevention against division by zero error
    if num2 == 0:
        return "Error, Division by zero."
    else:
        return num1 / num2

# --- Utility Functions ---
def getnumber(text):
    """Handles input validation to ensure only floats are accepted."""
    while True:
        try:
            value = float(input(text))
            return value   # Exits the function and returns the numeric value
        except ValueError:
            print("Invalid input, try again.")

# --- Mapping Operators to Functions ---
operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# --- Main Application Loop ---
while True:
    # 1. Get the first valid number
    num1 = getnumber("Value Here: ")
    
    # 2. Loop until a valid operator is provided
    while True:
        op = str(input("=> "))
        if op in operators:
            break # Exit the operator loop only
        else:
            print("Invalid input, try again.")
    
    # 3. Get the second valid number
    num2 = getnumber("Another Value Here: ")
    
    # 4. Execute the function stored in the dictionary and print the result
    print(operators[op](num1, num2))
    
    # 5. Checkpoint: Empty input to exit, any key to restart
    choise = str(input("Press ENTER to exit or any key to restart: "))
    
    if choise.strip() == "":
        print("Closing the program", end=" ", flush=True)
        # Visual exit sequence
        for _ in range(3):
            time.sleep(1)
            print(".", end=" ", flush=True)
        print()
        break # Exit the main calculator loop
    else:
        # Clear terminal screen based on OS
        os.system("cls" if os.name == "nt" else "clear")
