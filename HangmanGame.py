from os import system
import random
import time

aquatic_animals = ["Baleia", "Golfinho", "Tubarao", "Tartaruga", "Polvo", "Lula", "Sardinha", "Caranguejo", "Lagosta", "Cavalo Marinho", "Estrela Do Mar", "Pinguim", "Foca", "Lontra", "Orca", "Arraia", "Camarao", "Medusa", "Bacalhau", "Tubarao Martelo"]
terrestrial_animals = ["Cachorro", "Gato", "Elefante", "Leao", "Tigre", "Girafa", "Zebra", "Macaco", "Coelho", "Cavalo", "Vaca", "Porco", "Rato", "Esquilo", "Urso", "Raposa", "Canguru", "Cervo", "Lobo", "Hamster"]
aerial_animals = ["Aguia", "Beija Flor", "Papagaio", "Coruja", "Gaviao", "Pombo", "Andorinha", "Pardal", "Tucano", "Arara", "Pica Pau", "Morcego", "Falcao", "Cisne", "Ganso", "Pato", "Cegonha", "Flamingo", "Peru", "Galinha"]

animals_groups = ["Aquático", "Terrestre", "Aéreo"]
indice_group = random.randint(0, 2)
categorias_animais  = {
    "Aquático": aquatic_animals, 
    "Terrestre": terrestrial_animals, 
    "Aéreo": aerial_animals
}
nomes_categorias = list(categorias_animais.keys())
tema_sorteado = random.choice(nomes_categorias)
choisen_animal = random.choice(categorias_animais[tema_sorteado]).upper()

lenght_name = len(choisen_animal)
hidden_name = [" " if letra == " " else "_" for letra in choisen_animal]

erros = 0
acertos = 0
lista_acertos = []
lista_erros = []

dica_usada = False

stages = [
    """
_ _ _  
|   |  
|   O  
|  /|\ 
|  / \ 
|_  
    """,

    """
_ _ _
|   |
|   O
|   |\ 
|  / \ 
|_
    """,

    """
_ _ _
|   |
|   O
|   |
|  / \ 
|_
    """,

    """
_ _ _
|   |
|   O
|   |
|    \ 
|_
    """,

    """
_ _ _ 
|   |
|   O
|   |
|     
|_    
    """,

    """
_ _ _
|   |
|   O
|
|
|_
    """,
    """
_ _ _
|   |
|
|
|
|_
    """
]

derrota = False

while "_" in hidden_name:
    system("clear")

    if erros == 6:
        system("clear")
        print(stages[6])
        derrota = True
        break
    print(stages[erros])
    print(" ".join(hidden_name))
    print("")
    palpite = input("Palpite: ").upper()
    if palpite == "dica":
        if dica_usada == True:
            print("A dica já foi usada!.")
            time.sleep(1)
            continue
        print(f"Dica: {tema_sorteado}")
        dica_usada = True
        time.sleep(1)
        continue

    comprimento_palpite = len(palpite)
    if comprimento_palpite != 1 and palpite != "dica":
        print("Só é permitido 1 letra por tentativa, tente novamente.")
        time.sleep(1)
        continue
        
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
        time.sleep(1)
if derrota:
    print("Gamer Over.",end="")
    time.sleep(0.5)
    print(".",end="")
    time.sleep(0.5)
    print(".",end="")
    time.sleep(0.5)
    print(".")
    print("")
    print("-= Estatisticas do jogo =-")
    print(f"Erros: {erros}")
    print(f"Acertos: {acertos}")
    print(f"Letras Reveladas/Acertadas: {lista_acertos}")
    print(f"Letras Erradas: {lista_erros}")
    print("")
    print(f"Nome do Animal: {choisen_animal}")
else:
    print("Parabéns, você venceu o jogo.")
    print("[Estatisticas do jogo]")
    print(f"Erros: {erros}")
    print(f"Acertos: {acertos}")
    print(f"Letras Reveladas/Acertadas: {lista_acertos}")
    print(f"Letras Erradas: {lista_erros}")