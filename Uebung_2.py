import random
class Uebungen:
    @staticmethod
    def mittelwert_berechen():
        """
        Berchnet den Durschnitt der Zahlen welche der nutzer eingibt
        """
        zahlen = []

        while True:
            input_gerade = input("Zahl eingeben (oder 'Fertig' damit alle Zahlen eingeben sind): ")

            if input_gerade.lower() == 'fertig':
                break

            try:
                aktuellerinput = float(input_gerade)
                zahlen.append(aktuellerinput)
            except ValueError:
                print("Bitte geben Sie eine Zahl ein.")

        if zahlen:
            average = sum(zahlen) / len(zahlen)
            print(f"Durschnitt: {average:.2f}")
        else:
            print("keine eingetragen Zahl.")

    @staticmethod
    def drei_mal_wuerfen():
        """
        :return sum von drei würffeln
        """
        return sum(random.randint(1, 6) for i in range(3))

    def summe_der_wuerfe(self, anzahl:int):
        summe = 0
        for i in range(anzahl):
            summe += self.drei_mal_wuerfen()
        return summe

    @staticmethod
    def get_AT_gehalt(dna = "ABCSDADATWA", runden = 2):
        """
        :param dna: als String
        :param runden:  die nachkommerstellen wo gerundetwerden soll
        :return gehalt: gehalt der mitarbeiter gerundet auf die nachkommerstellen
        """
        laenge = len(dna)
        A_anzahl = dna.upper().count('A')
        T_anzahl = dna.upper().count('T')
        AT_gehalt = (A_anzahl + T_anzahl) / laenge
        return round(AT_gehalt, runden)

if __name__ == '__main__':
    uebungen_13_03 = Uebungen()
    #print(uebungen_13_03.summe_der_wuerfe(100))
    print(uebungen_13_03.get_AT_gehalt("ATGCTAGT", 2))
    print(uebungen_13_03.get_AT_gehalt("AAAA", 0))
    print(uebungen_13_03.get_AT_gehalt("GGTA", 7))
