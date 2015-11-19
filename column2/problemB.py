import random
import unittest


def GetSource(index, length, rotationAmount):
    return (index + rotationAmount) % length


def GetDest(index, length, rotationAmount):
    return (index - rotationAmount) % length


def Rotate(vector, rotationAmount):
    """Implementation for problem 3
    Rotate a vector by using a single swap space.
    """
    if rotationAmount == 0:
        # Special case performance enhancement. If we don't do this we would perform
        # iterate through the vector swapping elements with themselves.
        return
    else:
        num_swaps = 0
        i = 0
        while num_swaps < len(vector):
            num_swaps += DoRotationCycle(vector, rotationAmount, i)
            i += 1


def DoRotationCycle(vector, rotationAmount, start_index):
    num_rotations = 1
    swap = vector[start_index]
    vector[start_index] = vector[GetSource(start_index, len(vector), rotationAmount)]
    i = GetDest(start_index, len(vector), rotationAmount)
    while i != start_index:
        vector[i], swap = swap, vector[i]
        i = GetDest(i, len(vector), rotationAmount)
        num_rotations += 1
    return num_rotations


def RotatedCopy(vector, rotationAmount):
    return vector[rotationAmount:] + vector[:rotationAmount]


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


class RotatedCopyTests(unittest.TestCase):

    def test_SimpleTest(self):
        data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.assertEqual(RotatedCopy(data, 2),
                         ['c', 'd', 'e', 'f', 'g', 'h', 'a', 'b'])


class RotateTests(unittest.TestCase):

    def test_NoRotate(self):
        data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        answer = list(data)
        Rotate(data, 0)
        self.assertEqual(data, answer)

    def test_ArrayOf8Rotate2(self):
        data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        answer = RotatedCopy(data, 2)
        Rotate(data, 2)
        self.assertEqual(data, answer)

    def test_ArrayOf6Rotate4(self):
        data = ['a', 'b', 'c', 'd', 'e', 'f']
        answer = RotatedCopy(data, 4)
        Rotate(data, 4)
        self.assertEqual(data, answer)

    def test_ArrayOf8Rotate6(self):
        data = ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'i']
        answer = RotatedCopy(data, 6)
        Rotate(data, 6)
        self.assertEqual(data, answer)

    def test_Random(self):
        for _ in range(1000):
            data = [random.randrange(10) for i in range(random.randrange(1, 100))]
            original = list(data)
            rotationAmount = random.randrange(len(data))
            answer = RotatedCopy(data, rotationAmount)
            Rotate(data, rotationAmount)
            self.assertEqual(data, answer,
                             msg="Fail length: %i, rotation: %i, original: %s" % (
                                len(data), rotationAmount, original))

if __name__ == '__main__':
    unittest.main()
