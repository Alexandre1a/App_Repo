import tkinter as tk
from tkinter import ttk
import threading
from Update import *
# from lib import popupmsg
import nava

with open("manifest_current.json", "r") as f:
    data = json.load(f)

version = data["version"]

LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Alexandre_1a's LAUNCHER") # Defines the size and the name of the app
        self.resizable(width=0,height=0) # Blocks the size change
        self.geometry("400x500")

        self.notebook = ttk.Notebook(self) # Alows the apps to have tabs
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.page1 = MainMenu(self.notebook)
        self.page2 = SettingsPage(self.notebook, self)
        self.page3 = UpdatePage(self.notebook)
        self.page4 = AboutPage(self.notebook)

        self.notebook.add(self.page1, text="Home") # Give a name to the tabs
        self.notebook.add(self.page2, text="Settings")
        self.notebook.add(self.page3, text="Updates")
        self.notebook.add(self.page4, text="About")
'''
        self.key_to_bind = "u" # Important : Changes the default keybind
        self.bind(f"<KeyPress-{self.key_to_bind}>", self.page2.show_updates)  # Binds the key to the fonction to show credits
'''
class MainMenu(tk.Frame): # Displays the main menu
    def __init__(self, parent):
        super().__init__(parent)


        label = tk.Label(self, text="Welcome to the main menu !")
        label.pack(padx=10, pady=10)

        self.Info_label = tk.Label(self,text="Hey ! You should check the Update page !")
        self.Info_label.pack(side=tk.TOP, pady=10)

        self.Version_label = tk.Label(self,text=f"Version : {version} Generic Release")
        self.Version_label.pack(anchor="n")

        button_middle = tk.Button(self, text="Test !", command=self.play_game)
        button_middle.pack(side=tk.TOP, pady=20)

        if internet_on() == False:
            self.Info_label.configure(text="No internet connection available")
            self.Verify_button = tk.Button(self, text="Check Again", command=internet_on())
            self.Verify_button.pack(side=tk.TOP, pady= 30)

        button_bottom = tk.Button(self, text="Close", command=self.quit_application) # Permet de faire un boutton quitter ( à incorporer partout !)
        button_bottom.pack(side=tk.BOTTOM, pady=10)

        button_bottom = tk.Button(self, text="Settings", command=self.show_settings)
        button_bottom.pack(side=tk.BOTTOM, pady=10)


    def Test():
        UpdatePage.thread_it

    def quit_application(self):
        app.destroy()
        print("App Closed")

    def play_game(self):
        print("Test Is OK")

    def show_settings(self): # Sélectionne la page des paramètres
        app.notebook.select(1)
        print("Settings displayed")  
        


