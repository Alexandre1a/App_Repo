import customtkinter as ctk
from nava import *
import time
import threading
import os

# Set the colors
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x240")

# Sets the default time
initial_time = 0

# Sets the start time
start_time = None

# Sets the status of the countdown
is_running = False

def update_countown():
    global initial_time, start_time, is_running

    # 

def play_song():
    sound_id = play("./Musics/test.wav", async_mode=True)
    try:
        sound_id = play("./Musics/text.wav", async_mode=True)
    except NavaBaseError as e:
        print(str(e))

play_button = ctk.CTkButton(master= app, text="Play", command=play_song)
play_button.place(relx=0.5, rely=0.5, anchor=ctk.SW)





app.mainloop()