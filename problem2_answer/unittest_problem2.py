import unittest
from problem2 import select_num


class Test(unittest.TestCase):
    def test_select_num(self):
        self.assertEqual(select_num(5), f'Output:{3}')
        self.assertEqual(select_num(10), f'Output:{5}')
        self.assertEqual(select_num(15), f'Output:{9}')


if __name__ == '__main__':
    unittest.main()
