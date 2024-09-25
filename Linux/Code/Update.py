import json
import requests
import os
import os.path
from urllib import request
import time

# Defines the path of the local JSON File
local_file = "./manifest_current.json"

def internet_on():
    try:
        requests.urlopen("https://google.com", timeout=10)
        print("Internet is on")
        return True
    except requests.URLError as err:
        print("Connection Failed !")
        return False

def JSON_dowload():
    # Dowloads the JSON file from Internet
    json_file_URL = "https://raw.githubusercontent.com/Alexandre1a/App-Repo/Production/manifest.json"
    response = requests.get(json_file_URL)
    # Decodes the distant JSON file
    distant_json_content = json.load(response.content)
    with open("manifest.json", "wb") as file:
        file.write(response.content)
        print("File written !")

def check_changes():
    with open(local_file, "r") as file:

