import random
import os

class Uebungen:
    @staticmethod
    def schere_stein_papier():
        """
        Diese Methode führt eine Runde Schere, Stein, Papier, Spock, Echse durch.
        Der Benutzer wählt eine Option, der Computer wählt zufällig, und das Ergebnis wird ermittelt.

        Rückgabewerte:
            - "Du warst zu blöd" bei ungültiger Eingabe.
            - "Unentschieden" bei einem Unentschieden.
            - "Gewonnen" bei einem Sieg des Benutzers.
            - "Verloren" bei einer Niederlage des Benutzers.
        """
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
        """
        Diese Methode lädt die Punktzahlen des Benutzers und des Computers aus einer Datei.

        Parameter:
            - dateiname: Der Name der Datei, aus der die Punkte geladen werden.

        Rückgabewerte:
            - Ein Tupel mit den Punkten des Benutzers und des Computers.
            - Wenn die Datei nicht existiert oder nicht die erwarteten Daten enthält, wird 0, 0 zurückgegeben.
        """
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
        """
        Diese Methode speichert die Punktzahlen des Benutzers und des Computers in einer Datei.

        Parameter:
            - dateiname: Der Name der Datei, in die die Punkte gespeichert werden.
            - user_punkte: Die aktuellen Punkte des Benutzers.
            - computer_punkte: Die aktuellen Punkte des Computers.
        """
        with open(dateiname, 'w') as f:
            f.write(f"{user_punkte}\n")
            f.write(f"{computer_punkte}\n")

    @staticmethod
    def drucke_zwischenstand(gewonnen_anzahl, verloren_anzahl):
        """
        Diese Methode druckt den aktuellen Zwischenstand des Spiels.

        Parameter:
            - gewonnen_anzahl: Anzahl der gewonnenen Spiele des Benutzers.
            - verloren_anzahl: Anzahl der verlorenen Spiele des Benutzers.
        """
        print(f"Zwischenstand {gewonnen_anzahl} : {verloren_anzahl}")

    @staticmethod
    def spiele_runden():
        """
        Diese Methode führt mehrere Runden des Spiels durch und speichert die Ergebnisse jeder Runde.

        Rückgabewerte:
            - Eine Liste der Ergebnisse aller gespielten Runden.
        """
        liste_der_ergebnisse = []
        spielen = True
        while spielen:
            liste_der_ergebnisse.append(Uebungen.schere_stein_papier())
            print("Willst du nochmal spielen? ja oder nein")
            if input().lower().startswith("n"):
                spielen = False
        return liste_der_ergebnisse

    @staticmethod
    def bestimme_gesamtgewinner(gewonnen_anzahl, verloren_anzahl):
        """
        Diese Methode bestimmt den Gesamtsieger basierend auf der Anzahl der gewonnenen und verlorenen Spiele.

        Parameter:
            - gewonnen_anzahl: Anzahl der gewonnenen Spiele des Benutzers.
            - verloren_anzahl: Anzahl der verlorenen Spiele des Benutzers.

        Rückgabewert:
            - Eine Nachricht, die den Gesamtsieger des Spiels angibt.
        """
        if gewonnen_anzahl > verloren_anzahl:
            return "Du bist der Gesamtsieger!"
        elif verloren_anzahl > gewonnen_anzahl:
            return "Du hast insgesamt verloren."
        return "Unentschieden"

    @staticmethod
    def drucke_endergebnisse(gewonnen_anzahl, verloren_anzahl, unentschieden_anzahl, liste_der_ergebnisse,
                             gesamtgewinner):
        """
        Diese Methode druckt die Endergebnisse des Spiels, einschließlich der Anzahl der gewonnenen, verlorenen und unentschiedenen Runden.

        Parameter:
            - gewonnen_anzahl: Anzahl der gewonnenen Spiele des Benutzers.
            - verloren_anzahl: Anzahl der verlorenen Spiele des Benutzers.
            - unentschieden_anzahl: Anzahl der unentschiedenen Spiele.
            - liste_der_ergebnisse: Liste der Ergebnisse aller gespielten Runden.
            - gesamtgewinner: Der Gesamtsieger des Spiels.
        """
        print(f"Du hast beim Spielen folgende Ergebnisse erzielt: Du hast {gewonnen_anzahl} mal gewonnen, "
              f"{verloren_anzahl} mal verloren und {unentschieden_anzahl} mal unentschieden gespielt.\n"
              f"Dein Gesamtverlauf ist {liste_der_ergebnisse}.\n"
              f"Gesamt Ergebnis: {gesamtgewinner} ({gewonnen_anzahl} : {verloren_anzahl})")

    @staticmethod
    def main():
        """
        Diese Methode führt das gesamte Spiel durch, lädt die Punktzahlen, spielt Runden, aktualisiert die Punkte und gibt die Endergebnisse aus.
        """
        dateiname = "Punkte.txt"
        gewonnen_anzahl, verloren_anzahl = Uebungen.lade_punkte(dateiname)
        Uebungen.drucke_zwischenstand(gewonnen_anzahl, verloren_anzahl)

        liste_der_ergebnisse = Uebungen.spiele_runden()

        gewonnen_anzahl += gewonnen_anzahl + liste_der_ergebnisse.count("Gewonnen")
        verloren_anzahl += verloren_anzahl + liste_der_ergebnisse.count("Verloren")
        unentschieden_anzahl = liste_der_ergebnisse.count("Unentschieden")

        gesamtgewinner = Uebungen.bestimme_gesamtgewinner(gewonnen_anzahl, verloren_anzahl)

        Uebungen.drucke_endergebnisse(gewonnen_anzahl, verloren_anzahl, unentschieden_anzahl, liste_der_ergebnisse,
                                  gesamtgewinner)

        Uebungen.speichere_punkte(dateiname, gewonnen_anzahl, verloren_anzahl)


if __name__ == '__main__':
    Uebungen.main()