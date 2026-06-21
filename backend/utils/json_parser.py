import json
from typing import List, Dict, Any

def json_parser(filepath: str) -> Dict[str, Any]:
    with open(filepath, "r") as file:
        data = json.load(file)
    if data:
        return data
    return {}