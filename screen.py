import tkinter as tk
from PIL import Image, ImageTk

# janela
screen = tk.Tk()
screen.title("== DEVA ==")

# Carregando a imagem
image = Image.open("C:/Users/USUARIO/Documents/PROGRAMAÇÃO/CODIGOS2/DEVA/deva_assistent.jpg")
image = image.resize((400, 400)) 
image = ImageTk.PhotoImage(image)

# icone
screen.iconbitmap("C:/Users/USUARIO/Documents/PROGRAMAÇÃO/CODIGOS2/DEVA/deva_assistent.jpg")

# Crie um frame com uma borda personalizada
frame = tk.Frame(screen, bd=2, relief=tk.SOLID)
frame.pack()

# Adicionando a image à janela
label_image = tk.Label(screen, image=image)
label_image.pack()

# Adicion o texto à janela
text = "Este é um exemplo de texto."
label_text = tk.Label(screen, text=text,bd=8,)
label_text.pack()


# Execute a janela
screen.mainloop()
