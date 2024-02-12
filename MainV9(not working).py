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

        self.key_to_bind = "k"
        self.bind(f"<KeyPress-{self.key_to_bind}>", self.page2.show_credits)  # Associe la touche définie par la variable à la fonction show_credits

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

        # ... (autres éléments de l'interface)

        # Changer le keybind
        keybind_label = tk.Label(self, text="Changer le keybind:")
        keybind_label.pack(pady=5)
        keybind_entry = tk.Entry(self)
        keybind_entry.insert(0, app.key_to_bind)  # Affiche la valeur actuelle de la variable key_to_bind
        keybind_entry.pack(pady=5)

        # Boutons pour changer la résolution et le keybind
        button_720p = tk.Button(self, text="Changer en 720p", command=lambda: self.change_resolution("720p"))
        button_720p.pack(pady=5)

        button_1080p = tk.Button(self, text="Changer en 1080p", command=lambda: self.change_resolution("1080p"))
        button_1080p.pack(pady=5)

        button_keybind = tk.Button(self, text="Changer le keybind", command=lambda: self.change_keybind(keybind_entry.get()))
        button_keybind.pack(pady=5)

        button_save = tk.Button(self, text="Sauvegarder", command=lambda: self.save_keybind(keybind_entry))
        button_save.pack(pady=5)

        button_middle = tk.Button(self, text="Retour au Menu", command=self.show_main_menu)
        button_middle.pack(pady=20)

        button_bottom = tk.Button(self, text="Crédits", command=self.show_credits)
        button_bottom.pack(side=tk.BOTTOM, pady=10)

    def show_main_menu(self):
        app.notebook.select(0)  # Sélectionne la page du menu principal

    def show_credits(self, event=None):
        app.notebook.select(2)  # Sélectionne la page des crédits

    def change_resolution(self, new_resolution):
        print(f"Changer la résolution en {new_resolution}")

    def change_keybind(self, new_keybind):
        app.unbind(f"<KeyPress-{app.key_to_bind}>")  # Désassocie l'ancien keybind
        app.key_to_bind = new_keybind
        app.bind(f"<KeyPress-{app.key_to_bind}>", self.show_credits)  # Associe la nouvelle touche à la fonction show_credits

    def save_keybind(self, keybind_entry):
        new_keybind = keybind_entry.get()
        self.change_keybind(new_keybind)

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
