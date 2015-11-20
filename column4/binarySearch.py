import random
import unittest


def HasElement(vector, element):
    # It seems that binary search is not hard to write correctly anymore with Python
    vector.sort()
    if len(vector) == 0:
        return False
    elif len(vector) == 1:
        return vector[0] == element
    else:
        midpoint = len(vector) // 2
        return (HasElement(vector[:midpoint], element) or
                HasElement(vector[midpoint:], element))


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
