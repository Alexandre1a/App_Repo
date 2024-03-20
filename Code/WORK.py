import tkinter as tk
from tkinter import ttk
from Update import * # Pour importer la fonction de MAJ. ATTENTION : Si importé tel quel, lancera le processus de vérification JSON automatiquement au démarage !
from lib im

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Alexandre_1a's LAUNCHER") # Définit la taille et le nom de l'app
        self.geometry("600x500")
        self.resizable(width=0,height=0) # size change Not allowed 
        self.configure(bg='red')
        self.geometry("400x500"

        self.notebook = ttk.Notebook(self) # Permet de définir le fait qu'il y ait des onglets
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.page1 = MainMenu(self.notebook)
        self.page2 = SettingsPage(self.notebook, self)  # Passe l'instance de l'application à la page2
        self.page3 = UpdatePage(self.notebook)
        self.page4 = AboutPage(self.notebook)

        self.notebook.add(self.page1, text="Accueil") # Permet de donner des noms aux onglets
        self.notebook.add(self.page2, text="Paramètres")
        self.notebook.add(self.page3, text="Updates")
        self.notebook.add(self.page4, text="About")


    if manifest=="=" :
        print("Update Available")
        popupmsg("A new update is available, go to the update page to get the new version !")
'''
        self.key_to_bind = "u" # Important : permet de changer le keybind par défaut
        self.bind(f"<KeyPress-{self.key_to_bind}>", self.page2.show_updates)  # Associe la touche définie par la variable à la fonction show_credits
'''
class MainMenu(tk.Frame): # Affiche le menu principal
    def __init__(self, parent):
        super().__init__(parent)


        label = tk.Label(self, text="Bienvenue Sur Le Menu Principal")
        label.pack(padx=10, pady=10)

        button_middle = tk.Button(self, text="Test !", command=self.play_game)
        button_middle.pack(side=tk.TOP, pady=20)

        button_bottom = tk.Button(self, text="Quitter", command=self.quit_application) # Permet de faire un boutton quitter ( à incorporer partout !)
        button_bottom.pack(side=tk.BOTTOM, pady=10)
        label = tk.Label(self, text="Bienvenue dans le Menu Principal")
        label.pack(padx=10, pady=10)

        button_middle = tk.Button(self, text="Test !", command=self.play_game)
        button_middle.pack(pady=20)

        button_bottom = tk.Button(self, text="Paramètres", command=self.show_settings)
        button_bottom.pack(side=tk.BOTTOM, pady=10)

    def quit_application(self):
        app.destroy()
        print("App Quitté")

    def play_game(self):
        print("Test Is OK")
    def play_game(self):
        print("Test Triggered sucessfully !")

    def show_settings(self): # Sélectionne la page des paramètres
        app.notebook.select(1)
        print("Paramètres Affichés")  

class SettingsPage(tk.Frame):
    def __init__(self, parent, app_instance):
        super().__init__(parent)

        self.app = app_instance  # Stocke l'instance de l'application pour accéder à ses variables

        label = tk.Label(self, text="Paramètres")
        label.pack(padx=10, pady=10)

        # ... (autres éléments de l'interface)

        '''# Changer le keybind
        keybind_label = tk.Label(self, text="Changer le keybind:")
        keybind_label.pack(pady=5)
        keybind_entry = tk.Entry(self)
        keybind_entry.insert(0, self.app.key_to_bind if hasattr(self.app, 'key_to_bind') else "")  # Affiche la valeur actuelle de la variable key_to_bind
        keybind_entry.pack(pady=5)'''

        # Boutons pour changer la résolution et le keybind

        button_400 = tk.Button(self, text="Passer en 400*400", command=self.change_geometry_400)
        button_400.pack(pady=5)

        button_720p = tk.Button(self, text="Changer en 720p", command=lambda: self.change_resolution("720p"))
        button_720p.pack(pady=5)


        button_1080p = tk.Button(self, text="Changer en 1080p", command=lambda: self.change_resolution("1080p"))
        button_1080p.pack(pady=5)

        '''button_keybind = tk.Button(self, text="Changer le keybind", command=lambda: self.change_keybind(keybind_entry.get()))
        button_keybind.pack(pady=5)

        button_save = tk.Button(self, text="Sauvegarder", command=lambda: self.save_keybind(keybind_entry))
        button_save.pack(pady=5)'''


        button_bottom = tk.Button(self, text="Quitter", command=self.quit_application) # Permet de faire un boutton quitter ( à incorporer partout !)
        button_bottom.pack(side=tk.BOTTOM, pady=10)

        button_middle = tk.Button(self, text="Retour au Menu", command=self.show_main_menu)
        button_middle.pack(pady=20)


        button_bottom = tk.Button(self, text="Updates", command=self.show_updates)
        button_bottom.pack(side=tk.BOTTOM, pady=10)


        button_middle = tk.Button(self, text="Retour au Menu", command=self.show_main_menu)
        button_middle.pack(side=tk.BOTTOM, pady=10)

    def quit_application(self):
        app.destroy()
        print("App Quitté")

        button_bottom = tk.Button(self, text="Quitter", command=self.quit_application) # Permet de faire un boutton quitter ( à incorporer partout !)
        button_bottom.pack(side=tk.RIGHT, pady=100, padx=10)

    def quit_application(self):
        app.destroy()
        print("App quitté")

        
    def show_main_menu(self):
        self.app.notebook.select(0)  # Sélectionne la page du menu principal
        print("Menu Principal Affiché")

    def show_updates(self):
        self.app.notebook.select(2)  # Sélectionne la page des crédits
        print("Updates Affiché")

    def change_geometry_400(self):
        print("Changer la géométrie en 400*400")
        self.geometry("400x400")
                      
    def show_updates(self, event=None):
        self.app.notebook.select(2)  # Sélectionne la page des crédits
        print("Updates Affiché")

    def change_resolution(self, new_resolution):
        print(f"Changer la résolution en {new_resolution}")

'''
    def change_keybind(self, new_keybind):
        self.app.unbind(f"<KeyPress-{self.app.key_to_bind}>")  # Désassocie l'ancien keybind
        self.app.key_to_bind = new_keybind
        self.app.bind(f"<KeyPress-{self.app.key_to_bind}>", self.show_updates)  # Associe la nouvelle touche à la fonction show_credits

    def save_keybind(self, keybind_entry):
        new_keybind = keybind_entry.get()
        self.change_keybind(new_keybind)
'''
class UpdatePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        label = tk.Label(self, text="Page Des Mises à jour")
        label.pack(padx=10, pady=10)

        button_bottom = tk.Button(self, text="Quitter", command=self.quit_application)
        button_bottom.pack(side=tk.BOTTOM, pady=10)

        button_bottom = tk.Button(self, text="About", command=self.show_about)
        button_bottom.pack(side=tk.BOTTOM, pady=10)

        button_middle = tk.Button(self, text="Retour au Menu", command=self.show_main_menu)
        button_middle.pack(side=tk.BOTTOM, pady=10)


    def show_main_menu(self):
        app.notebook.select(0)  # Sélectionne la page du menu principal
        print("Menu Principal Affiché")

    def quit_application(self):
        app.destroy()
        print("App Quitté")

    def show_about(self):
        app.notebook.select(3)
        print("About Affiché")

        label = tk.Label(self, text="Page des Mises à jour")
        label.pack(padx=10, pady=10)

        button_middle = tk.Button(self, text="Retour au Menu", command=self.show_main_menu)
        button_middle.pack(pady=20)

        button_bottom = tk.Button(self, text="Quitter", command=self.quit_application)
        button_bottom.pack(side=tk.BOTTOM, pady=10)

    def show_main_menu(self):
        app.notebook.select(0)  # Sélectionne la page du menu principal

    def quit_application(self):
        app.destroy()

class AboutPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        label = tk.Label(self, text="Créé par : Alexandre_1a")
        label.pack(side=tk.TOP, pady=1)

        label = tk.Label(self, text="2023-2024 Alexandre_1a")
        label.pack(side=tk.TOP, pady=1)

        label = tk.Label(self, text="Made With Python (Tkinter) and some programmer magic")
        label.pack(side=tk.TOP, pady=1)
                      
        label.pack(padx=10, pady=10)
        label = tk.Label(self, text="2023-2024 Alexandre_1a")
        label.pack(padx=10, pady=5)

        button_middle = tk.Button(self, text="Retour au Menu", command=self.show_main_menu)
        button_middle.pack(pady=20)


        button_bottom = tk.Button(self, text="Quitter", command=self.quit_application) # Permet de faire un boutton quitter ( à incorporer partout !)
        button_bottom.pack(side=tk.BOTTOM, pady=10)


        button_middle = tk.Button(self, text="Retour Au Menu", command=self.show_main_menu)
        button_middle.pack(side=tk.BOTTOM, pady=10)

    def show_main_menu(self):
        app.notebook.select(0)  # Sélectionne la page du menu principal
        print("Menu Principal Affiché")
    def show_main_menu(self):
        app.notebook.select(0)  # Sélectionne la page du menu principal

    def quit_application(self):
        app.destroy()

if __name__ == "__main__":
    app = Application()
    app.mainloop()