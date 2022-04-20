import unittest

from unit.src.medain import median


class TestMedian(unittest.TestCase):

    def test_median_empty_list(self):
        self.assertIsNone(median([]))

    def test_median_list_single_element(self):
        self.assertEqual(median([2]), 2)


if __name__ == '__main__':
    unittest.main()
