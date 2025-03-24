class Bruch:
    def __init__(self, zaehler=0, nenner=1):
        if nenner == 0:
            raise ValueError("Nenner darf nicht null sein.")
        self.zaehler = zaehler
        self.nenner = nenner
        self.kuerzen()

    def kuerzen(self):
        teiler = self.groeßte_gemeinsame_teiler(self.zaehler, self.nenner)
        self.zaehler //= teiler
        self.nenner //= teiler
        if self.nenner < 0:
            self.zaehler *= -1
            self.nenner *= -1

    @staticmethod
    def groeßte_gemeinsame_teiler(zaehler, nenner):
        while nenner:
            zaehler, nenner = nenner, zaehler % nenner
        return abs(zaehler)

    def __str__(self):
        return f"{self.zaehler}/{self.nenner}"

    def to_string(self):
        print(f"{self.zaehler}/{self.nenner}")

    def __add__(self, bruch_addieren):
        neuer_zaehler = self.zaehler * bruch_addieren.nenner + bruch_addieren.zaehler * self.nenner
        neuer_nenner = self.nenner * bruch_addieren.nenner
        return Bruch(neuer_zaehler, neuer_nenner)

    def add(self, bruch_addieren):
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

        bruch3_add = bruch1.add(bruch2)
        bruch4_add = bruch2.add(bruch1)
        bruch_5_2 = Bruch()
        bruch3 = bruch1 + bruch2
        bruch3.to_string()
        print(bruch3)
        print(bruch3_add)

        bruch4 = Bruch(1, 3)
        print(bruch4.float_bruch())

if __name__ == '__main__':
    Bruch.main()