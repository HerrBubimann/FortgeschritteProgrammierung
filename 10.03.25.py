class Uebungen:
    @staticmethod
    def durchschnitt_berechnen(zahlen: []):
        int_zahlgesamt = sum(zahlen)
        dbl_durchschnitt = float(int_zahlgesamt) / len(zahlen)
        return dbl_durchschnitt

    @staticmethod
    def zahlen_vergleichen(zahl1: int, zahl2: int):
        if zahl1 > zahl2:
            return f"Die Zahl {zahl1} ist größer als die Zahl {zahl2}"
        elif zahl1 < zahl2:
            return f"Die Zahl {zahl2} ist größer als die Zahl {zahl1}"
        else:
            return f"Die Zahlen {zahl1} und {zahl2} sind gleich groß"

    @staticmethod
    def zahlen_teilen(zahl1: int, zahl2 :int):
        ergebnis = 0
        if zahl1 == 0 and zahl2 == 0:
            ergebnis = "Division nicht möglich: Beide Zahlen sind 0."

        if zahl1 > zahl2:
            if zahl2 !=0:
                ergebnis = zahl1 / zahl2
            else:
                ergebnis = "Division nicht möglich: Beide Zahlen sind 0."
        elif zahl1 > zahl2:
            if zahl1 !=0:
                ergebnis = zahl2 / zahl1
            else:
                ergebnis = "Division nicht möglich: Beide Zahlen sind 0."
        elif zahl1 == zahl2:
            ergebnis = 1
        else:
            ergebnis = "Fehler"

    @staticmethod
    def schleife_uebung():
        wert = 0
        for i in range(2, 101, 2):
            print(i, end=" ")
            wert = wert + i
        print()
        print(wert)
        wert = 0
        zaehler = 0
        while zaehler != 100:
            zaehler += 2
            print(zaehler, end=" ")
            wert += zaehler
        print()
        print(wert)

    @staticmethod
    def fahreneinheit_zu_celsius(gradzahl_fahrenheit: float):
        return round((gradzahl_fahrenheit-32) * 5/9, 2)

if __name__ == '__main__':
    uebungen_10_03 = Uebungen()
    #arr = [5, 9, 4, 17, 3]
    #dbl_durschnitt = uebungen_10_03.durchschnitt_berechnen(arr)
    #print(f"{dbl_durschnitt:.2f}")
    #zahl1 = int(input("Geben Sie eine Zahl ein zu vergleichen"))
    #zahl2 = int(input("Geben Sie eine Zahl ein zu vergleichen"))
    #print(uebungen_10_03.zahlen_vergleichen(zahl1,zahl2))
    #zahl1 = int(input("Geben Sie eine Zahl ein zum teilen an"))
    #zahl2 = int(input("Geben Sie eine Zahl ein zum teilen an"))
    #print(f"{uebungen_10_03.zahlen_teilen(zahl1, zahl2)}")
    print(f"{uebungen_10_03.fahreneinheit_zu_celsius(90)}")


