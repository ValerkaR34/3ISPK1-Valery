import unittest
from lab import fdd

class TestNumber(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(fdd("00300"),"2", "ошибочка вышла")


if __name__ =='__main__':
    unittest.main()