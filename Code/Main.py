import tkinter as tk
import subprocess

def open_program_1():
    subprocess.Popen(['python', '.\App Repo/Launcher/V0.py'])

def open_program_2():
    subprocess.Popen(['python', 'program2.py'])

def open_program_3():
    subprocess.Popen(['python', '.\Launcher/V0.py'])

def close_program():
    root.destroy()


# Créer la fenêtre principale
root = tk.Tk()

# Définir la taille de la fenêtre
root.geometry("1280x720")

# Créer les boutons pour ouvrir les programmes
button1 = tk.Button(root, text="Ouvrir Programme 1", command=open_program_1)
button1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

button2 = tk.Button(root, text="Ouvrir Programme 2", command=open_program_2)
button2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

button3 = tk.Button(root, text="Ouvrir Programme 3", command=open_program_3)
button3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Créer le bouton pour fermer le programme
close_button = tk.Button(root, text="Close", command=close_program)
close_button.place(relx=1, rely=1, anchor=tk.SE)

# Démarrer la boucle principale de la fenêtre
root.mainloop()