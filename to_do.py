print("Meine To-Do-Liste")

aufgaben = []

aufgabe = input("Was möchtest du hinzufügen? ")

if aufgabe == "fertig":
    break

aufgaben.append(aufgabe)

print("Deine Aufgaben:")

for aufgabe in aufgaben:
    print(aufgabe)
