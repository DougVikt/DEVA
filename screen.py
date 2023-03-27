import tkinter as tk
from PIL import Image, ImageTk

# OBS : trocar local das imagens de acordo com a necessidade

def screen(text = str):
    # janela
    screen = tk.Tk()
    screen.title("DEVA")
    # janela com fundo preto
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
    label_image.pack()

    # Adicion o texto à janela
    label_text = tk.Label(screen_b, text=text.upper(),bd=12,bg='black',fg='white' )
    label_text.pack()


    # Execute a janela
    screen_b.mainloop()

