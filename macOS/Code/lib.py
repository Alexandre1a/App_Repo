# Usefull libs !
import tkinter as tk
from tkinter import ttk
from Update import Check_Changes
import threading

LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)


def popupmsg(msg):
    popup = tk.Tk()
    popup.geometry("270x70")
    popup.wm_title("Update Available !")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay !", command = popup.destroy)
    B1.pack()
    popup.mainloop()
