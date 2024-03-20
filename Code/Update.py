import json
import requests
import os
import os.path
from urllib import request

# Définition de la variable
manifest=str("-")
# Définition du chemin du fichier JSON local
fichier_local = "manifest_current.json"

def File_Download():   
    # Téléchargement du fichier JSON distant
    url_fichier_json = "https://raw.githubusercontent.com/Alexandre1a/App_Repo/Production/manifest.json"
    response = requests.get(url_fichier_json)
    print("Fichier téléchargé !")
    # Décodage du fichier JSON distant
    contenu_json_distant = json.loads(response.content)
    with open("manifest.json", "wb") as fichier:
        fichier.write(response.content)
        print("Fichier écrit !")

def internet_on():
    try:
        request.urlopen('https://google.com', timeout=10)
        return True
        print("Internet ok ! (en principe)")
    except request.URLError as err: 
        return False
        print("Connection échouée !")

def Check_Changes():
    # Si le téléchargement du fichier distant est OK
    if internet_on()==True:
        # Lecture du fichier JSON local
        with open(fichier_local, "r") as fichier:
            contenu_json_local = json.load(fichier)
            print("Fichier lu !")

        # Extraction des versions + Définition de là où est le fichier distant
        url_fichier_json = "https://raw.githubusercontent.com/Alexandre1a/App_Repo/Production/manifest.json"
        response = requests.get(url_fichier_json)
        contenu_json_distant = json.loads(response.content)
        version_telechargee = contenu_json_distant["version"]
        version_locale = contenu_json_local["version"]
        print("Versions extraites des JSON !")
       
        # Comparaison des versions
        if version_telechargee > version_locale:
            print("+")
            manifest="+"
        elif version_telechargee < version_locale:
            print("-")
            manifest="-"
        else:
            print("=")
            manifest="="
        print("Fichiers comparés !")
    else:
        print("Erreur lors de la comparaison des version ! (Erreur inconue !)")


def Update():
    if os.path.isfile("manifest.json"):
        print("Fichier présent !")
        Check_Changes()
        if manifest== "+":
            print("Update Available, starting the upgrade process !")
            
        # Removes the old manifest and rename the new one for the next update 
        os.remove("manifest_current.json")
        os.rename("manifest.json", "manifest_current.json")
    else:
        print("Fichier non présent donc téléchargé !")
        File_Download()

Update()
'''
if Update()==False:
    Update()
'''