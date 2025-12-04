import random
import time

print("Bem vindo/a ao programa ´TriForce-Battle´, este jogo é baseado no jogo clássico: Pedra, Papel e Tesoura.")
print("Regras Básicas: Pedra vence Tesoura\nPapel vence Pedra\nTesoura vence Papel")
print("Os únicos inputs válidos são: Papel, Pedra, Tesoura")
print("Qualquer outro input não vai funcionar corretamente, verifique antes de dar ENTER.")
print("Cada jogo completo vai até 5 rondas, se quiser jogar mais vezes o score reinicia.")

# confirmar se o user quer comecar o jogo
escolha = input("Você está pronto? (sim = confirmar, não ou qualquer outra coisa = negar) ").lower()
if escolha != "sim":
    print("Ok, encerrando o jogo.")
    exit()

# Contadores do jogo
vitorias = 0
derrotas = 0
empates = 0
rounds = 0

# Enquanto os rouds for menor que 5
while rounds < 5:
    user = input("(user) -> ").lower()
    time.sleep(0.5)
    machine = random.choice(["pedra", "papel", "tesoura"])
    print(f"(machine) -> {machine}")

    # Em caso de Empate
    if user == machine:
        empates += 1
        print(f"Empates: {empates}")
        if empates == 5:
            print("Não existe vencedor, foram 5 empates seguidos!")
            break

    # Vitória
    elif (user == "pedra" and machine == "tesoura") or \
         (user == "papel" and machine == "pedra") or \
         (user == "tesoura" and machine == "papel"):
        vitorias += 1
        print(f"Vitórias: {vitorias}")

    # Derrota
    elif user in ["pedra", "papel", "tesoura"]:
        derrotas += 1
        print(f"Derrotas: {derrotas}")

    else:
        print("Input inválido.")
        continue  # não conta como ronda

    rounds += 1  # só conta se jogada foi válida

# Resumo final (se não terminou por 5 empates)
if empates < 5:
    print("\nResumo Final:")
    print(f"Vitórias: {vitorias}")
    print(f"Derrotas: {derrotas}")
    print(f"Empates: {empates}")

    if vitorias > derrotas:
        print("Resultado: Você venceu!")
    elif derrotas > vitorias:
        print("Resultado: Você perdeu!")
    else:
        print("Resultado: Empate geral.")
