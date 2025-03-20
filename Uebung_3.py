import random
import os
class Uebungen:

    @staticmethod
    def schere_stein_papier():
        moegliche_auswahl = ["Schere", "Stein", "Papier", "Spock", "Echse"]
        gewinnkombinationen = [
            ("Schere", "Papier"), ("Schere", "Echse"),
            ("Stein", "Schere"), ("Stein", "Echse"),
            ("Papier", "Stein"), ("Papier", "Spock"),
            ("Spock", "Schere"), ("Spock", "Stein"),
            ("Echse", "Spock"), ("Echse", "Papier")
        ]

        auswahl = input("Wähle Schere, Stein, Papier, Spock oder Echse: ").capitalize()

        if auswahl not in moegliche_auswahl:
            print("Ungültige Eingabe! Bitte wähle zwischen Schere, Stein, Papier, Spock oder Echse.")
            return "Du warst zu blöd"

        computer_wahl = random.choice(moegliche_auswahl)
        print(f"Computer wählt: {computer_wahl}")

        if auswahl == computer_wahl:
            print("Unentschieden!")
            return "Unentschieden"
        elif (auswahl, computer_wahl) in gewinnkombinationen:
            print("Du gewinnst!")
            return "Gewonnen"
        else:
            print("Computer gewinnt!")
            return "Verloren"

    @staticmethod
    def lade_punkte(dateiname):
        # Wenn die Datei existiert, lade die gespeicherten Punkte
        if os.path.exists(dateiname):
            with open(dateiname, 'r') as f:
                lines = f.readlines()
                if len(lines) == 2:
                    user_punkte = int(lines[0].strip())
                    computer_punkte = int(lines[1].strip())
                    return user_punkte, computer_punkte
        return 0, 0

    @staticmethod
    def speichere_punkte(dateiname, user_punkte, computer_punkte):
        # Speichere die Punkte in die Datei
        with open(dateiname, 'w') as f:
            f.write(f"{user_punkte}\n")
            f.write(f"{computer_punkte}\n")

    def main(self):
        spielen = True
        liste_der_ergebnisse = []
        dateiname = "Punkte.txt"
        gewonnen_anzahl,verloren_anzahl = self.lade_punkte(dateiname)

        print(f"Zwischenstand {gewonnen_anzahl} : {verloren_anzahl}")

        while spielen:
            liste_der_ergebnisse.append(self.schere_stein_papier())
            print("Willst du nochmal spielen? ja oder nein")
            if input().lower().startswith("n"):
                spielen = False

        gewonnen_anzahl = liste_der_ergebnisse.count("Gewonnen")
        verloren_anzahl = liste_der_ergebnisse.count("Verloren")
        unenschieden_anzahl = liste_der_ergebnisse.count("Unentschieden")

        gesamtgewinner = "Unentschieden"
        if gewonnen_anzahl > verloren_anzahl:
            gesamtgewinner = "Du bist der Gesamtsieger!"
        elif verloren_anzahl > gewonnen_anzahl:
            gesamtgewinner = "Du hast insgesamt verloren."

        print(f"Du hast beim Spielen folgende Ergebnisse erzielt: Du hast {gewonnen_anzahl} mal gewonnen, "
              f"{verloren_anzahl} mal verloren und {unenschieden_anzahl} mal unentschieden gespielt.\n"
              f"Dein Gesamtverlauf ist {liste_der_ergebnisse}.\n"
              f"Gesamt Ergebnis: {gesamtgewinner}")

        self.speichere_punkte(dateiname, gewonnen_anzahl, verloren_anzahl)

if __name__ == '__main__':
    uebungen_17_03 = Uebungen()
    uebungen_17_03.main()