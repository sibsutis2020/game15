import unittest
from neighbor_cell_m import neighbor_cell

class TestNeighborCell(unittest.TestCase):

    def test_neighbor_cell(self):
        result = neighbor_cell(2)
        self.assertListEqual(result, [1, 3, 6])

if __name__ == '__main__':
    unittest.main()
