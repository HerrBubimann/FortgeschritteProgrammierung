class Demo():
    def __init__(self):
        self.pub = 'Ich bin öffentlich'
        self._prot = 'Ich bin schwach privat'
        # nicht ganz vergleichbar mit protected
        self.__priv = 'Ich bin stark privat'
        # wird erreicht über Namensverstuemmelung
        self.__notpriv__ = 'Ich bin nicht privat'
        # keine Namensverstuemmelung


class Vererbung(Demo):
    def __init__(self):
        super().__init__()
        print(self.pub)
        print(self._prot)
        print(self.__priv)
        print(self.__notpriv__)


def main():
    testObjekt = Demo()
    print(dir(testObjekt), '\n')

    print(testObjekt.pub)
    testObjekt.pub = \
        'Man kann meinen Wert ändern und das ist gut so'
    print(testObjekt.pub, '\n')

    print(testObjekt._prot)
    testObjekt._prot = \
        'Man kann meinen Wert von außen ändern,' + \
        ' sollte es aber nicht tun'
    print(testObjekt._prot, '\n')

    print(testObjekt.__notpriv__)
    testObjekt.__notpriv__ = \
        'Ich bin speziell für Python'
    print(testObjekt.__notpriv__, '\n')

    test = Vererbung()
    try:
        print(test)
    except Exception as e:
        print(e)

    print(dir(test))
    print(dir(testObjekt))
    # print(testObjekt.__priv,'\n') # Fehlermeldung

    # testObjekt = Vererbung()


if __name__ == '__main__':
    main()
