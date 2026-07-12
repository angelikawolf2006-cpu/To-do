print("Meine To-Do-Liste")

aufgaben = []

aufgabe = input("Was möchtest du hinzufügen? ")

aufgaben.append(aufgabe)

print("Deine Aufgaben:")

for aufgabe in aufgaben:
    print(aufgabe)
