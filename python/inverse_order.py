import time
import unittest


def inverse(word):
    n = int(len(word))
    i = 1
    new_word = ''
    while (i <= n):
        new_word += word[n-i]
        i += 1
    return new_word


def inverse_ver_two(word):
    n = int(len(word)-1)
    new_word = ''
    for i in range(0, n+1):
        new_word += word[n-i]
    return new_word


class InverseOrderTests(unittest.TestCase):

    def test(self):
        word = 'house'
        print("Word used: {}".format(word))
        print("Correct inversion: {}".format('esuoh'))
        self.assertEqual(inverse(word), 'esuoh')

    @staticmethod
    def performance():
        print("Using Own Reverse Function: \n")
        start_time = time.time()
        print(inverse("casa"))
        print("--- %s seconds ---" % (time.time() - start_time)+"\n")

        print("Using Own Reverse Function Version 2: \n")
        start_time = time.time()
        print(inverse_ver_two("casa"))
        print("--- %s seconds ---" % (time.time() - start_time)+"\n")

        print("Using Python's Reverse Function: \n")
        start_time = time.time()
        print(("casa")[::-1])
        print("--- %s seconds ---" % (time.time() - start_time)+"\n")
