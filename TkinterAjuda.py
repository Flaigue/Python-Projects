"""from tkinter import * para importar a biblioteca Tkinter
window = Tk() Criar a variavel da janela

window.geometry("800x600") Tamanho da janela
window.title("Aiming training") Nome da Janela

app_icon = PhotoImage(file="C:/Users/Leandro/Documents/Coding/My Own Projects/AimTraining/Python.png") #Variavel do icon
window.iconphoto(True,app_icon) #Icon na janela na parte superior esquerdo

photo = PhotoImage(file="Pithon.png")

MainText = Label(window, Label que vai conter tudo do texto

              text="Train you accuracy here",
              font=("Fixedsys", "25", "bold"), Estilo da letra, tamanho e se é bold, italico etc
              fg="white", cor da letra

              background="black", cor do fundo da letra

              relief=raised, Estilo da borda
              bd= 10, tamanho da borda

              pad= 10, alterar o padding, pode usar pady e padx se quiser especificar
              
              image= photo,
              compound="bottom" Se eu quiser manter o texto com a imagem, bottom para a imagem ficar embaixo
              )
MainText.pack() Centraliza o texto

window.config(background="Black") Altera o fundo da janela

window.mainloop() #Abre e mantém a janela aberta"""