import os
import datetime

# Get current date info
current_date = datetime.date.today()
current_day = current_date.day
current_month = current_date.month

# User input for tree height
height = int(input("Enter tree height => "))
trunk_spacing = " " * (height - 2)
os.system("cls" if os.name == "nt" else "clear")

# Color dictionary using ANSI RGB escape sequences
colors = {
    "reset": "\033[0m",
    "yellow": "\033[38;2;255;255;0m",
    "brown": "\033[38;2;160;105;40m",
    "grey": "\033[48;2;75;75;75m",
    "green": "\033[38;2;0;255;0m"
}

# Drawing the tree leaves (canopy)
for level in range(1, height + 1):
    spaces = " " * (height - level)
    
    # The first level (top) is the star (yellow), others are green
    if level == 1:
        chosen_color = colors["yellow"]
    else:
        chosen_color = colors["green"]
    
    print(f"{spaces}{chosen_color}{'*' * (2 * level - 1)}{colors['reset']}")

# Drawing the trunk
for _ in range(2):
    print(f"{trunk_spacing}{colors['brown']}{'|'*3}{colors['reset']}")

# Drawing the base (soil/support)
print(f"{' '*(height - 3)}{colors['grey']}{' '*5}{colors['reset']}")

print("")

# Seasonal messaging logic
if current_month == 12:
    if current_day == 24:
        print("Congratulations! It's Christmas Eve, and tomorrow will be an amazing day.")
    elif current_day == 25:
        print("Congratulations! Today is the most festive day of the year — celebrate and enjoy every moment.")
    else:
        print("We're in the Christmas season, but Christmas hasn't arrived yet.")
else:
    print("Unfortunately, you're not in the festive month of December, but don't worry — it will be here before you know it.")

# Keep terminal open
exit_prompt = str(input("\nPress Enter to exit..."))
exit()
