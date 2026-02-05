from tkinter import *
import random
import os

os.system("cls" if os.name == "nt" else "clear")

counter = 0

def action(#event=None):
    with_window = window.winfo_width()
    height_window = window.winfo_height()
    
    new_x = random.randint(50, with_window - 50)
    new_y= random.randint(50, height_window - 50)
    mainbutton.place(x=new_x, y=new_y)

def clicking():
    global counter
    counter += 1
    score.config(text=f"Score: {counter}")
    action()

window = Tk()

window.state("zoomed") #Tamanho da janela
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
    command=clicking
    )
mainbutton.place(x=400, y=300)

score = Label(window,
              text="Score: 0",
              font=("MS Serif","15"),
              fg="#ffffff",
              bg="#000000"
              )
score.place(relx=0.99, rely=0.01, anchor=NE )

#window.bind("<Configure>", action)

window.config(background="Black")

window.mainloop() #Abre e mantém a janela aberta