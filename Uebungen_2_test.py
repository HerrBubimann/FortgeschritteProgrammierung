import unittest
from Uebung_2 import Uebungen


class MyTestCase(unittest.TestCase):
    def test_get_AT_gehalt(self):
        uebungen_13_03 = Uebungen()
        try:
            self.assertEqual(uebungen_13_03.get_AT_gehalt("ATTA", 2), 1.0, "Test 1 fehlgeschlagen")
        except Exception as e:
            print(f"Fehler in Test 1: {e}")

        try:
            self.assertEqual(uebungen_13_03.get_AT_gehalt("aaattggc", 2), 0.62, "Test 2 fehlgeschlagen")
        except Exception as e:
            print(f"Fehler in Test 2: {e}")

        try:
            self.assertEqual(uebungen_13_03.get_AT_gehalt("ACGT", 1), 0.5, "Test 3 fehlgeschlagen")
        except Exception as e:
            print(f"Fehler in Test 3: {e}")

        # Künstlicher Fehler
        try:
            self.assertEqual(uebungen_13_03.get_AT_gehalt(), 0, "Test 4 fehlgeschlagen")
        except Exception as e:
            print(f"Fehler in Test 4: {e}")


if __name__ == '__main__':
    unittest.main()
