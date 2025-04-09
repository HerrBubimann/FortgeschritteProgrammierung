import time

class HalfIterator:
    def __init__(self, array):
        self.array = array
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.index < len(self.array):
                self.index += 1
                return self.array[self.index - 1] / 2
            else:
                raise HalfIterator("Außerhalb des Wertebereichs")
        except Exception as e:
            raise HalfIterator(f"Fehler beim Iterieren: {str(e)}")

class ReversIterator:
    def __init__(self, array):
        self.array = array
        self.index = len(array) - 1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.index >= 0:
                print("print in if")
                index = self.index
                self.index -= 1
                time.sleep(1)
                return self.array[index]
            else:
                raise StopIteration
        except Exception as e:
            raise self.ReversIteratorError(f"Fehler beim Iterieren: {str(e)}")

    class ReversIteratorError(Exception):
        pass

if __name__ == "__main__":
    for test in ReversIterator([1,2,3]):
        print(test)