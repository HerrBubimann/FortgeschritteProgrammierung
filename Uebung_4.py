class Uebungen:

    @staticmethod
    def drei_chinesen(wort, variable):
        """
        Ersetzt bestimmte Zeichen im Text durch den Wert der 'variable'.
        """
        reinfolge_zu_ersetzten = {
            "ie": variable, "au": variable, "eu": variable, "ei": variable,
            "a": variable, "e": variable, "o": variable, "u": variable,
            "ä": variable, "ö": variable, "ü": variable, "i": variable
        }

        for key in reinfolge_zu_ersetzten:
            wort = wort.replace(key, reinfolge_zu_ersetzten[key])
        return wort

    @staticmethod
    def main():
        testworte = ["Drei", "Chinesen", "mit", "Kontrabass", "sassen", "auf", "der", "Strasse", "und", "erzählten",
                     "sich", "was"]

        zu_ersetzten = ["a", "e", "o", "u"]

        for variable in zu_ersetzten:
            ergebniss = ""
            for wort in testworte:
                ergebniss += " " + Uebungen.drei_chinesen(wort, variable)
            print(ergebniss)

class Katze:
    def __init__(self, name, farbe, alter=1, geschlecht = True):
        self.name = name
        self.farbe = farbe
        self.alter = alter
        self.geschlecht = geschlecht

    def gebe_aus(self):
        print(f'Die Katze heisst {self.name} und ist {self.alter} Jahre alt und hat die Farbe {self.farbe}')

    def __str__(self):
        geschlecht_str = "männlich" if self.geschlecht else "weiblich"
        return f"Katze: {self.name}, Alter: {self.alter}, Farbe: {self.farbe}, Geschlecht: {geschlecht_str}"

    def miau(self):
        print(f"{self.name} hat miauut")

    @staticmethod
    def main():
        cat_1 = Katze(name='Mietze', alter=5, farbe='grau', geschlecht=True)
        cat_2 = Katze(name='Mietze_2', alter=6, farbe='grau', geschlecht=False)
        cat_1.gebe_aus()
        cat_1.miau()
        cat_2.miau()
        cat_2.gebe_aus()


if __name__ == '__main__':
    uebungen_20_03 = Uebungen()
    uebungen_20_03.main()
    #Katze.main()
