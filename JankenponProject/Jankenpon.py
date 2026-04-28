import random
import time
import os
import subprocess

# Clears the terminal screen based on the Operating System
def clear_screen():
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True)

# Handles the post-game menu for restarting or exiting
def exit_menu():
    while True:
        print("")
        choice = input("Do you want to restart the Game? (y/n): ").strip().lower()
        if choice in ["yes", "y"]:
            clear_screen()
            return True
        elif choice in ["no", "n"]:
            print("Program closing", end="")
            # Loop for the visual dots effect
            for _ in range(3):
                time.sleep(1)
                print(".", end="", flush=True)
            exit()
        else:
            print("Invalid input, try again.")

clear_screen()

# Main Game Loop
while True:
    menu_text = " [ 1 ] = Rock [ 2 ] = Paper [ 3 ] = Scissors "
    print("=" * len(menu_text))
    print(menu_text)
    print("=" * len(menu_text))

    # Input validation loop with error handling
    while True:
        try:
            user_choice = int(input("-> "))
            if user_choice in (1, 2, 3):
                break
            print("Please choose 1, 2 or 3.")
        except ValueError:
            print("That's not a number! Try again.")
    
    print("=" * len(menu_text))

    # Dramatic countdown effect
    time.sleep(0.5)
    print("Rock")
    time.sleep(0.5)
    print("Paper")
    time.sleep(0.5)
    print("Scissors !!!")
    print("=" * len(menu_text))

    # Machine logic and dictionary for mapping values to strings
    choices_list = [1, 2, 3]
    machine_choice = random.choice(choices_list)
    options_map = {
        1: "Rock",
        2: "Paper",
        3: "Scissors"
    }

    # Data-driven win conditions (Winner, Loser)
    win_conditions = [
        (1, 3), # Rock beats Scissors
        (2, 1), # Paper beats Rock
        (3, 2)  # Scissors beats Paper
    ]

    # Outcome logic using the tuple comparison method
    if user_choice == machine_choice:
        print("It's a Draw!")
    elif (user_choice, machine_choice) in win_conditions:
        print("Victory !!!")
    else:
        print("Defeat !!!")

    # Display results for both players
    print(f"User = {user_choice} '{options_map[user_choice]}'")
    print(f"Machine = {machine_choice} '{options_map[machine_choice]}'")

    exit_menu()

    # Software created on 05/12/2025
    # SSoftware updated on 27 April 2026