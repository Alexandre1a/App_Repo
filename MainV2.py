import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Menu de Jeu Vidéo")
        self.geometry("400x300")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.page1 = MainMenu(self.notebook)
        self.page2 = SettingsPage(self.notebook)
        self.page3 = CreditsPage(self.notebook)

        self.notebook.add(self.page1, text="Accueil")
        self.notebook.add(self.page2, text="Paramètres")
        self.notebook.add(self.page3, text="Crédits")

class MainMenu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        label = tk.Label(self, text="Bienvenue dans le Menu Principal")
        label.pack(padx=10, pady=10)

        button_middle = tk.Button(self, text="Jouer", command=self.play_game)
        button_middle.pack(pady=20)

        button_bottom = tk.Button(self, text="Paramètres", command=self.show_settings)
        button_bottom.pack(side=tk.BOTTOM, pady=10)

    def play_game(self):
        print("Lancer le jeu !")

    def show_settings(self):
        app.notebook.select(1)  # Sélectionne la page des paramètres

class SettingsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        label = tk.Label(self, text="Page des Paramètres")
        label.pack(padx=10, pady=10)

        button_middle = tk.Button(self, text="Retour au Menu", command=self.show_main_menu)
        button_middle.pack(pady=20)

        button_bottom = tk.Button(self, text="Crédits", command=self.show_credits)
        button_bottom.pack(side=tk.BOTTOM, pady=10)

    def show_main_menu(self):
        app.notebook.select(0)  # Sélectionne la page du menu principal

    def show_credits(self):
        app.notebook.select(2)  # Sélectionne la page des crédits

class CreditsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        label = tk.Label(self, text="Page des Crédits")
        label.pack(padx=10, pady=10)

        button_middle = tk.Button(self, text="Retour au Menu", command=self.show_main_menu)
        button_middle.pack(pady=20)

        button_bottom = tk.Button(self, text="Quitter", command=self.quit_application)
        button_bottom.pack(side=tk.BOTTOM, pady=10)

    def show_main_menu(self):
        app.notebook.select(0)  # Sélectionne la page du menu principal

    def quit_application(self):
        app.destroy()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
