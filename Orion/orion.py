from memory import laden, speichern
from calculator import rechnen
from notes import notiz_hinzufuegen, notizen_anzeigen
from tasks import task_hinzufuegen, tasks_anzeigen
from websearch import suche
from wissen import wissen

daten = laden()

print("Orion AI gestartet!")
print("Tippe 'hilfe' für Befehle.")

while True:
    
    text = input("Du: ").lower()



    if text in wissen:
        print("Orion:", wissen[text])
        continue



    if text.lower() == "ende":
        speichern(daten)
        print("Orion: Tschüss!")
        break

    elif text.lower() == "hilfe":
        print("""
Befehle:

notiz TEXT
notizen

task TEXT
tasks

merke NAME WERT
zeige NAME

suche TEXT

Rechenaufgaben:
5+5
100/4
25*12
5 + 3 = 8
10 - 4 = 6
7 + 6 = 13
9 - 2 = 7
8 + 8 = 16
✖️ Multiplikation
3 × 4 = 12
6 × 5 = 30
7 × 7 = 49
9 × 3 = 27
8 × 6 = 48
➗ Division
12 ÷ 3 = 4
20 ÷ 5 = 4
18 ÷ 2 = 9
24 ÷ 6 = 4
36 ÷ 9 = 4
🧠 Gemischte Aufgaben
5 + 3 × 2 = 11
(10 + 5) ÷ 3 = 5
8 × 2 + 6 = 22
20 - 4 × 3 = 8
(7 + 3) × 2 = 20
🔥 Schwieriger
125 × 4 = 500
144 ÷ 12 = 12
15² = 225
9³ = 729
√64 = 8

ende
""")

    elif text.lower().startswith("notiz "):
        notiz_hinzufuegen(daten, text[6:])
        speichern(daten)
        print("Orion: Notiz gespeichert.")

    elif text.lower() == "notizen":

        for n in notizen_anzeigen(daten):
            print("-", n)

    elif text.lower().startswith("task "):
        task_hinzufuegen(daten, text[5:])
        speichern(daten)
        print("Orion: Aufgabe gespeichert.")

    elif text.lower() == "tasks":

        for t in tasks_anzeigen(daten):
            print("-", t)

    elif text.lower().startswith("merke "):

        teile = text[6:].split(" ", 1)

        if len(teile) == 2:
            daten[teile[0]] = teile[1]
            speichern(daten)
            print("Orion: Gemerkt.")

    elif text.lower().startswith("zeige "):

        key = text[6:]

        if key in daten:
            print("Orion:", daten[key])
        else:
            print("Orion: Nicht gefunden.")

    elif text.lower().startswith("suche "):
        suche(text[6:])
        print("Orion: Suche wird geöffnet.")

    else:

        erg = rechnen(text)

        if erg is not None:
            print("Orion:", erg)
        else:
            print("Orion: Das verstehe ich noch nicht.")
