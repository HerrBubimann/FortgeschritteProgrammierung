from timeit import repeat
from random import randint

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

    @staticmethod
    def insertion_sort(arr):
        n = len(arr)
        if n <= 1:
            return arr

        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    @staticmethod
    def merge(left, right):
        if len(left) == 0:
            return right

        if len(right) == 0:
            return left

        result = []
        index_left = index_right = 0

        while len(result) < len(left) + len(right):
            if left[index_left] <= right[index_right]:
                result.append(left[index_left])
                index_left += 1
            else:
                result.append(right[index_right])
                index_right += 1

            if index_right == len(right):
                result += left[index_left:]
                break

            if index_left == len(left):
                result += right[index_right:]
                break

        return result

    @staticmethod
    def merge_sort(array):
        if len(array) < 2:
            return array

        midpoint = len(array) // 2
        #print(f"links:{array[:midpoint]} rechts:{array[midpoint:]}")

        return Sorter.merge(
            left=Sorter.merge_sort(array[:midpoint]),
            right=Sorter.merge_sort(array[midpoint:]))

    def quick_sort(self, array):
        if len(array) < 2:
            return array

        low, same, high = [], [], []

        pivot = array[randint(0, len(array) - 1)]

        for item in array:
            if item < pivot:
                low.append(item)
            elif item == pivot:
                same.append(item)
            elif item > pivot:
                high.append(item)

        return self.quick_sort(low) + same + self.quick_sort(high)


    def tim_sort(self, array):
        min_run = 32
        n = len(array)

        for i in range(0, n, min_run):
            self.insertion_sort(array, i, min((i + min_run - 1), n - 1))

        size = min_run
        while size < n:
            for start in range(0, n, size * 2):
                midpoint = start + size - 1
                end = min((start + size * 2 - 1), (n - 1))

                merged_array = self.merge(
                    left=array[start:midpoint + 1],
                    right=array[midpoint + 1:end + 1])

                array[start:start + len(merged_array)] = merged_array

            size *= 2

        return array

def run_sorting_algorithm(algorithm, array):
    # Create an instance of Sorter
    sorter = Sorter()

    # Get the actual function from the sorter instance
    if algorithm == "sorted":
        func = sorted
    else:
        func = getattr(sorter, algorithm)

    # The statement to time - we need to pass the function directly
    # We'll use a lambda to avoid import issues
    stmt = f"{algorithm}({array.copy()})"

    # Setup code that imports the Sorter class and gets the function
    setup_code = f"""
from __main__ import Sorter
sorter = Sorter()
{algorithm} = sorter.{algorithm}
"""

    # Execute the code ten different times and return the time
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


if __name__ == "__main__":
    array = [2, 4, 1, 3, 6, 8, 5, 7]
    #run_sorting_algorithm("merge_sort", array.copy())
    sor = Sorter()
    foo = sor.merge_sort(array.copy())
    print(foo)