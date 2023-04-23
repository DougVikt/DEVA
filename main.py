import tkinter as tk
from PIL import Image, ImageTk
import config as cf

# OBS : trocar local das imagens de acordo com a necessidade

 # adiciona text a tela 
def text(text= "Hello !"):
    
    label_text = tk.Label(screen_b, text=text ,bd=12,bg='black',fg='white' )
    label_text.grid()


# abrir a janela de configuração apos apertar o botão
def open_config():
    
    config_window = cf.ConfigWindow()
    config_window.grab_set()
    config_window.wait_window()
    if hasattr(config_window , 'saved')  :
        dados = config_window.saved()  
    
def information() :
    return dados 

if __name__ == '__main__' :
    
    screen = tk.Tk()
    screen.title("DEVA")
# fundo da tela
    screen_b = tk.Frame(screen, bg='black')
    screen_b.pack(padx=2,pady=2)

    # Carregando a imagem
    image = Image.open("C:/Users/USUARIO/Documents/PROGRAMAÇÃO/CODIGOS2/DEVA/deva_assistent.jpg")
    image = image.resize((200, 200)) 
    image = ImageTk.PhotoImage(image)

    # icone
    screen.iconbitmap("C:/Users/USUARIO/Documents/PROGRAMAÇÃO/CODIGOS2/DEVA/deva_assistent.jpg")
    
    # Adicionando a image à janela
    label_image = tk.Label(screen_b, image=image , background="black")
    label_image.grid()

    # Criando um botão e posicionando-o sobre a imagem 
    image_bt = tk.PhotoImage(file="C:/Users/USUARIO/Documents/PROGRAMAÇÃO/CODIGOS2/DEVA/settings.png")
    button = tk.Button(screen_b, image=image_bt , command=open_config , width=10 , height=10)
    button.place(x=10, y=10, anchor="nw")
  
    text()
 # Execute a janela
    screen_b.mainloop()

   


    
    
    
    
    
    
    
    
    
    