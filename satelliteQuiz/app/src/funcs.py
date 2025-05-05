from pathlib import Path
import json
from os.path import exists

def readJson(path: str):
    path = Path(path)
    
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return data

def createUserJson(path: str):
    path: Path = Path(path)


    if not exists(path):
        with path.open("w", encoding="utf-8") as file:
            data: dict = {"points": 0}
            json.dump(data, file, indent=4)

    return path

def updateJson(path: str, points: int = 0):
    path: Path = Path(path)

    data = readJson(path)

    if not exists(path):
        createUserJson(path)

    data["points"] = data["points"] + points

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
        
    return "Points added"

