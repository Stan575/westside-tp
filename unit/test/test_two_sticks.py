import unittest
from unit.src.two_sticks import solution


class TestTwoSticks(unittest.TestCase):

    def test_two_sticks_second_larger_that_first(self):
        self.assertEqual(solution(10, 21), 7)


if __name__ == '__main__':
    unittest.main()