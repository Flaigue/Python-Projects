# Importa o módulo 'os', que fornece ferramentas para interagir com o Sistema Operativo
import os
from time import sleep
# Usa o atalho '~' para encontrar o caminho da pasta pessoal do utilizador atual (ex: /home/leandro)
# Isso garante que o programa funcione em qualquer computador, não apenas no teu
home = os.path.expanduser("~")

# Cria o caminho completo onde a pasta deve estar, juntando a Home + Documents + User_Data
# O 'join' coloca as barras '/' ou '\' automaticamente dependendo se é Linux ou Windows
caminho_final = os.path.join(home, "Documents", "User_Data")

# Verifica se o caminho definido acima (a pasta) NÃO existe no disco rígido
if not os.path.exists(caminho_final):
    # Se não existir, o comando 'mkdir' cria a pasta fisicamente no destino
    os.mkdir(caminho_final)
    print("Pasta criada com sucesso.")

# Define o caminho completo do ficheiro de texto dentro da pasta que acabámos de garantir que existe
ficheiro = os.path.join(caminho_final, "usuarios.txt")

def credencials():
    name = input("Name: ")
    password = input("Password: ")
    return name, password

def wait():
    sleep(0.5)
    print(".", end="")
    sleep(0.5)
    print(".", end="")
    sleep(0.5)
    print(".")
    
while True:
    # Executa um comando no terminal, 'clear' limpa o ecrã para o programa começar limpo
    os.system("clear")

    print("="*10,"Home Page","="*10)
    print("""1 - Register user
2 - Login User
3 - Leave/Exit program""")
    print("="*31)

    option = str(input(": ")).lower()
    print("="*31)

    if option in ["1", "register", "registrar", "registro", "r"]:
        print("Inicializando registro", end="")
        wait()
        nome, senha = credencials()

        with open(ficheiro, "a") as f:
            f.write(f"{nome},{senha}\n")
        print("Registro realizado com sucesso.")
        sleep(1)
        
    elif option in ["2", "login", "logar", "l"]:
        print("Inicializando login", end="")
        wait()
        l_nome, l_senha = credencials()
        login_sucesso = False
        if os.path.exists(ficheiro):
            with open(ficheiro, "r") as f:
                for linha in f:
                    dados = linha.strip().split(",")
                    if len(dados) == 2:
                        if l_nome == dados[0] and l_senha == dados[1]:
                            login_sucesso = True 
                            break
        if login_sucesso == True:
            print(f"Bem vindo user: {l_nome}.")
            sleep(1)
            break
        else:
            print("Credenciais incorretas, tente novamente")

    elif option in ["3", "leave", "exit", "quit", "sair"]:
        print("Encerrando", end="")
        wait()
        break

""" Coisas a melhorar:
Qualquer coisa que não estiver em nenhuma das opções mostrar Input invalido, tente novamente
Se colocar a senha ou nome errado mostrar credenciais incorretas, porque não está a aparecer
Adicionar a função de recuperar senha, para verificar a autenticidade, perguntar o nome, se o nome
bater o utilizador pode criar uma nova senha e a senha antiga vai ser substituida pela nova"""