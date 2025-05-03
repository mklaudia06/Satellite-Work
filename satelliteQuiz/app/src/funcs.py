from pathlib import Path
import json

def readJson(path: str):
    path = Path(path)
    
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return data