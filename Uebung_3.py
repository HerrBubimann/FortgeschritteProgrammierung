import random
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

    def main(self):
        spielen = True
        liste_der_ergebnisse = []
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


if __name__ == '__main__':
    uebungen_17_03 = Uebungen()
    uebungen_17_03.main()