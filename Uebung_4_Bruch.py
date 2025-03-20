
class Bruch:
    def __init__(self, zaehler, nenner=1):
        if nenner == 0:
            raise ValueError("Nenner darf nicht null sein.")
        self.zaehler = zaehler
        self.nenner = nenner
        self.kuerzen()

    def kuerzen(self):
        teiler = self.ggT(self.zaehler, self.nenner)
        self.zaehler //= teiler
        self.nenner //= teiler
        if self.nenner < 0:
            self.zaehler *= -1
            self.nenner *= -1

    def ggT(self, zaehler, nenner):
        while nenner:
            zaehler, nenner = nenner, zaehler % nenner
        return abs(zaehler)

    def __str__(self):
        return f"{self.zaehler}/{self.nenner}"

    def __add__(self, bruch_addieren):
        neuer_zaehler = self.zaehler * bruch_addieren.nenner + bruch_addieren.zaehler * self.nenner
        neuer_nenner = self.nenner * bruch_addieren.nenner
        return Bruch(neuer_zaehler, neuer_nenner)

    def float_bruch(self):
        return self.zaehler / self.nenner

    @staticmethod
    def main():
        bruch1 = Bruch(3, 4)
        bruch2 = Bruch(1, 2)
        print(bruch1)
        print(bruch2)

        bruch3 = bruch1.__add__(bruch2)
        print(bruch3)

        bruch4 = Bruch(1, 3)
        print(bruch4.float_bruch())

        bruch1.__str__()
        bruch2.__str__()
        bruch3.__str__()
        bruch4.__str__()



if __name__ == '__main__':
    Bruch.main()