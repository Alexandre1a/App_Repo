import json
import requests
import os
import os.path
from urllib import request
'''
# Defines the variable
manifest=str("-")
'''
# Defines the path of the local JSON file
local_file = "manifest_current.json"

def File_Download():   
    # Downloads the JSON file from internet
    json_file_URL = "https://raw.githubusercontent.com/Alexandre1a/App_Repo/Production/manifest.json"
    response = requests.get(json_file_URL)
    print("File downloaded !")
    # Decodes the distant JSON file
    distant_json_content = json.loads(response.content)
    with open("manifest.json", "wb") as file:
        file.write(response.content)
        print("File written !")

def internet_on():
    try:
        request.urlopen('https://google.com', timeout=10)
        return True
        print("Internet is ok !")
    except request.URLError as err: 
        return False
        print("Connection failed !")

def Check_Changes():
    # If the download of the distant JSON file is OK
    if internet_on()==True:
        # Reads the local JSON
        with open(local_file, "r") as file:
            local_json_content = json.load(file)
            print("File readed !")

        # Extracts the versions + Defines where the distant JSON file is
        json_file_URL = "https://raw.githubusercontent.com/Alexandre1a/App_Repo/Production/manifest.json"
        response = requests.get(json_file_URL)
        distant_json_content = json.loads(response.content)
        downloaded_version = distant_json_content["version"]
        local_version = local_json_content["version"]
        print("Versions extracted from the JSON file !")
       
        # Comparaison des versions
        if downloaded_version > local_version:
            print("+")
            return str("+")
        elif downloaded_version < local_version:
            print("-")
            return str("-")
        else:
            print("=")
            return str("=")
        print("Files compared !")
    else:
        if internet_on()==False:
            print("Uh oh, your computer is offline or google.com is unreachable, check your internet connection !")
        else:
            print("Error while comparing versions !")


def Update():
    if os.path.isfile("manifest.json"):
        print("File exists !")
        result = Check_Changes()
        if result == str("+"):
            print("Update Available, starting the upgrade process !")
            with open("manifest.json", "r") as f:
                # Charger le contenu du fichier JSON dans une variable
                data = json.load(f)
            # Obtenir la liste des fichiers à télécharger depuis le fichier JSON
            files = data["files"]
            # Créer une liste vide pour contenir les liens
            names = []
            # Parcourir la liste des fichiers
            for fichier in files:
                # Récupérer le lien depuis le fichier
                lien = fichier["link"]
                nom_fichier = fichier["name"]
                # Ajouter les liens à la liste
                names.append(nom_fichier)
            # Télécharge les fichiers
            for i in range(len(files)):
                # Télécharge le fichier
                response = requests.get(files[i]["link"])
                if response.status_code == 200:
                    # File is ok
                    # Save the actual file
                    with open(names[i],"wb") as f:
                        f.write(response.content)
                    print(f"Le fichier {names[i]}")
        elif result == "=":
            print("You have a up to date manifest !")
        else :
            print("Seems you are a version ahead from the Release, please report this with a Github issue") 
        # Removes the old manifest and rename the new one for the next update 
        os.remove("manifest_current.json")
        os.rename("manifest.json", "manifest_current.json")  
    else:
        print("File was mission so I downloaded it !")
        File_Download()
        print("Relaunching the fonction after downloading the file")
        Update()

Update() # Uncomment this to test the program and comment it if you are testing the WORK.py

'''
if Update()==False:
    Update()
'''