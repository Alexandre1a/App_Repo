import json
import requests
import os
import os.path
from urllib import request
import time

def File_download(url, name):
    response = requests.get(url)
    '''
    if Is_File_Here(name) == True:
        os.remove(name)
    '''
    if response.status_code == 200:
        with open(name, "wb") as file:
            file.write(response.content)
        print(f"Le fichier {name}")
        
choice = str(input("Entrez L'URL "))
nom = str(input("Choisisez le nom "))

File_download(choice, nom)    