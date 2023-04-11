import tkinter as tk
from PIL import Image, ImageTk

# OBS : trocar local das imagens de acordo com a necessidade

class ConfigWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Configurações")

        # Cria o widget Label
        self.label_name = tk.Label(self, text="Name:")
        self.label_name.grid(row=0, column=0)

        # Cria o widget Entry
        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row=0, column=1)
        
        # Cria o widget Label
        self.label_lang = tk.Label(self, text="Language:")
        self.label_lang.grid(row=0, column=2)

        # Cria o widget Entry
        self.entry_lang = tk.Entry(self)
        self.entry_lang.grid(row=0, column=3)

        # Cria o botão Salvar
        self.button_save = tk.Button(self, text="Salvar", command=self.save_config)
        self.button_save.grid(row=1, column=0)

        # Cria o botão Cancelar
        self.button_cancel = tk.Button(self, text="Cancelar", command=self.destroy)
        self.button_cancel.grid(row=1, column=1)

    def save_config(self):
        # Salva o nome e linguagem 
        self.name = self.entry_name.get()
        self.lang = self.entry_lang.get()
        self.destroy()

    def saved(self):
        user= []
        user.append(self.name , self.lang)
        return user



class Screen(tk.Tk):
    
    def __init__(self):
        super().__init__()    
        self.title("DEVA")
    # fundo da tela
        self.screen_b = tk.Frame(self, bg='black')
        self.screen_b.pack(padx=2,pady=2)
 
        # Carregando a imagem
        self.image = Image.open("C:/Users/USUARIO/Documents/PROGRAMAÇÃO/CODIGOS2/DEVA/deva_assistent.jpg")
        self.image = self.image.resize((200, 200)) 
        self.image = ImageTk.PhotoImage(self.image)

        # icone
        self.iconbitmap("C:/Users/USUARIO/Documents/PROGRAMAÇÃO/CODIGOS2/DEVA/deva_assistent.jpg")
        
        # Adicionando a image à janela
        self.label_image = tk.Label(self.screen_b, image=self.image , background="black")
        self.label_image.grid()

        # Criando um botão e posicionando-o sobre a imagem 
        self.image_bt = tk.PhotoImage(file="C:/Users/USUARIO/Documents/PROGRAMAÇÃO/CODIGOS2/DEVA/settings.png")
        self.button = tk.Button(self.screen_b, image=self.image_bt , command=self.open_config() , width=10 , height=10)
        self.button.place(x=10, y=10, anchor="nw")
        
        
    # Adiciona o texto à janela
        self.label_text = tk.Label(self.screen_b, text=self.text() ,bd=12,bg='black',fg='white' )
        self.label_text.grid()

        # Execute a janela
        self.screen_b.mainloop()

    # adiciona text a tela 
    def text(self , text= "Hello !"):
        return text.upper()
    
    # abrir a janela de configuração apos apertar o botão
    def open_config(self):
        config_window = ConfigWindow()
        config_window.grab_set()
        config_window.wait_window()
        self.dados = config_window.saved()  
        
    def information(self) :
        return self.dados 


    
    
    
    
    
    
    
    
    
    