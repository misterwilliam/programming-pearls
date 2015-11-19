import unittest


def GetSource(index, length, rotationAmount):
    retVal = index + rotationAmount
    if retVal < length:
        return retVal
    else:
        return retVal - length


def GetDest(index, length, rotationAmount):
    retVal = index - rotationAmount
    if retVal >= 0:
        return retVal
    else:
        return retVal + length


def Rotate(vector, rotationAmount):
    swap = vector[0]
    vector[0] = GetSource(0, len(vector), rotationAmount)
    i = GetDest(0, len(vector), rotationAmount)
    while i != 0:
        vector[i], swap = swap, vector[i]
        i = GetDest(i, len(vector), rotationAmount)


class GetSourceTests(unittest.TestCase):

    def test_ArrayOfSize6(self):
        self.assertEqual(GetSource(0, 5, 3), 3)
        self.assertEqual(GetSource(1, 5, 3), 4)
        self.assertEqual(GetSource(2, 5, 3), 0)
        self.assertEqual(GetSource(3, 5, 3), 1)
        self.assertEqual(GetSource(4, 5, 3), 2)


class GetDestTests(unittest.TestCase):

    def test_ArrayOfSize5(self):
        self.assertEqual(GetDest(0, 5, 3), 2)
        self.assertEqual(GetDest(1, 5, 3), 3)
        self.assertEqual(GetDest(2, 5, 3), 4)
        self.assertEqual(GetDest(3, 5, 3), 0)
        self.assertEqual(GetDest(4, 5, 3), 1)


class RotateTests(unittest.TestCase):

    def test_basic(self):
        data = [0, 1, 2, 3, 4, 5, 6]
        Rotate(data, 3)
        self.assertEqual(data, [3, 4, 5, 6, 0, 1, 2])


if __name__ == '__main__':
    unittest.main()
