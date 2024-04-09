#!/usr/bin/env python3
"""
Module contains TestAccessNestedMap class
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map



class TestAccessNestedMap(unittest.TestCase):
    """AI is creating summary for TestAccessNestedMap

    Args:
        unittest (module): a module to create unittests
    """
    @parameterized.expand([
        ({"a": 1}, "a", 1),
        ({"a": {"b": 2}}, "a", {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """AI is creating summary for test_access_nested_map

        Args:
            nested_map (Mapping): map to be checked
            path (Sequence): a sequence of key repr a path to value
            expected (Any): value of the sequence
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


    @parameterized.expand([
        ({}, "a", KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """AI is creating summary for test_access_nested_map_exception

        Args:
            nested_map (Mapping): map to be checked
            path (Sequence): a sequence of key repr a path to value
            expected (Any): value of the sequence
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()
