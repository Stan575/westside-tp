import unittest

from unit.src.balanced_brackets import is_balanced


class Test_Balanced_Brackets(unittest.TestCase):

    def test_balance_01(self):
        self.assertEqual(is_balanced('{{[([())]]}}'), False)

    def test_balance_02(self):
        self.assertEqual(is_balanced('{{[[(())]]}}'), True)

    def test_balance_03(self):
        self.assertEqual(is_balanced('[]{}()'), True)

    def test_balance_04(self):
        self.assertEqual(is_balanced('[({})]{}()'), True)

    def test_balance_05(self):
        self.assertEqual(is_balanced('({(){}[]})[]'), True)

    def test_balance_06(self):
        self.assertEqual(is_balanced('[]{}())'), False)

    def test_balance_07(self):
        self.assertEqual(is_balanced('[]{(}())'), False)

    def test_balance_08(self):
        self.assertEqual(is_balanced('[{(})]{}()'), False)

    def test_balance_09(self):
        self.assertEqual(is_balanced('[({}][))(]{}()'), False)

    def test_balance_10(self):
        self.assertEqual(is_balanced('[({}][)]{}()'), False)


if __name__ == '__main__':
    unittest.main()
