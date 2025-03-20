class Uebungen:

    @staticmethod
    def drei_chinesen(text, variable):
        """
        Static-Methode: Ersetzt bestimmte Zeichen im Text durch den Wert der 'variable'.
        """
        # Dictionary mit Ersetzungen: Bestimmte Zeichen werden durch die 'variable' ersetzt
        reinfolge_zu_ersetzten = {
            "ie": variable, "au": variable, "eu": variable, "ei": variable,
            "a": variable, "e": variable, "o": variable, "u": variable,
            "ä": variable, "ö": variable, "ü": variable, "i": variable
        }

        # Schleife über die Schlüssel im Dictionary, um die Ersetzungen vorzunehmen
        for key in reinfolge_zu_ersetzten:
            """ 
            Ersetzt alle Vorkommen von 'key' im Text durch den entsprechenden Wert (variable).
            """
            text = text.replace(key, reinfolge_zu_ersetzten[key])

        # Gibt den modifizierten Text zurück
        return text

    @staticmethod
    def main():
        """
        Hauptmethode: Testet die Ersetzungen für eine Liste von Wörtern mit verschiedenen 'variable' Werten.
        """
        # Liste von Testwörtern, die bearbeitet werden sollen
        testworte = ["Drei", "Chinesen", "mit", "Kontrabass", "sassen", "auf", "der", "Strasse", "und", "erzählten",
                     "sich", "was"]

        # Liste der zu ersetzenden Zeichen (Vokale und Umlaute)
        zu_ersetzten = ["a", "e", "o", "u"]

        # Schleife über jede 'variable' in der Liste 'zu_ersetzten'
        for variable in zu_ersetzten:
            ergebniss = ""
            # Schleife über jedes Wort in der Liste 'testworte'
            for wort in testworte:
                #Ersetzt jedes Wort mit der Methode 'drei_chinesen' und fügt es zum Ergebnis hinzu.
                ergebniss += " " + Uebungen.drei_chinesen(wort, variable)
            # Gibt das Ergebnis nach jeder 'variable' aus
            print(ergebniss)


if __name__ == '__main__':
    uebungen_20_03 = Uebungen()
    uebungen_20_03.main()
