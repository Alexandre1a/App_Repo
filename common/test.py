import json
import requests
import os
import os.path
from urllib import request
import time

local_file = "./test1.json"
distant_file = "./test2.json"

a=0

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

def File_Cleaner():
    os.remove(local_file)
    os.rename(distant_file, local_file)

while a < 2:
    choice = str(input("Entrez L'URL "))
    nom = str(input("Choisisez le nom "))
    File_download(choice, nom)
    a= a+1

File_Cleaner()