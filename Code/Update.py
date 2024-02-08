import json
import requests
import os

# Définition du chemin du fichier JSON local
fichier_local = "manifest_OLD.json"

# Téléchargement du fichier JSON distant
url_fichier_json = "https://raw.githubusercontent.com/Alexandre1a/App_Repo/Test/manifest.json"
response = requests.get(url_fichier_json)

# Si le téléchargement du fichier distant est OK
if response.status_code == 200:
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
        os.remove("manifest_OLD.json")
        os.rename("manifest.json", "manifest_OLD.json")
    elif version_telechargee < version_locale:
        print("-")
    else:
        print("=")
        os.remove("manifest_OLD.json")
        os.rename("manifest.json", "manifest_OLD.json")
else:
    print("Erreur lors du téléchargement du fichier JSON distant")
