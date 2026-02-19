import os
import datetime

current_date = datetime.date.today()
current_day = current_date.day
current_month = current_date.month

altura = int(input("=> "))
tronco = " " * (altura - 2)
os.system("clear")

cores = {
    "reset": "\033[0m",
    "amarelo": "\033[38;2;255;255;0m",
    "castanho": "\033[38;2;160;105;40m",
    "cinzento": "\033[48;2;75;75;75m",
    "verde": "\033[38;2;0;255;0m"
}

for andar in range (1, altura + 1):
    espacos = " " * (altura - andar)
      
    if andar == 1:
        cor_escolhida = cores["amarelo"]
    else:
        cor_escolhida = cores["verde"]
    print(f"{espacos}{cor_escolhida}{'*' * (2 * andar - 1)}{cores['reset']}")

for i in range(2):
    print(f"{tronco}{cores['castanho']}{'|'*3}{cores['reset']}")
print(f"{' '*(altura - 3)}{cores['cinzento']}{' '*5}{cores['reset']}")

print("")
if current_month == 12:
    if current_day == 24:
        print("Congratulations! It's Christmas Eve, and tomorrow will be an amazing day.")
    elif current_day == 25:
        print("Congratulations! Today is the most festive day of the year — celebrate and enjoy every moment.")
    else:
        print("We're in the Christmas season, but Christmas hasn't arrived yet.")
else:
    print("Unfortunately, you're not in the festive month of December, but don't worry — it will be here before you know it.")

sair = str(input(""))
exit()
