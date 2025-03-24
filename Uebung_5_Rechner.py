import  math

class Rechner:
    def __init__(self, wert):
        self.wert = wert

    def __add__(self, wert_add):
        if isinstance(wert_add, (int, float)):
            return Rechner(self.wert + wert_add)
        elif isinstance(wert_add, Rechner):
            return Rechner(self.wert + wert_add.wert)
        else:
            raise TypeError("Nur Zahlen sind erlaubt oder Rechnerklassen sind erlaubt")

    def __sub__(self, wert_sub):
        if isinstance(wert_sub, (int, float)):
            return Rechner(self.wert - wert_sub)
        elif isinstance(wert_sub, Rechner):
            return Rechner(self.wert - wert_sub.wert)
        else:
            raise TypeError("Nur Zahlen sind erlaubt oder Rechnerklassen sind erlaubt")

    def __mul__(self, wert_mutli):
        if isinstance(wert_mutli, (int, float)):
            return Rechner(self.wert * wert_mutli)
        elif isinstance(wert_mutli, Rechner):
            return Rechner(self.wert * wert_mutli.wert)
        else:
            raise TypeError("Nur Zahlen sind erlaubt oder Rechnerklassen sind erlaubt")

    def __truediv__(self, wert_zum_teilen):
        if isinstance(wert_zum_teilen, (int, float)):
            if wert_zum_teilen == 0:
                raise ZeroDivisionError("Division durch Null nicht erlaubt")
            return Rechner(self.wert / wert_zum_teilen)
        elif isinstance(wert_zum_teilen, Rechner):
            if wert_zum_teilen.wert == 0:
                raise ZeroDivisionError("Division durch Null nicht erlaubt")
            return Rechner(self.wert / wert_zum_teilen.wert)
        else:
            raise TypeError("Nur Zahlen sind erlaubt oder Rechnerklassen sind erlaubt")

    def __str__(self):
        return str(self.wert)

class ProfiRechner(Rechner):
    def __init__(self, wert):
        super().__init__(wert)

    @staticmethod
    def fakultaet(fakultaet_wert):
        if not isinstance(fakultaet_wert, int):
            raise TypeError("Nur ganz Zahlen sind erlaubt")
        if fakultaet_wert < 0:
            raise ValueError("Nur Positive Zahlen sind erlaut")
        if fakultaet_wert == 0:
            return 1
        ergebnis = 1
        for i in range(1, fakultaet_wert + 1):
            ergebnis *= i
        return ergebnis

    def __pow__(self, exponent_wert):
        if isinstance(exponent_wert, (int, float)):
            if self.wert == 0 and exponent_wert < 0:
                raise ValueError("Es kann nicht mit 0 potenziert werden")
            return ProfiRechner(self.wert ** exponent_wert)
        else:
            raise TypeError("Exponent muss eine Zahl sein")


class GeoRechner(Rechner):
    def __init__(self, wert):
        super().__init__(wert)

    def flaeche_rechteck(self, a, b):
        return a * b if isinstance(self.wert, (int, float)) else a * b

    def umfang_rechteck(self, a, b):
        return (a + b) * 2

    def flaeche_kreis(self, radius):
        return math.pi * (radius ** 2)

def main():
    rechner_1 = Rechner(10)
    rechner_2 = Rechner(5)

    print("Mit Klasse")
    print(f"Addition: {rechner_1 + rechner_2}")
    print(f"Subtraktion: {rechner_1 - rechner_2}")
    print(f"Multiplikation: {rechner_1 * rechner_2}")
    print(f"Division: {rechner_1 / rechner_2}")
    print("\n")
    
    wert = 7
    print("ohne Klasse")
    print(f"Addition: {rechner_1 + wert}")
    print(f"Subtraktion: {rechner_1 - wert}")
    print(f"Multiplikation: {rechner_1 * wert}")
    print(f"Division: {rechner_1 / wert}")
    print("\n")

    print()
    profi_rechner_1 = ProfiRechner(2)
    print(f"Fakultät von 5: {profi_rechner_1.fakultaet(5)}")
    print(f"Potenz: {profi_rechner_1.wert **wert}")
    print("\n")

    geo_rechner_1 = GeoRechner(4)
    print(f"Fläche Rechteck: {geo_rechner_1.flaeche_rechteck(4,2)}")
    print(f"Umfang Rechteck: {geo_rechner_1.umfang_rechteck(4,2)}")
    print(f"Fläche Kreis: {geo_rechner_1.flaeche_kreis(6)}")

if __name__ == '__main__':
    main()