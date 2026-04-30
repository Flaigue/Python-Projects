from os import system
system("clear")
lista_nomes = [
    "Ana", "Rui", "Luís", "Vera", "João", 
    "Tiago", "Maria", "Diogo", "Sandro", "Afonso", 
    "Duarte", "Beatriz", "Rodrigo", "Mariana", "Ricardo", 
    "Francisco", "Margarida", "Guilherme", "Alexandra", "Frederico"
]
valor = 1
lista_filtrada = []
for n in lista_nomes:
    if len(n) >= valor:
        lista_filtrada.append(n)
        valor += 1
    print(lista_filtrada)