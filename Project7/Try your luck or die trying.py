import random

print("Bem-vindo ao programa 'Escolhe e vence ou perde tentando'")

numeros_disponiveis = list(range(10))
pontos = 0
primeira_tentativa = True

while True:

    if len(numeros_disponiveis) == 2:
        print("\n⚡ Última rodada decisiva!")
        print("Restam apenas 2 números:", numeros_disponiveis)

        num_escolhido = random.choice(numeros_disponiveis)
        tentativa = int(input("Tente adivinhar: "))

        if tentativa == num_escolhido:
            pontos += 1
            print("🥳 Você acertou! Pontuação final:", pontos)
        else:
            print("😞 Você errou! Pontuação final:", pontos)
        break

    num_escolhido = random.choice(numeros_disponiveis)
    print("\nO programa escolheu um número secreto entre 0 e 9 (excluindo já removidos).")
    tentativa = int(input("Tente adivinhar: "))

    if tentativa == num_escolhido:
        pontos += 1
        print("🥳 Você acertou!!!")
        print("Número escolhido era:", num_escolhido)
        numeros_disponiveis.remove(num_escolhido)
        print("Números restantes:", numeros_disponiveis)
        primeira_tentativa = False
    else:
        print("😞 Você errou!")
        print("Número escolhido era:", num_escolhido)

        if primeira_tentativa:
            pontos = 0
            resposta = input("Quer recomeçar? (s/n): ").lower()
            if resposta == "s":
                numeros_disponiveis = list(range(10))
                pontos = 0
                primeira_tentativa = True
                continue
            else:
                print("Fim do jogo. Pontuação final:", pontos)
                break
        else:
            print("Fim do jogo. Pontuação final:", pontos)
            break
