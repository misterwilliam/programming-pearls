import random
import unittest


def HasElement(vector, element):
    # It seems that binary search is not hard to write correctly anymore with Python
    vector.sort()

    def _BinarySearch(begin, end, element):
        if begin == end:
            return False
        elif end - begin == 1:
            return vector[begin] == element
        else:
            midpoint = begin + (end - begin) // 2
            midpointValue = vector[midpoint]
            if midpointValue == element:
                return True
            elif midpointValue > element:
                return _BinarySearch(begin, midpoint, element)
            else:
                return _BinarySearch(midpoint, end, element)

    return _BinarySearch(0, len(vector), element)


class HasElementTests(unittest.TestCase):

    def test_EmptyArray(self):
        self.assertEqual(HasElement([], 1), False)

    def test_SingleElementArrayWithElement(self):
        self.assertEqual(HasElement([1], 1), True)

    def test_SingleElementArrayWithoutElement(self):
        self.assertEqual(HasElement([1], 0), False)

    def test_LongerArrayWithElement(self):
        self.assertEqual(HasElement([1, 4, 6, 9, 11, 15], 6), True)

    def test_Random(self):
        for _ in range(500):
            data = [random.randrange(50) for _ in range(random.randrange(100))]
            element = random.randrange(50)
            self.assertEqual(HasElement(data, element), element in data)


if __name__ == '__main__':
    unittest.main()
