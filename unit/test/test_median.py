import unittest
from unit.src.medain import median
from unit.src.balanced_brackets import is_balanced


class TestMedian(unittest.TestCase):

    def test_median_empty_list(self):
        self.assertIsNone(median([]))

    def test_median_list_single_element(self):
        self.assertEqual(median([2]), 2)

class Test_Balanced_Bracets(unittest.TestCase):

    def test_balance(self):
        self.assertEqual(is_balanced('{{[([())]]}}'), False)

    def test_balance2(self):
        self.assertEqual(is_balanced('{{[[(())]]}}'), True)
        
if __name__ == '__main__':
    unittest.main()
