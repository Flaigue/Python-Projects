import os
import random
import time

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') #se o sistema for windows carregar "cls" senão carregar "clear" no terminal

aquatic_animals = ["Baleia", "Golfinho", "Tubarao", "Tartaruga", "Polvo", "Lula", "Sardinha", "Caranguejo", "Lagosta", "Cavalo Marinho", "Estrela Do Mar", "Pinguim", "Foca", "Lontra", "Orca", "Arraia", "Camarao", "Medusa", "Bacalhau", "Tubarao Martelo"]
terrestrial_animals = ["Cachorro", "Gato", "Elefante", "Leao", "Tigre", "Girafa", "Zebra", "Macaco", "Coelho", "Cavalo", "Vaca", "Porco", "Rato", "Esquilo", "Urso", "Raposa", "Canguru", "Cervo", "Lobo", "Hamster"]
aerial_animals = ["Aguia", "Beija Flor", "Papagaio", "Coruja", "Gaviao", "Pombo", "Andorinha", "Pardal", "Tucano", "Arara", "Pica Pau", "Morcego", "Falcao", "Cisne", "Ganso", "Pato", "Cegonha", "Flamingo", "Peru", "Galinha"]

animals_groups = ["Aquático", "Terrestre", "Aéreo"]
categorias_animais  = {
    "Aquático": aquatic_animals, 
    "Terrestre": terrestrial_animals, 
    "Aéreo": aerial_animals
} #dicionario com chaves "Aquático", "Terrestre" e "Aéreo" com values associados as listas encima criadas

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
] #niveis do boneco da forca

while continuar == True: #loop continua enquanto a a variavel continuar (continuar o jogo) for igual a True

    derrota = False #False signigica que a derrota ainda não aconteceu, o jogador ainda está vivo
    dica_usada = False #False significa que a dica ainda não foi usada

    nomes_categorias = list(categorias_animais.keys()) #Variavel que guarda todas as chaves do dicionario "categorias_animais", as chaves são Aquático, Terrestre e Aéreo.
    tema_sorteado = random.choice(nomes_categorias) #Variavel que escolhe aleatoriamente 1 dos valores da variavel nomes_categorias encima, escolhe apenas 1 valor que é Aquático, Terrestre ou Aéreo (por exemplo: Aquático)
    choisen_animal = random.choice(categorias_animais[tema_sorteado]).lower() # Acessa a lista do tema_sorteado e escolhe um animal aleatório em minúsculas. (por exemplo: Tubarao dentro de Aquático)

    hidden_name = [" " if letra == " " else "_" for letra in choisen_animal]

    erros = 0 #Erros do jogador começa com 0 e vai atualizando ao longo do jogo
    acertos = 0 #Acertos do jogador começa com 0 e vai atualizando ao longo do jogo
    lista_acertos = [] #Onde fica armazenado as letras acertadas
    lista_erros = [] #Onde fica armazenado as letras erradas
    while "_" in hidden_name: #Enquanto tiver "_" no hidden_name o jogo continua, significa que enquanto tiver algum "_" no hidden_name o nome do animal ainda não foi revelado completamente
        limpar()

        if erros == 6: #Se os erros for igual a 6 significa que a pessoa perdeu todas as vidas
            limpar()
            print(stages[6]) #Mostrar a forca sem o boneco que significa que o boneco morreu 
            derrota = True #A condição da derrota agora é True 
            time.sleep(1)
            break #Sair do loop do jogo
        print(stages[erros]) #Mostrar o estagio do boneco atual condizente a quantidade de erros
        print(" ".join(hidden_name)) #Transformar o hidden_name de ['_', '_', '_', '_'] para _ _ _ _
        print("")

        #Se o usuario usar a dica
        palpite = input("Palpite: ").lower() #Palpite do jogador, convertido para minusculas para não dar problema

        if palpite == "dica": #Entrar da condição se o palpite for igual a "dica"
            if dica_usada == True: #Se a dica_usada for igual a True significa que a dica já foi usada anteriormente e mostra a frase embaixo
                print("A dica já foi usada!.")
                time.sleep(1)
                continue #Volta ao inicio do loop
            print(f"Dica: {tema_sorteado}") #Se for a primeira vez a usar a dica o player entra nesta condição e mostra a dica
            dica_usada = True #Transforma a dica em True o que significa que a dica foi usada
            time.sleep(1)
            continue #Volta ao inicio do loop

        #Caso a pessoa escreva mais que 1 letra por palpite
        comprimento_palpite = len(palpite) #Calcula o comprimento do palpite
        if comprimento_palpite != 1 and palpite != "dica": #Se o comprimento do palpite for diferente que 1 e diferente que "dica" então mostra o print abaixo
            print("Só é permitido 1 letra por tentativa, tente novamente.")
            time.sleep(1) #Serve para dar uma pausa de 1 segundo
            continue

        if palpite in lista_acertos or palpite in lista_erros: #Se o palpite já estiver na lista_acertos e na lista_erros então mostra o print abaixo
            print("Tu já tentaste essa letra, escolha uma diferente!")
            time.sleep(1)
            continue
            
        elif palpite in choisen_animal: #Se o palpite estiver dentro do choisen_animal entra na condição
            for i in range(len(choisen_animal)): #Fazer um loop com um intervalo do comprimento do choisen_animal
                if choisen_animal[i] == palpite: #Verifica se a letra do indice é igual ao palpite
                    hidden_name[i] = palpite #Substitui a letra a posição do indice do hidden_name pelo palpite
            if palpite not in lista_acertos: #Verifica se o palpite não está na lista_acertos
                lista_acertos.append(palpite) #Adiciona o palpite na lista
                acertos += 1 #Atualiza o contador
        else: #Só entra nesta condição se o user errar a letra
            erros += 1
            lista_erros.append(palpite)
            if erros > 0: #Verifica se a variavel erros é maior que 0
                print(f"Erros: {erros}") #Mostra o contador de erros atual
            time.sleep(1)
    if derrota: #Se a variavel derrota for igual a True então entra nesta condição
        limpar()
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
    else: #Se a variavel derrota se manter false então entra nesta condição
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