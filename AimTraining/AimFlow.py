from tkinter import *
import random
import os

# Limpa o terminal ao iniciar para uma execução mais limpa
os.system("cls" if os.name == "nt" else "clear")

# --- CONFIGURAÇÕES E VARIÁVEIS GLOBAIS ---
counter = 0
time = 10
game_started = False

# --- LÓGICA DAS FUNÇÕES ---

def action(event=None):
    """Controla o posicionamento aleatório do botão alvo."""
    if event is None or event.widget == window:
        with_window = window.winfo_width()
        height_window = window.winfo_height()

        # Garante que o botão não seja gerado fora de janelas muito pequenas
        if with_window > 150 and height_window > 150:
            new_x = random.randint(50, with_window - 50)
            new_y = random.randint(50, height_window - 50)
            main_button.place(x=new_x, y=new_y)

def clicking():
    """Registra o clique, inicia o jogo e atualiza o score."""
    global counter, game_started
    if game_started is not True:
        game_started = True
        update_timer()
    
    counter += 1
    score.config(text=f"Score: {counter}")
    action()

def update_timer():
    """Gerencia a contagem regressiva e o estado de fim de jogo."""
    global time
    if time > 0:
        time -= 1
        timer_window.config(text=f"Time: {time}sec")
        window.after(1000, update_timer)
    else:
        # Finaliza a interação e exibe o menu de Game Over
        main_button.config(state="disabled")
        main_button.place_forget()
        main_text.config(text="Game Over !", fg="#FF0000")
        restart_button.place(relx=0.5, rely=0.60, anchor="center")
        leave_button.place(relx=0.5, rely=0.75, anchor="center")

def reset_game():
    """Restaura as variáveis e a interface para o estado inicial."""
    global counter, time, game_started
    counter = 0
    time = 10
    game_started = False

    score.config(text="Score: 0")
    timer_window.config(text="Time: 10sec")
    main_text.config(text="Train you accuracy here", fg="#ffffff")

    main_button.config(state="normal")
    main_button.place(relx=0.5, rely=0.5, anchor="center")

    restart_button.place_forget()
    leave_button.place_forget()

def leave():
    """Fecha a aplicação."""
    window.destroy()

# --- INTERFACE GRÁFICA (GUI) ---

window = Tk()
window.state("zoomed")
window.title("Flow Aim")
window.config(background="Black")

# --- LÓGICA DINÂMICA PARA O ÍCONE ---
try:
    pasta_projeto = os.path.dirname(__file__)
    caminho_icone = os.path.join(pasta_projeto, "Python.png")
    app_icon = PhotoImage(file=caminho_icone)
    window.iconphoto(True, app_icon)
except Exception as error:
    # Se a imagem falhar, o programa continua mas avisa o erro no terminal
    print(f"Erro em carregar o ícone: {error}")

# Elementos de Texto e Alvos
main_text = Label(window, text="Train you accuracy here", font=("Fixedsys", "25"), background="black", fg="white")
main_text.pack(pady=20)

main_button = Button(window, background="white", relief="flat", highlightthickness=0, padx=15, pady=10, command=clicking)
main_button.place(relx=0.5, rely=0.5, anchor="center")

# Painel de Status (Score e Timer)
score = Label(window, text="Score: 0", font=("MS Serif","15"), fg="#ffffff", bg="#000000")
score.place(relx=0.99, rely=0.01, anchor="ne")

timer_window = Label(window, text="Time: 10sec", font=("MS Serif","15"), fg="#ffffff", bg="#000000")
timer_window.place(relx=0.99, rely=0.05, anchor="ne")

# Botões de Menu (Reiniciar e Sair)
restart_button = Button(window, text="Restart", font=("8514oem", "25"), padx=5, pady=3, bg="#FFFFFF", fg="#000000", command=reset_game)

leave_button = Button(window, text="Leave", font=("8514oem", "25"), padx=3, pady=3, bg="#ffffff", fg="#000000", command=leave)

# --- EVENTOS E EXECUÇÃO ---

# Detecta mudanças na janela para ajustar o botão alvo
window.bind("<Configure>", action)

window.mainloop()
