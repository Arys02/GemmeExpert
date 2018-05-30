import DataSetFactory

import unittest

class TestStringMethods(unittest.TestCase):
    def test_string_a(self):
        self.assertEqual(DataSetFactory.test_1(), "lolmdr")


if __name__ == '__main__':
    unittest.main()