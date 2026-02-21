from os import system
import random
num_random = int
user = int
system("clear")
num_random = random.randint(1, 5)
tentativas = 0

while num_random != user:
    
    num_random = random.randint(1, 5)
    user = int(input(": "))
    tentativas += 1

    if user == num_random:
        print("Kaboom")
        print(num_random)
        print(f"Tentativas: {tentativas}")
        sair = str(input("Quit, Leave, Exit? ")).lower().strip()
        if sair in ("yes", "yeah", "yup", "y"):
            break
        elif sair in ("no, not"):
            pass
        else:
            print("Invalid Input, try again")
            pass
