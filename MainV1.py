import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Application avec plusieurs pages")

        self.geometry("400x300")

        # Création du gestionnaire de pages
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Création de chaque page
        self.page1 = Page1(self.notebook)
        self.page2 = Page2(self.notebook)
        self.page3 = Page3(self.notebook)

        # Ajout des pages au gestionnaire de pages
        self.notebook.add(self.page1, text="Page 1")
        self.notebook.add(self.page2, text="Page 2")
        self.notebook.add(self.page3, text="Page 3")

class Page1(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        label = tk.Label(self, text="Bienvenue sur la Page 1")
        label.pack(padx=10, pady=10)

        # Ajoutez ici les éléments spécifiques à la Page 1

class Page2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        label = tk.Label(self, text="Bienvenue sur la Page 2")
        label.pack(padx=10, pady=10)

        # Ajoutez ici les éléments spécifiques à la Page 2

class Page3(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        label = tk.Label(self, text="Bienvenue sur la Page 3")
        label.pack(padx=10, pady=10)

        # Ajoutez ici les éléments spécifiques à la Page 3

if __name__ == "__main__":
    app = Application()
    app.mainloop()
