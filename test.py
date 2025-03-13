zahlen = []

while True:
    input_benutzer = input("Zahl eingeben (oder 'f' damit alle Zahlen eingeben sind): ")

    if input_benutzer.lower() == 'F'.lower:
        break

    try:
        aktueller_input = float(input_benutzer)
        zahlen.append(aktueller_input)
    except ValueError:
        print("Bitte geben Sie eine Zahl ein.")

if zahlen:
    average = sum(zahlen) / len(zahlen)
    print(f"Durschnitt: {average:.2f}")
else:
    print("Keine eingetragen Zahl.")
