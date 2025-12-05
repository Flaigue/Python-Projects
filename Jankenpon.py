import random
import time
import os
os.system("clear") #Limpar o que estiver anteriormente no terminal
texto = " [ 1 ] = Pedra [ 2 ] = Papel [ 3 ] = Tesoura "
print("=" * len(texto)) #Fazer as barras de espaçamento entre o conteudo do comprimento do menu
print(texto) #Output do Menu
print("=" * len(texto))

user = int(input("-> ")) #Input do user
if user not in (1, 2, 3): #Encerrar o software se for introduzido qualquer coisa que não seja 1, 2 ou 3
   print("Input invalido")
   exit()
print("=" * len(texto))

time.sleep(0.5) #Output com timing do "Pedra, Papel ou Tesoura !!!" 
print("Pedra")
time.sleep(0.5)
print("Papel")
time.sleep(0.5)
print("Tesoura !!!")
print("=" * len(texto))

lista = [1, 2, 3] #Lista para armazenar as 3 opções possiveis
machine = random.choice(lista) #A maquina escolher uma opção entre 1 a 3 na lista
option = { #Dicionario para armazenar os valores e os seus correspondentes
   1: "Pedra",
   2: "Papel",
   3: "Tesoura"
}

#Se a escolha do user e da machine for empate
if user == 1 and machine == 1 or \
   user == 2 and machine == 2 or \
   user == 3 and machine == 3:
   print("Empate !!!")

#Se o user ganhar da machine
elif user == 1 and machine == 3 or \
    user == 2 and machine == 1 or \
    user == 3 and machine == 2:
   print("Vitoria !!!")
   print(f"user = {user} '{option[user]}'\nmachine = {machine} '{option[machine]}'")

#Se o user perder da machine
elif user == 1 and machine == 2 or \
    user == 2 and machine == 3 or \
    user == 3 and machine == 1:
   print("Derrota !!!")
   print(f"user = {user} '{option[user]}'\nmachine = {machine} '{option[machine]}'")
   #Print realizado para output da escolha do user e da machine em valo e mostrar a sua string associada

#Software criado em 05/12/2025