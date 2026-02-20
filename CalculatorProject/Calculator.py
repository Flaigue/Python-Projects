print("Caculadora Simples")
print("-"*50)
print("Funções disponiveis: ")
print("+ = somar")
print("- = subtrair")
print("* = multiplicar")
print("/ = dividir")

def somar(var1, var2):
    return var1 + var2

def subtrair(var1, var2):
    return var1 - var2

def multiplicar(var1, var2):
    return var1 * var2

def dividir(var1, var2):
    return var1 / var2

while True:
    try:
        var1 = float(input("- "))
    except ValueError:
        print("Input Invalido")
        continue
    op = input("> ").strip()
    if op not in ("+", "-", "*", "/"):
        print("Input Invalido")
        continue
    try:
        var2 = float(input("- "))
    except ValueError:
        print("Input Invalido")
        continue
    if op == "+":
        print(somar(var1, var2))
    elif op == "-":
        print(subtrair(var1, var2))
    elif op == "*":
        print(multiplicar(var1, var2))
    elif op == "/":
        if var2 == 0:
            print("Erro: divisão por zero")
            continue
        print(dividir(var1, var2))
    saida = input("-> ").strip().lower()
    if saida in ("s", "sim", "quit", "leave", "sair"):
        break