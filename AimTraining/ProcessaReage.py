from tkinter import *
import random
import os

os.system("cls" if os.name == "nt" else "clear")

def move_button():
    new_x = random.randint(30, 770)
    new_y= random.randint(60, 580)
    mainbutton.place(x=new_x, y=new_y)

window = Tk()

window.geometry("800x600") #Tamanho da janela
window.title("Flow Aim") #Nome da Janela

app_icon = PhotoImage(file="C:/Users/Leandro/Documents/Coding/My Own Projects/AimTraining/Python.png") #Variavel do icon
window.iconphoto(True,app_icon) #Icon na janela

MainText = Label(window, 
              text="Train you accuracy here",
              font=("Fixedsys", "25"),
              background="black", #cor do fundo da letra
              fg="white", #cor da letra
              )
MainText.pack()


mainbutton = Button (
    window,
    font=("Comic Sans MS", 5),
    background="white",
    relief="flat",
    highlightthickness=0,
    padx=15,
    pady=10,
    command=move_button
    )
mainbutton.place(x=400, y=300)

window.config(background="Black")

window.mainloop() #Abre e mantém a janela aberta