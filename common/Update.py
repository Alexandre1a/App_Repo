import json
import requests
import os
import os.path
from urllib import request
import time

# Defines the path of the local JSON File
local_file = "./manifest_current.json"
distant_file = "./manifest.json"
distant_file_URL = "https://raw.githubusercontent.com/Alexandre1a/App_Repo/Production/manifest.json"
both_file = False

def internet_on():
    try:
        request.urlopen("https://google.com", timeout=10)
        print("Internet is on")
        return True
    except request.URLError as err:
        print("Connection Failed !")
        return False

def Is_File_Here(file):
    try:
        if os.path.isfile(file):
            return True
    except AttributeError:
        print("File missing")
        return False
        
def File_Cleaner():
    os.remove(local_file)
    os.rename(distant_file, "manifest_current.json")

def JSON_dowload():
    # Dowloads the JSON file from Internet
    json_file_URL = "https://raw.githubusercontent.com/Alexandre1a/App_Repo/Production/manifest.json"
    response = requests.get(json_file_URL)
    # Decodes the distant JSON file
    distant_json_content = json.load(response.content)
    with open("manifest.json", "wb") as file:
        file.write(response.content)
        print("File written !")
    return True

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


def check_changes():
    Dependencies()
    with open(local_file, "r") as file:
        local_json_content = json.load(file)
        print("File read")
        with open(distant_file) as f:
            distant_content = json.load(f)
        downloaded_version = distant_content["version"]
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

def Dependencies():
    global both_file
    if Is_File_Here(local_file) and internet_on():
        File_download(distant_file_URL, "manifest.json")
        return True
    elif Is_File_Here(local_file) and Is_File_Here(distant_file) and internet_on() == True: 
        return True
        

def Update():
    if Dependencies() == True:
        result = check_changes()
        if result == str("+"):
            with open(local_file, "r") as f:
                data = json.load(f)["files"]
            name = []
            URL = []
            for fichier in data:
                URL = fichier["link"]
                name = fichier["name"]
                File_download(URL, name)
            File_Cleaner()
        elif result == str("="):
            print("no update")
        
Update()