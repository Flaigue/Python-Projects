from tkinter import *
import random
import os

# Clears the terminal at startup for a cleaner execution
os.system("cls" if os.name == "nt" else "clear")

# --- SETTINGS AND GLOBAL VARIABLES ---
score_counter = 0
time_remaining = 10
game_started = False

# --- FUNCTION LOGIC ---

def reposition_target(event=None):
    """Handles the random positioning of the target button."""
    if event is None or event.widget == window:
        window_width = window.winfo_width()
        window_height = window.winfo_height()

        # Ensures the button isn't generated outside if the window is too small
        if window_width > 150 and window_height > 150:
            new_x = random.randint(50, window_width - 50)
            new_y = random.randint(50, window_height - 50)
            target_button.place(x=new_x, y=new_y)

def handle_click():
    """Registers the click, starts the game, and updates the score."""
    global score_counter, game_started
    if not game_started:
        game_started = True
        update_timer()
    
    score_counter += 1
    score_label.config(text=f"Score: {score_counter}")
    reposition_target()

def update_timer():
    """Manages the countdown and the game-over state."""
    global time_remaining
    if time_remaining > 0:
        time_remaining -= 1
        timer_label.config(text=f"Time: {time_remaining}sec")
        window.after(1000, update_timer)
    else:
        # Finalizes interactions and displays the Game Over menu
        target_button.config(state="disabled")
        target_button.place_forget()
        instruction_text.config(text="Game Over!", fg="#FF0000")
        restart_button.place(relx=0.5, rely=0.60, anchor="center")
        exit_button.place(relx=0.5, rely=0.75, anchor="center")

def reset_game():
    """Restores variables and UI to their initial state."""
    global score_counter, time_remaining, game_started
    score_counter = 0
    time_remaining = 10
    game_started = False

    score_label.config(text="Score: 0")
    timer_label.config(text="Time: 10sec")
    instruction_text.config(text="Train your accuracy here", fg="#ffffff")

    target_button.config(state="normal")
    target_button.place(relx=0.5, rely=0.5, anchor="center")

    restart_button.place_forget()
    exit_button.place_forget()

def exit_application():
    """Closes the application."""
    window.destroy()

# --- GRAPHICAL USER INTERFACE (GUI) ---

window = Tk()

# Compatibility fix for Linux (Mint/Ubuntu) and Windows
try:
    window.state("zoomed")  # Works on Windows
except:
    window.attributes('-zoomed', True)  # Works on Linux
    
window.title("Flow Aim")
window.config(background="Black")

# --- DYNAMIC ICON LOGIC ---
try:
    project_dir = os.path.dirname(__file__)
    icon_path = os.path.join(project_dir, "Python.png")
    app_icon = PhotoImage(file=icon_path)
    window.iconphoto(True, app_icon)
except Exception as error:
    print(f"Error loading icon: {error}")

# Font settings (Added fallbacks for better cross-platform support)
main_font = ("Fixedsys", 25, "bold")
ui_font = ("MS Serif", 15)
button_font = ("Courier", 25, "bold") # Changed to Courier for better compatibility

# Text Elements and Targets
instruction_text = Label(window, text="Train your accuracy here", font=main_font, background="black", fg="white")
instruction_text.pack(pady=20)

target_button = Button(window, background="white", relief="flat", highlightthickness=0, padx=15, pady=10, command=handle_click)
target_button.place(relx=0.5, rely=0.5, anchor="center")

# Status Panel (Score and Timer)
score_label = Label(window, text="Score: 0", font=ui_font, fg="#ffffff", bg="#000000")
score_label.place(relx=0.99, rely=0.01, anchor="ne")

timer_label = Label(window, text="Time: 10sec", font=ui_font, fg="#ffffff", bg="#000000")
timer_label.place(relx=0.99, rely=0.05, anchor="ne")

# Menu Buttons (Restart and Exit)
restart_button = Button(window, text="Restart", font=button_font, padx=5, pady=3, bg="#FFFFFF", fg="#000000", command=reset_game)

exit_button = Button(window, text="Leave", font=button_font, padx=3, pady=3, bg="#ffffff", fg="#000000", command=exit_application)

# --- EVENTS AND EXECUTION ---

# Detects window changes to adjust target positioning
window.bind("<Configure>", reposition_target)

window.mainloop()
