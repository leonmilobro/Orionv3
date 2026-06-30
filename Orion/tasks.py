def task_hinzufuegen(daten, text):
    if "tasks" not in daten:
        daten["tasks"] = []

    daten["tasks"].append(text)

def tasks_anzeigen(daten):
    return daten.get("tasks", [])
