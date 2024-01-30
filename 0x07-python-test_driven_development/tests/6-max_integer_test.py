#!/usr/bin/python3
"""Module unit_test for the max_integer fct
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Unittest for max_integer([..])"""

    def test_max_integer_basic(self):
        # Test with a list of integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_integer_empty(self):
        # Test with an empty list
        self.assertIsNone(max_integer([]))

    def test_max_integer_single_element(self):
        # Test with a list containing a single element
        self.assertEqual(max_integer([5]), 5)

    def test_max_integer_negative(self):
        # Test with a list containing negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_integer_mixed(self):
        # Test with a list containing both positive and negative integers
        self.assertEqual(max_integer([-1, 0, 3, -4]), 3)

    def test_max_integer_repeated(self):
        # Test with a list containing repeated numbers
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_max_integer_large_numbers(self):
        # Test with large numbers
        self.assertEqual(max_integer([100000, 99999, 200000]), 200000)

    def test_max_integer_large_list(self):
        # Test with a large list
        large_list = list(range(1000))  # list from 0 to 999
        self.assertEqual(max_integer(large_list), 999)

    def test_max_integer_with_floats(self):
        # Test with a list containing floats
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)

    def test_max_integer_with_all_same_elements(self):
        # Test with a list where all elements are the same
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_max_integer_with_non_numeric(self):
        # Test with a list containing non-numeric values(should raise an error)
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'three', 4])

    def test_max_integer_with_none(self):
        # Test with a list containing None (should raise an error)
        with self.assertRaises(TypeError):
            max_integer([1, None, 3])

    def test_max_integer_empty(self):
        # Test with an empty list
        self.assertIsNone(max_integer([]))

    def test_max_integer_huge_list(self):
        # Test with a very large list
        huge_list = list(range(1000000))  # list from 0 to 999999
        self.assertEqual(max_integer(huge_list), 999999)

    def test_max_integer_list_of_strings(self):
        # Test with a list of strings (should raise an error)
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c"])

    def test_max_integer_list_of_booleans(self):
        # Test with a list of booleans
        # Assuming the function treats booleans as integers (False=0, True=1)
        self.assertEqual(max_integer([True, False, True]), True)
