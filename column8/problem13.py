import random
import unittest

# Find the maximum sum of subarray.

class Matrix(object):

  def __init__(self, data):
    self.data = data
    self.height = len(data)
    self.width = 0 if self.height == 0 else len(data[0])
    for row in data:
        assert len(row) == self.width

  def __getitem__(self, key):
    """Retrieve elements or rows or submatrices
    m = Matrix(...)
    m[0][0]  # retrieve element at row 0 col 0
    m[0]     # retrieves row 0
    m[0:2]   # retrieves submatrix of rows 0 to 1
    m[0:2, 0:2]  # retrieves submatrix of rows 0 to 1 and cols 0 to 1
    m[0:2, 1]   # retrieves col 1 (as a list) of rows 0 to 1
    """
    if isinstance(key, tuple):
        rowKey, colKey = key
        result = []
        for row in self.data.__getitem__(rowKey):
            result += [row.__getitem__(colKey)]
        return result
    else:
        return self.data.__getitem__(key)


# Brute force solution O(width ^ 2 * height ^2) -------
def GenSubmatrices(m):
    yield [[]]  # Yield empty matrix
    for rowStart in xrange(m.height):
        for rowEnd in xrange(rowStart + 1, m.height + 1):
            for colStart in xrange(m.width):
                for colEnd in xrange(colStart + 1, m.width + 1):
                    yield m[rowStart:rowEnd, colStart:colEnd]

def GetMaxSubmatrixSum(m):
    currMax = 0
    for submatrix in GenSubmatrices(m):
        submatrixSum = 0
        for row in submatrix:
            submatrixSum += sum(row)
        currMax = max(currMax, submatrixSum)
    return currMax

# height * width ^ 2 based solution -----
def GenSubRows(m):
    yield Matrix([[]])
    for rowStart in xrange(m.height):
        for rowEnd in xrange(rowStart + 1, m.height + 1):
            yield Matrix(m[rowStart:rowEnd])

def GetMaxSubmatrixSumBetter(m):
    currMax = 0
    for subRow in GenSubRows(m):
        acc = 0
        # iterate of over columns
        for i in xrange(subRow.width):
            colSum = sum(subRow[:, i])
            acc = max(acc + colSum, 0)
            currMax = max(currMax, acc)
    return currMax


class MatrixTests(unittest.TestCase):

  def test_MatrixConstruction(self):
    m = Matrix([[1, 2, 3],
                [4, 5, 6]])
    self.assertEqual(m.width, 3)
    self.assertEqual(m.height, 2)

  def test_MatrixConstructionFailBadInput(self):
    with self.assertRaises(AssertionError):
        m = Matrix([[1, 2, 3],
                    [4, 5]])

  def test_MatrixGet(self):
    m = Matrix([[1, 2, 3],
                [4, 5, 6]])
    self.assertEqual(m[0][0], 1)
    self.assertEqual(m[0:1], [[1, 2, 3]])
    self.assertEqual(m[0:1, 0:1], [[1]])
    self.assertEqual(m[0:1, 0:2], [[1, 2]])
    self.assertEqual(m[0:2, 1:2], [[2], [5]])
    self.assertEqual(m[0:2, 1], [2, 5])


class GenSubmatricesTests(unittest.TestCase):

  def test_OneByThree(self):
    m = Matrix([
          [1, 2, 3],
        ])
    submatrices = [submatrix for submatrix in GenSubmatrices(m)]
    self.assertEqual(len(submatrices), 7)
    self.assertEqual(submatrices[0], [[]])
    self.assertEqual(submatrices[1], [[1]])
    self.assertEqual(submatrices[2], [[1, 2]])
    self.assertEqual(submatrices[3], [[1, 2, 3]])
    self.assertEqual(submatrices[4], [[2]])
    self.assertEqual(submatrices[5], [[2, 3]])
    self.assertEqual(submatrices[6], [[3]])

  def test_ThreeByThree(self):
    m = Matrix([
          [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
        ])
    submatrices = [submatrix for submatrix in GenSubmatrices(m)]
    self.assertEqual(len(submatrices), 37)


class GetMaxSubmatrixSumTests(unittest.TestCase):

  def test_AllPositiveTest(self):
    m = Matrix([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]])
    self.assertEqual(GetMaxSubmatrixSum(m), 9)

  def test_SimpleTest(self):
    m = Matrix([[-1, -1, -1],
                [-1,  1, -1],
                [-1, -1, -1]])
    self.assertEqual(GetMaxSubmatrixSum(m), 1)


class GetMaxSubmatrixSumBetterTests(unittest.TestCase):

  def test_AllPositiveTest(self):
    m = Matrix([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]])
    self.assertEqual(GetMaxSubmatrixSumBetter(m), 9)

  def test_SimpleTest(self):
    m = Matrix([[-1, -1, -1],
                [-1,  1, -1],
                [-1, -1, -1]])
    self.assertEqual(GetMaxSubmatrixSumBetter(m), 1)


  def test_RandomTests(self):
    for _ in xrange(20):
        width = random.randint(1, 20)
        height = random.randint(1, 20)
        m = Matrix([[random.randint(-5, 5) for i in xrange(width)] for _ in xrange(height)])
        self.assertEqual(GetMaxSubmatrixSumBetter(m), GetMaxSubmatrixSum(m))


if __name__ == "__main__":
  unittest.main()