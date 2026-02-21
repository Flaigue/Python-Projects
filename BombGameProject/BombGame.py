import os
import random
import time

def play():
    os.system("cls" if os.name == "nt" else "clear")
    bomb = random.randint(1, 5)
    attempts = 0

    while True:
        try:
            user_attempt = int(input("=> "))
            if user_attempt == bomb:
                print("Game Over buddy")
                print("Unfortunately, you picked the wrong number.")
                leave_value = leave()
                if leave_value == True:
                    print("Closing the game", end=" ")
                    time.sleep(1)
                    print(".", end=" ")
                    time.sleep(1)
                    print(".", end=" ")
                    time.sleep(1)
                    print(".")
                    return
                else:
                    print("Restarting the game", end=" ")
                    time.sleep(1)
                    print(".", end=" ")
                    time.sleep(1)
                    print(".", end=" ")
                    time.sleep(1)
                    print(".")
                    play()
            else:
                attempts += 1
                print(f"The number {user_attempt} you have chosen is secure, you can continue.")
        except ValueError:
            print("Invalid input, this input just accept numbers into 1 to 5")
            pass
def leave():
    while True:
        print("This option just accept 'yes' ou 'no'.")
        choise = str(input("You wanna leave ?: ")).lower().strip()
        if choise == "yes":
            return True
        elif choise == "no":
            return False
        else:
            print("Invalid input, try again.")
            os.system("cls" if os.name == "nt" else "clear")
play()
