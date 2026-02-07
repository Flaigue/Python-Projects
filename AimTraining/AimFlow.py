from tkinter import *
import random
import os

os.system("cls" if os.name == "nt" else "clear")

counter = 0
time = 10
game_started = False

def action(event=None):
    if event is None or event.widget == window:
        with_window = window.winfo_width()
        height_window = window.winfo_height()

        if with_window > 150 and height_window > 150:
            new_x = random.randint(50, with_window - 50)
            new_y= random.randint(50, height_window - 50)
            main_button.place(x=new_x, y=new_y)

def clicking():
    global counter, game_started
    if game_started is not True:
        game_started = True
        update_timer()
    counter += 1
    score.config(text=f"Score: {counter}")
    action()

def update_timer():
    global time
    if time > 0:
        time -= 1
        timer_window.config(text=f"Time: {time}")
        window.after(1000, update_timer)
    else:
        main_button.config(state=DISABLED)
        main_text.config(text="Game Over !", fg="#FF0000")


window = Tk()

window.state("zoomed") #Tamanho da janela
window.title("Flow Aim") #Nome da Janela

app_icon = PhotoImage(file="C:/Users/Leandro/Documents/Coding/My Own Projects/AimTraining/Python.png") #Variavel do icon
window.iconphoto(True,app_icon) #Icon na janela

main_text = Label(window, 
              text="Train you accuracy here",
              font=("Fixedsys", "25"),
              background="black", #cor do fundo da letra
              fg="white" #cor da letra
              )
main_text.pack()

main_button = Button (
    window,
    font=("Comic Sans MS", 5),
    background="white",
    relief="flat",
    highlightthickness=0,
    padx=15,
    pady=10,
    command=clicking
    )
main_button.place(x=400, y=300)

score = Label(window,
              text="Score: 0",
              font=("MS Serif","15"),
              fg="#ffffff",
              bg="#000000"
              )
score.place(relx=0.99, rely=0.01, anchor=NE)

timer_window = Label(window,
             text="Time: 10sec",
             font=("MS Serif","15"),
             fg="#ffffff",
             bg="#000000"
             )
timer_window.place(relx=0.99, rely=0.05,anchor=NE)

window.bind("<Configure>", action)

window.config(background="Black")

window.mainloop() #Abre e mantém a janela aberta