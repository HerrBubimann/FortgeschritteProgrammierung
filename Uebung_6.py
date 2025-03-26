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

    @staticmethod
    def insertion_sort(arr):
        n = len(arr)
        if n <= 1:
            return

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

    def merge_sort(self,array):
        if len(array) < 2:
            return array

        midpoint = len(array) // 2
        print(f"1:{array[:midpoint]} 2:{array[midpoint:]}")
        return self.merge(
            left=self.merge_sort(array[:midpoint]),
            right=self.merge_sort(array[midpoint:]))

def main():
    '''    algorithm = "bubble"
        setup_code = """
    from __main__ import Sorter
    arr = [2, 8, 4, 6, 2, 7]
        """
        stmt_code = "Sorter.bubble_sort(arr)"
        times = repeat(setup=setup_code, stmt=stmt_code, repeat=3, number=10)
        print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")'''
    sor = Sorter()
    array = [2,4,1,3,6,8,5,7]
    foo = sor.merge_sort(array)
    print(foo)

if __name__ == "__main__":
    main()