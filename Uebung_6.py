from timeit import repeat

class Sorter:
    @staticmethod
    def bubble_sort(arr):
        for i in range(len(arr)):
            is_sorted = True
            for n in range(len(arr) - i - 1):
                if arr[n] > arr[n + 1]:
                    arr[n], arr[n + 1] = arr[n + 1], arr[n]
                    is_sorted = False
            if is_sorted:
                break
        return arr

def main():
    algorithm = "bubble"
    setup_code = """
from __main__ import Sorter
arr = [2, 8, 4, 6, 2, 7]
    """
    stmt_code = "Sorter.bubble_sort(arr)"
    times = repeat(setup=setup_code, stmt=stmt_code, repeat=3, number=10)
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")

if __name__ == "__main__":
    main()