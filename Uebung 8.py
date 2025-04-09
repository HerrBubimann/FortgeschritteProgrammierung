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