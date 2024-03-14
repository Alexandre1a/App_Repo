import json
import requests
import os
from urllib import request

# Définition de la variable
manifest=str(".")
# Définition du chemin du fichier JSON local
fichier_local = "manifest_OLD.json"

# Téléchargement du fichier JSON distant
url_fichier_json = "https://raw.githubusercontent.com/Alexandre1a/App_Repo/Test/manifest.json"
response = requests.get(url_fichier_json)
def internet_on():
    try:
        request.urlopen('http://216.58.192.142', timeout=1)
        return True
    except request.URLError as err: 
        return False

# Si le téléchargement du fichier distant est OK
if response.status_code == 200 and internet_on==True:
    # Décodage du fichier JSON distant
    contenu_json_distant = json.loads(response.content)
    with open("manifest.json", "wb") as fichier:
        fichier.write(response.content)

    # Lecture du fichier JSON local
    with open(fichier_local, "r") as fichier:
        contenu_json_local = json.load(fichier)

    # Extraction des versions
    version_telechargee = contenu_json_distant["version"]
    version_locale = contenu_json_local["version"]

    # Comparaison des versions
    if version_telechargee > version_locale:
        print("+")
        manifest="+"
        os.remove("manifest_OLD.json")
        os.rename("manifest.json", "manifest_OLD.json")
    elif version_telechargee < version_locale:
        print("-")
        manifest="-"
    else:
        print("=")
        manifest="="
        os.remove("manifest_OLD.json")
        os.rename("manifest.json", "manifest_OLD.json")
else:
    print("Erreur lors du téléchargement du fichier JSON distant (Vérifiez votre connection internet !)")