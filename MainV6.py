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

        # Volume de la musique
        music_label = tk.Label(self, text="Volume de la musique:")
        music_label.pack(pady=5)
        music_scale = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        music_scale.pack(pady=5)

        # Bruits d'interaction
        sound_label = tk.Label(self, text="Bruits d'interaction:")
        sound_label.pack(pady=5)
        sound_scale = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        sound_scale.pack(pady=5)

        # Résolution
        resolution_label = tk.Label(self, text="Résolution:")
        resolution_label.pack(pady=5)
        resolution_entry = tk.Entry(self)
        resolution_entry.pack(pady=5)

        # Mode d'écran
        fullscreen_var = tk.BooleanVar()
        fullscreen_checkbox = tk.Checkbutton(self, text="Plein écran", variable=fullscreen_var)
        fullscreen_checkbox.pack(pady=5)

        # Boutons pour changer la résolution
        button_720p = tk.Button(self, text="Changer en 720p", command=lambda: self.change_resolution("720p"))
        button_720p.pack(pady=5)

        button_1080p = tk.Button(self, text="Changer en 1080p", command=lambda: self.change_resolution("1080p"))
        button_1080p.pack(pady=5)

        button_middle = tk.Button(self, text="Retour au Menu", command=self.show_main_menu)
        button_middle.pack(pady=20)

        button_bottom = tk.Button(self, text="Crédits", command=self.show_credits)
        button_bottom.pack(side=tk.BOTTOM, pady=10)

    def show_main_menu(self):
        app.notebook.select(0)  # Sélectionne la page du menu principal

    def show_credits(self, event=None):  # L'événement est nécessaire pour être compatible avec le keybind
        app.notebook.select(2)  # Sélectionne la page des crédits

    def change_resolution(self, new_resolution):
        # Vous pouvez mettre ici le code pour appliquer la nouvelle résolution
        print(f"Changer la résolution en {new_resolution}")

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
    app.bind("<KeyPress-k>", app.page2.show_credits)  # Associe la touche "k" à la fonction show_credits de la page2
    app.mainloop()
