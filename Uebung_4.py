class Uebungen:

    @staticmethod
    def drei_chinesen(text, variable):
        reinfolge_zu_ersetzten = {
            "ie": variable, "au": variable, "eu": variable, "ei": variable,
            "a": variable, "e": variable, "o": variable, "u": variable,
            "ä": variable, "ö": variable, "ü": variable, "i": variable
        }

        for key in reinfolge_zu_ersetzten:
            text = text.replace(key, reinfolge_zu_ersetzten[key])

        return text


if __name__ == '__main__':
    uebungen_20_03 = Uebungen()
    testworte = ["Drei", "Chinesen", "mit", "Kontrabass", "sassen", "auf", "der", "Strasse", "und", "erzählten", "sich", "was"]
    zu_ersetzten = ["a", "e", "o", "u"]

    for variable in zu_ersetzten:
        ergebniss = ""
        for wort in testworte:
            ergebniss += " " + uebungen_20_03.drei_chinesen(wort, variable)
        print(ergebniss)
