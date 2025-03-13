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

    @staticmethod
    def drogrie_aufgabe():
        end_preis = 711
        ziel_nach_multiplikation = end_preis * 100 ** 3

        for a in range(1, end_preis):
            for b in range(a, end_preis - a):
                for c in range(b, end_preis - a - b):
                    d = end_preis - a - b - c
                    if d <= 1:
                        continue
                    if a * b * c * d == ziel_nach_multiplikation:
                        return (a, b, c, d)
        return None

    #Quiz
    #Wie geben Sie den String 'Hallo' in der Mitte von insgesamt 35 Zeichen aufgefüllt mit ' ! ' aus?
    #1. 'Hallo'.center(35, '!' )
    #2.  center( 'Hallo', 35, '!' )
    #3. 'Hallo' + 35 *'!'
    #4. 35 *'!' + 'Hallo'
    #5. center(35, '!' , 'Hallo')
    #Antwort: 1 ist korrekt

if __name__ == '__main__':
    uebungen_13_03 = Uebungen()
    #print(uebungen_13_03.summe_der_wuerfe(100))
    #print(uebungen_13_03.get_AT_gehalt("ATGCTAGT", 2))
    #print(uebungen_13_03.get_AT_gehalt("AAAA", 0))
    #print(uebungen_13_03.get_AT_gehalt("GGTA", 7))
    print(uebungen_13_03.drogrie_aufgabe())
