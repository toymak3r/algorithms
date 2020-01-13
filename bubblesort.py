# bubble sort
from random import randint
import time
import unittest


class BubbleSort:

    MAX_RANGE_INT = 0  # define style

    def __init__(self, max_range_int=10000000):
        self.MAX_RANGE_INT = max_range_int

    def sort(self, numbers) -> list:
        changed = True
        while changed:
            changed = False
            for x in range(len(numbers)-1, 0, -1):
                temp = numbers[x]
                if numbers[x] < numbers[x-1]:
                    numbers[x] = numbers[x-1]
                    numbers[x-1] = temp
                    changed = True

        return numbers


class BubbleSortTest(unittest.TestCase):
    bs = BubbleSort()
    n_tests = 10
    n_elements = 10
    numbers = []

    def setUp(self):
        self.set_rand_numbers()

    def setDown(self):
        self.numbers = []

    def set_rand_numbers(self):
        self.numbers = [randint(1, randint(1, self.bs.MAX_RANGE_INT))
                        for _ in range(self.n_elements)]

    def test(self):
        sorted_numbers = self.numbers
        sorted_numbers.sort()
        result = self.bs.sort(self.numbers)

        print("List Numbers to be used: {}".format(self.numbers))
        print("sorted by sort() python: {}".format(sorted_numbers))
        print("sorted by function: {}".format(result))
        self.assertEqual(self.bs.sort(self.numbers), sorted_numbers)

    @staticmethod
    def performance():
        print("Using Own BubbleSort Function: \n")
        numbers = [2, 3, 10, 40, 4, 1, 20]
        b = BubbleSort()
        start_time = time.time()
        print(b.sort(numbers))
        print("--- %s seconds ---" % (time.time() - start_time)+"\n")

        print("Using Sort() Python Function: \n")
        numbers = [2, 3, 10, 40, 4, 1, 20]
        start_time = time.time()
        numbers.sort()
        print(numbers)
        print("--- %s seconds ---" % (time.time() - start_time)+"\n")
