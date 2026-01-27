import os
import random
import time

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

aquatic_animals = ["Baleia", "Golfinho", "Tubarao", "Tartaruga", "Polvo", "Lula", "Sardinha", "Caranguejo", "Lagosta", "Cavalo Marinho", "EstrelaDoMar", "Pinguim", "Foca", "Lontra", "Orca", "Arraia", "Camarao", "Medusa", "Bacalhau", "TubaraoMartelo"]
terrestrial_animals = ["Cachorro", "Gato", "Elefante", "Leao", "Tigre", "Girafa", "Zebra", "Macaco", "Coelho", "Cavalo", "Vaca", "Porco", "Rato", "Esquilo", "Urso", "Raposa", "Canguru", "Cervo", "Lobo", "Hamster"]
aerial_animals = ["Aguia", "BeijaFlor", "Papagaio", "Coruja", "Gaviao", "Pombo", "Andorinha", "Pardal", "Tucano", "Arara", "PicaPau", "Morcego", "Falcao", "Cisne", "Ganso", "Pato", "Cegonha", "Flamingo", "Peru", "Galinha"]

animals_groups = ["Aquático", "Terrestre", "Aéreo"]
categorias_animais  = {
    "Aquático": aquatic_animals, 
    "Terrestre": terrestrial_animals, 
    "Aéreo": aerial_animals
}

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

derrota = False
continuar = True

while continuar == True:
    derrota = False
    dica_usada = False

    indice_group = random.randint(0, 2) #Sorteia entre 0 a 2, posição

    nomes_categorias = list(categorias_animais.keys())
    tema_sorteado = random.choice(nomes_categorias)
    choisen_animal = random.choice(categorias_animais[tema_sorteado]).lower()

    lenght_name = len(choisen_animal)
    hidden_name = [" " if letra == " " else "_" for letra in choisen_animal]

    erros = 0
    acertos = 0
    lista_acertos = []
    lista_erros = []
    while "_" in hidden_name:
        limpar()

        if erros == 6:
            limpar()
            print(stages[6])
            derrota = True
            break
        print(stages[erros])
        print(" ".join(hidden_name))
        print("")

        #Se o usuario usar a dica
        palpite = input("Palpite: ").lower()

        if palpite == "dica":
            if dica_usada == True:
                print("A dica já foi usada!.")
                time.sleep(1)
                continue
            print(f"Dica: {tema_sorteado}")
            dica_usada = True
            time.sleep(1)
            continue

        #Caso a pessoa escreva mais que 1 letra por palpite
        comprimento_palpite = len(palpite)
        if comprimento_palpite != 1 and palpite != "dica":
            print("Só é permitido 1 letra por tentativa, tente novamente.")
            time.sleep(1)
            continue

        if palpite in lista_acertos or palpite in lista_erros:
            print("Tu já tentaste essa letra, escolha uma diferente!")
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
            if erros > 0:
                print(f"Erros: {erros}")
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
        print("")
        print("Parabéns, você venceu o jogo.")
        print("")
        print("-= Estatisticas do jogo =-")
        print(f"Erros: {erros}")
        print(f"Acertos: {acertos}")
        print(f"Letras Reveladas/Acertadas: {lista_acertos}")
        print(f"Letras Erradas: {lista_erros}")
    saida = input("Gostaria de tentar denovo ?, escreva (sim) para continuar, qualquer outro input o programa será fechado: ")
    if saida != "sim":
        continuar = False
print("Programa encerrando",end="")
time.sleep(1)
print(".",end="")
time.sleep(1)
print(".",end="")
time.sleep(1)
print(".")
exit()