import tkinter as tk

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
        if self.name != '' and self.lang != "" :
            self.saved()
        self.destroy()

    def saved(self):
        user= []
        user.append(self.name)
        user.append(self.lang)
        return user
