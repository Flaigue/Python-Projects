import time
import random
print("-"*50)
print("Bem vindo ao programa Quente e Frio")
print("-"*50)
print("Regras: ")
print("-"*50)
print("O sistema mais escolher 1 numero entre 0 a 100, o \nvalor\
 vai ser escolhido de forma aleatoria e tu \nteras que tentar acertar\
, o programa ira dar a dica \nse o valor está ´Muito quente´, ´Quente´,\
 ´Morno´, \n´Frio´ ou ´Muito frio´ ou ´Gelado´.")
print("-"*50)

pontos = 0 #Numero de pontos
tentativas = 0 #Numero de tentativas

def filtro():
    entrada = input(": ")  # lê como string
    if entrada.isdigit():
        valorfiltrado = int(entrada)
        if 0 <= valorfiltrado <= 100:
            return valorfiltrado
        else:
            print("O input tem que ser no intervalo de 0 a 100.")
            return None
    else:
        print("Input inválido, o input tem que ser um valor inteiro.")
        return None

def saida():  # Função para sair
    while True:
        resposta = input("Quer tentar denovo? ").lower().strip()
        if resposta in ["sim", "s", "claro", "obvio", "claramente"]:
            print("-"*50)
            return True   # continua o jogo
        elif resposta in ["não", "nao", "n", "nop", "nepia"]:
            print("Jogo encerrado.")
            exit()        # sai do programa
        else:
            print("Input inválido, tente novamente.")

while True:
    num = random.randint(1, 100)

    print(f"num sorteado {num}")
    valor = filtro()

    if valor is None:
        continue

    if num == valor: #Em caso de acertar
        if tentativas == 0: #Se for a primeira tentativa
            print("-"*50)
            print("Parabéns, você acertou na primeira tentativa")
        elif tentativas > 0: #Se acertar mas não na primeira tentativa
            print("-"*50)
            print(f"Parabéns, você acertou")
            print(f"Tentativas feitas: {tentativas}")

    elif num != valor:
        dif = abs(num - valor) #Cacular a diferença entre o numero sorteado e numero do user
        tentativas += 1
        print("-"*50)
        print(f"Tentativas: {tentativas}")

        if dif <= 5:
            print("Dica: Muito Quente")
        elif dif <= 10:
            print("Dica: Quente")
        elif dif <= 15:
            print("Dica: Morno")
        elif dif <= 20:
            print("Dica: Frio")
        elif dif <= 25:
            print("Dica: Muito Frio")
        else:
            print("Dica: Gelado")
        print(f"Valor errado, tente novamente")
        print("-"*50)
    if num == valor:
        saida()
    
    #Caso se o user errar 5 vezes
    if tentativas == 5:
        print("-"*50)
        print("Game Over.")
        saida()