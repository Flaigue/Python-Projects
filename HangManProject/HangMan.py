import os
import random
import time

# Helper to clear the terminal screen
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

# Animal datasets by category
aquatic_animals = ["Baleia", "Golfinho", "Tubarao", "Tartaruga", "Polvo", "Lula", "Sardinha", "Caranguejo", "Lagosta", "Cavalo Marinho", "Estrela Do Mar", "Pinguim", "Foca", "Lontra", "Orca", "Arraia", "Camarao", "Medusa", "Bacalhau", "Tubarao Martelo"]
terrestrial_animals = ["Cachorro", "Gato", "Elefante", "Leao", "Tigre", "Girafa", "Zebra", "Macaco", "Coelho", "Cavalo", "Vaca", "Porco", "Rato", "Esquilo", "Urso", "Raposa", "Canguru", "Cervo", "Lobo", "Hamster"]
aerial_animals = ["Aguia", "Beija Flor", "Papagaio", "Coruja", "Gaviao", "Pombo", "Andorinha", "Pardal", "Tucano", "Arara", "Pica Pau", "Morcego", "Falcao", "Cisne", "Ganso", "Pato", "Cegonha", "Flamingo", "Peru", "Galinha"]

animals_categories = {
    "Aquático": aquatic_animals,
    "Terrestre": terrestrial_animals,
    "Aéreo": aerial_animals
}

# Hangman ASCII art stages
stages = [
    r"""
_ _ _  
|   |  
|   O  
|  /|\ 
|  / \ 
|_  
    """,
    r"""
_ _ _
|   |
|   O
|   |\ 
|  / \ 
|_
    """,
    r"""
_ _ _
|   |
|   O
|   |
|  / \ 
|_
    """,
    r"""
_ _ _
|   |
|   O
|   |
|    \ 
|_
    """,
    r"""
_ _ _ 
|   |
|   O
|   |
|     
|_    
    """,
    r"""
_ _ _
|   |
|   O
|
|
|_
    """,
    r"""
_ _ _
|   |
|
|
|
|_
    """
]

continuar = True

# Main game session loop
while continuar:
    derrota = False
    dica_usada = False

    # Randomly select a category and an animal
    nomes_categorias = list(animals_categories.keys())
    tema_sorteado = random.choice(nomes_categorias)
    choisen_animal = random.choice(animals_categories[tema_sorteado]).lower()

    # Generate the masked word (preserving spaces)
    hidden_name = [" " if letra == " " else "_" for letra in choisen_animal]

    erros = 0
    acertos = 0
    lista_acertos = []
    lista_erros = []

    # Turn-based loop
    while "_" in hidden_name:
        limpar()

        # Check for game over condition
        if erros == 6:
            limpar()
            print(stages[6])
            derrota = True
            time.sleep(1)
            break

        print(stages[erros])
        print(" ".join(hidden_name))
        print("")

        palpite = input("Palpite: ").lower()

        # Handle hint mechanism (allowed once per game)
        if palpite == "dica":
            if dica_usada:
                print("A dica já foi usada!.")
                time.sleep(1)
                continue
            print(f"Dica: {tema_sorteado}")
            dica_usada = True
            time.sleep(1)
            continue

        # Validate input length
        if len(palpite) != 1 and palpite != "dica":
            print("Só é permitido 1 letra por tentativa, tente novamente.")
            time.sleep(1)
            continue

        # Prevent duplicate guesses
        if palpite in lista_acertos or palpite in lista_erros:
            print("Tu já tentaste essa letra, escolha uma diferente!")
            time.sleep(1)
            continue
        
        # Check if guess is correct and update hidden word
        elif palpite in choisen_animal:
            for i in range(len(choisen_animal)):
                if choisen_animal[i] == palpite:
                    hidden_name[i] = palpite
            if palpite not in lista_acertos:
                lista_acertos.append(palpite)
                acertos += 1
        else:
            erros += 1
            lista_erros.append(palpite)
            if erros > 0:
                print(f"Erros: {erros}")
            time.sleep(1)

    # Post-game results and statistics
    if derrota:
        limpar()
        print("Game Over.", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print("\n\n-= Game Statistics =-")
        print(f"Errors: {erros}")
        print(f"Hits: {acertos}")
        print(f"Correct Guesses: {lista_acertos}")
        print(f"Wrong Guesses: {lista_erros}")
        print(f"\nTarget Animal: {choisen_animal}")
    else:
        print("\nCongratulations, you won!")
        print("\n-= Game Statistics =-")
        print(f"Errors: {erros}")
        print(f"Hits: {acertos}")
        print(f"Correct Guesses: {lista_acertos}")
        print(f"Wrong Guesses: {lista_erros}")

    # Replay check
    saida = input("\nTry again? (type 'sim' to continue, any other key to exit): ")
    if saida != "sim":
        continuar = False

# Exit sequence
print("System shutting down", end="")
for _ in range(3):
    time.sleep(1)
    print(".", end="", flush=True)
exit()