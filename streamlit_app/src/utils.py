import pandas as pd
from typing import List

def readJson(path: str) -> pd.DataFrame:
    json = pd.read_json(path)
    
    return json
    
    
    
