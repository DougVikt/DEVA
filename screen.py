import tkinter as tk
from PIL import Image, ImageTk

# OBS : trocar local das imagens de acordo com a necessidade

class ConfigWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Configurações")

        # Cria o widget Label
        self.label_name = tk.Label(self, text="Nome:")
        self.label_name.grid(row=0, column=0)

        # Cria o widget Entry
        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row=0, column=1)

        # Cria o botão Salvar
        self.button_save = tk.Button(self, text="Salvar", command=self.save_config)
        self.button_save.grid(row=1, column=0)

        # Cria o botão Cancelar
        self.button_cancel = tk.Button(self, text="Cancelar", command=self.destroy)
        self.button_cancel.grid(row=1, column=1)

    def save_config(self):
        # Salva o nome digitado pelo usuário na variável name
        self.parent.name = self.entry_name.get()
        self.destroy()





def screen(text = str):
    
    # janela
    screen = tk.Tk()
    screen.title("DEVA")
    # janela com fundo preto
    screen_b = tk.Frame(screen, bg='black')
    screen_b.pack(padx=2,pady=2)

    def open_config():
        config_window = ConfigWindow(parent=screen)
        config_window.grab_set()


    # Carregando a imagem
    image = Image.open("C:/Users/USUARIO/Documents/PROGRAMAÇÃO/CODIGOS2/DEVA/deva_assistent.jpg")
    image = image.resize((200, 200)) 
    image = ImageTk.PhotoImage(image)

    # icone
    screen.iconbitmap("C:/Users/USUARIO/Documents/PROGRAMAÇÃO/CODIGOS2/DEVA/deva_assistent.jpg")
    
    # Adicionando a image à janela
    label_image = tk.Label(screen_b, image=image , background="black")
    label_image.pack()

    # Criando um botão e posicionando-o sobre a imagem 
    image_bt = tk.PhotoImage(file="C:/Users/USUARIO/Documents/PROGRAMAÇÃO/CODIGOS2/DEVA/settings.png")
    button = tk.Button(screen_b, image=image_bt , command=open_config , width=10 , height=10)
    button.place(x=10, y=10, anchor="nw")
    button

    # Adicion o texto à janela
    label_text = tk.Label(screen_b, text=text.upper(),bd=12,bg='black',fg='white' )
    label_text.pack()


    # Execute a janela
    screen_b.mainloop()