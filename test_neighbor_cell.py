import unittest
from neighbor_cell_m import neighbor_cell

class NeighborCellTest(unittest.TestCase):

    def test_neighbor_cell_1(self):
        result = neighbor_cell(1)
        self.assertListEqual(result, [0, 2, 5])

    def test_neighbor_cell_2(self):
        result = neighbor_cell(2)
        self.assertListEqual(result, [1, 3, 6])

    def test_neighbor_cell_3(self):
        result = neighbor_cell(3)
        self.assertListEqual(result, [2, 7])

    def test_neighbor_cell_4(self):
        result = neighbor_cell(4)
        self.assertListEqual(result, [5, 0, 8])

    def test_neighbor_cell_5(self):
        result = neighbor_cell(5)
        self.assertListEqual(result, [4, 6, 1, 9])

    def test_neighbor_cell_6(self):
        result = neighbor_cell(6)
        self.assertListEqual(result, [5, 7, 2, 10])

    def test_neighbor_cell_7(self):
        result = neighbor_cell(7)
        self.assertListEqual(result, [6, 3, 11])

    def test_neighbor_cell_8(self):
        result = neighbor_cell(8)
        self.assertListEqual(result, [9, 4, 12])

    def test_neighbor_cell_9(self):
        result = neighbor_cell(9)
        self.assertListEqual(result, [8, 10, 5, 13])

    def test_neighbor_cell_10(self):
        result = neighbor_cell(10)
        self.assertListEqual(result, [9, 11, 6, 14])

    def test_neighbor_cell_11(self):
        result = neighbor_cell(11)
        self.assertListEqual(result, [10, 7, 15])

    def test_neighbor_cell_12(self):
        result = neighbor_cell(12)
        self.assertListEqual(result, [13, 8])

    def test_neighbor_cell_13(self):
        result = neighbor_cell(13)
        self.assertListEqual(result, [12, 14, 9])

    def test_neighbor_cell_14(self):
        result = neighbor_cell(14)
        self.assertListEqual(result, [13, 15, 10])

    def test_neighbor_cell_15(self):
        result = neighbor_cell(15)
        self.assertListEqual(result, [14, 11])



if __name__ == '__main__':
    unittest.main()