class SettingsPage(tk.Frame):
    def __init__(self, parent, app_instance):
        super().__init__(parent)

        self.app = app_instance  # Stocke l'instance de l'application pour accéder à ses variables

        label = tk.Label(self, text="Settings")
        label.pack(padx=10, pady=10)

        # Boutons pour changer la résolution et le keybind
        '''
        button_400 = tk.Button(self, text="Change to 400*400", command=Application.geometry("400x400"))
        button_400.pack(pady=5)

        button_keybind = tk.Button(self, text="Changer le keybind", command=lambda: self.change_keybind(keybind_entry.get()))
        button_keybind.pack(pady=5)

        button_save = tk.Button(self, text="Sauvegarder", command=lambda: self.save_keybind(keybind_entry))
        button_save.pack(pady=5)'''

        WIP_label = tk.Label(self, text="Sorry, this tab is under construction")
        WIP_label.pack(pady=5)

        button_bottom = tk.Button(self, text="Close", command=self.quit_application) # Creates a button to quit the app 
        button_bottom.pack(side=tk.BOTTOM, pady=10)

        button_bottom = tk.Button(self, text="Updates", command=self.show_updates)
        button_bottom.pack(side=tk.BOTTOM, pady=10)


        button_middle = tk.Button(self, text="Go to main menu", command=self.show_main_menu)
        button_middle.pack(side=tk.BOTTOM, pady=10)

    def quit_application(self):
        app.destroy()
        print("App Closed")

    def show_main_menu(self):
        self.app.notebook.select(0)  # Selects the main menu
        print("Main menu displayed")

    def show_updates(self):
        self.app.notebook.select(2)  # Selects the updates page
        print("Updates Affiché")

    def change_geometry_400(self):
        print("Change geometry to 400*400")
        self.geometry("400x400")
                      
    def show_updates(self, event=None):
        self.app.notebook.select(2)  # Sélectionne la page des crédits
        print("Updates Affiché")

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

        self.Title_label = tk.Label(self, text="Update page")
        self.Title_label.pack(padx=10, pady=10)

        self.Check_button = tk.Button(self, text="Check Updates !", state="normal", command=lambda: self.thread_it(func=self.Check))
        self.Check_button.pack(padx=10, pady=10)

        self.Update_button = tk.Button(self, text="Update !", state="disable" , command=lambda: self.thread_it(func=self.Threaded_Update))
        self.Update_button.pack(side=tk.TOP, pady=10)

        self.Info_label = tk.Label(self,text="")
        self.Info_label.pack(padx=10, pady=10)

        self.Close_button = tk.Button(self, text="Close", command=self.quit_application)
        self.Close_button.pack(side=tk.BOTTOM, pady=10)

        self.About_button = tk.Button(self, text="About", command=self.show_about)
        self.About_button.pack(side=tk.BOTTOM, pady=10)

        self.Menu_button = tk.Button(self, text="Go to main menu", command=self.show_main_menu)
        self.Menu_button.pack(side=tk.BOTTOM, pady=10)

    def thread_it(self, func):
        self.myThread = threading.Thread(target=func)
        self.myThread.daemon = True  # When the main thread exits, the sub-threads exit directly after it, regardless of whether they finish running or not.
        self.myThread .start()
    
    def Threaded_Update(self):
        self.Update_button.configure(state="disabled")
        Update()
        result = check_changes()
        self.Update_button.configure(state="normal")
        if result == str("+") :
            self.Info_label.configure(text="You updated but you are still behind...")
        elif result == str("="):
            self.Info_label.configure(text="You already have the lastet version !")
            popupmsg("Update Finished")
        else:
            self.Info_label.configure(text="Uh oh !")

    def Check(self):
        self.Check_button.configure(state="disabled")
        result = check_changes()
        self.Update_button.configure(state="normal")
        if result == str("+") :
            self.Info_label.configure(text="Update available !")
        elif result == str("="):
            self.Info_label.configure(text="No update Available")
            self.Check_button.configure(state="normal")
            self.Update_button.configure(state="disabled")
        elif result == str("-"):
            self.Info_label.configure(text="Dev mode enabled")
            self.Check_button.configure(state="disabled")
            self.Update_button.configure(state="disabled")
        else:
            if internet_on() == False:
                self.Info_label.configure(text="Uh oh ! You have no internet ! Updates disabled")
                self.Update_button.configure(state="disabled")
                self.Check_button.configure(state="normal")
            else :
                self.Info_label.configure(text="Fatal error !")

    def show_main_menu(self):
        app.notebook.select(0)  # Sélectionne la page du menu principal
        print("Main menu displayed")

    def quit_application(self):
        app.destroy()
        print("App Closed")

    def show_about(self):
        app.notebook.select(3)
        print("About displayed")

    def show_main_menu(self):
        app.notebook.select(0)  # Sélectionne la page du menu principal

    def quit_application(self):
        app.destroy()

class AboutPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        label = tk.Label(self, text="Made by: Alexandre_1a")
        label.pack(side=tk.TOP, pady=1)

        label = tk.Label(self, text="2023-2025 Alexandre_1a")
        label.pack(side=tk.TOP, pady=1)

        label = tk.Label(self, text="Made With Python (Tkinter) and developed on Linux !")
        label.pack(side=tk.TOP, pady=1)

        button_bottom = tk.Button(self, text="Close", command=self.quit_application) # Permet de faire un boutton quitter ( à incorporer partout !)
        button_bottom.pack(side=tk.BOTTOM, pady=10)


        button_middle = tk.Button(self, text="Go to main menu", command=self.show_main_menu)
        button_middle.pack(side=tk.BOTTOM, pady=10)

    def show_main_menu(self):
        app.notebook.select(0)  # Sélectionne la page du menu principal
        print("Main menu displayed")

    def quit_application(self):
        app.destroy()


if __name__ == "__main__":
    app = Application()
    app.mainloop()