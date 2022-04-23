import unittest

from unit.src.medain import median


class TestMedian(unittest.TestCase):


    def test_median_empty_list(self):
        self.assertEqual(median([]), None)

    def test_median_list_single_element_two(self):
        self.assertEqual(median([2]), 2)

    def test_median_list_single_element_zero(self):
        self.assertEqual(median([0]), 0)

    def test_median_list_single_element_minus_two(self):
        self.assertEqual(median([-2]), -2)

    def test_median_list_two_elements_two_four(self):
        self.assertEqual(median([2, 4]), 3)

    def test_median_list_two_elements_five_five(self):
        self.assertEqual(median([5, 5]), 5)

    def test_median_list_two_elements_five_minusfive(self):
        self.assertEqual(median([-5, 5]), 0)

    def test_median_list_two_elements_two_three(self):
        self.assertEqual(median([2, 3]), 2.5)

    def test_median_list_two_elements_minustwo_minusthree(self):
        self.assertEqual(median([-2, -3]), -2.5)

    def test_median_list_two_elements_float_int(self):
        self.assertEqual(median([2.456, 3]), 2.728)

    def test_median_list_four_elements(self):
        self.assertEqual(median([9, 1, 5, 2]), 3.5)

    def test_median_list_five_elements(self):
        self.assertEqual(median([8, 5, 2, 1, 9]), 5)

    def test_median_list_bool_true_true(self):
        self.assertEqual(median([True, True]), 1)

    def test_median_list_bool_true_false(self):
        self.assertEqual(median([True, False]), 0.5)

    def test_median_list_bool_false_false(self):
        self.assertEqual(median([False, False]), 0)

    def test_median_list_bool_true_true_true(self):
        self.assertEqual(median([True, True, True]), 1)



if __name__ == '__main__':
    unittest.main()
