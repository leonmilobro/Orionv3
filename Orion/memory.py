import json
import os

DATEI = "orion_memory.json"

def laden():
    if os.path.exists(DATEI):
        with open(DATEI, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def speichern(daten):
    with open(DATEI, "w", encoding="utf-8") as f:
        json.dump(daten, f, ensure_ascii=False, indent=4)
