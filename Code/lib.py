# Usefull libs !
import tkinter as tk
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

def popupmsg(msg):
    popup = tk.Tk()
    popup.geometry("600x500")
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="let's go !", command = popup.destroy)
    B1.pack()
    popup.mainloop()