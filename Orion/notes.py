def notiz_hinzufuegen(daten, text):
    if "notizen" not in daten:
        daten["notizen"] = []

    daten["notizen"].append(text)

def notizen_anzeigen(daten):
    return daten.get("notizen", [])
