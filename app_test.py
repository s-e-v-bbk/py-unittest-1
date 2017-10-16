import app_main
import unittest
import math

print(app_main.my_little_function(5))


class TestStrings(unittest.TestCase):
    def test_passing_10(self):
        # should return 20 (10 x 2)
        self.assertEqual(app_main.my_little_function(10), 20)
    def test_passing_20(self):
        # should return 40 (20 x 2)
        self.assertEqual(app_main.my_little_function(20), 40)
    def test_passing_number(self):
        # should test if it's a number..
        self.assertEqual(math.isnan(app_main.my_little_function(30)), False)


unittest.main()
