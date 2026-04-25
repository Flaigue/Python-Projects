import random
import subprocess
import os
import time

# Display game introduction and rules
print("-" * 50)
print("Welcome to the Hot and Cold Game")
print("-" * 50)
print("Rules: ")
print("-" * 50)
print("The system will pick a number between 0 and 100.\n"
      "The value is chosen randomly and you must try to guess it.\n"
      "The program will give hints if the value is: \n"
      "'Very Hot', 'Hot', 'Warm', 'Cold', 'Very Cold' or 'Frozen'.")
print("-" * 50)

# Input validation function to ensure the user enters a valid integer between 0-100
def filter_input():
    while True:
        raw_value = input(": ")
        if raw_value.isdigit():
            filtered_value = int(raw_value)
            if 0 <= filtered_value <= 100:
                return filtered_value
            else:
                print("Input must be in the range of 0 to 100.")
        else:
            print("Invalid input, the input must be an integer.")

# Cross-platform command to clear the terminal screen
def clear_screen():
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True)

# Handles game restart or exit logic
def exit_menu():
    global attempts, chosen_num
    while True:
        answer = input("Do you want to try again? ").lower().strip()
        if answer in ["yes", "y", "sure", "obviously", "clearly"]:
            print("-" * 50)
            attempts = 0
            chosen_num = random.randint(1, 100)
            print("Restarting the Game", end="")
            # Visual feedback for restarting
            for _ in range(3):
                time.sleep(1)
                print(".", end="", flush=True)
            time.sleep(0.5)
            print() # New line after dots
            return True
        elif answer in ["no", "n", "nope", "not at all"]:
            print("Game closed.")
            exit()
        else:
            print("Invalid input, please try again.\n")

# Initial Game Setup
attempts = 0
chosen_num = random.randint(1, 100)
clear_screen()

# Main Game Loop
while True:
    guess = filter_input()

    # Victory Condition Check
    if chosen_num == guess:
        print("-" * 50)
        if attempts == 0:
            print("Congratulations! You got it right on the first try!")
        else:
            print("Congratulations! You got it right!")
            print(f"Attempts made: {attempts + 1}")
        print("-" * 50)
        exit_menu()
        time.sleep(1)
        clear_screen()
        continue

    # Hint Logic for incorrect guesses
    else:
        diff = abs(chosen_num - guess)
        attempts += 1
        print("-" * 50)
        print(f"Attempt/s: {attempts}")
            
        if diff <= 5:
            print("Hint: Very Hot")
        elif diff <= 10:
            print("Hint: Hot")
        elif diff <= 15:
            print("Hint: Warm")
        elif diff <= 20:
            print("Hint: Cold")
        elif diff <= 25:
            print("Hint: Very Cold")
        else:
            print("Hint: Frozen")

        # Loss Condition Check (Max 5 attempts)
        if attempts == 5:
            print("-" * 50)
            print(f"Game Over! The drawn number was: {chosen_num}.")
            exit_menu()
            clear_screen()
            continue
