#!/usr/bin/env python3
"""
Module contains TestAccessNestedMap and TestGetJson classes
"""
import unittest
import requests
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json


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


class TestGetJson(unittest.TestCase):
    """AI is creating summary for TestGetJson

    Args:
        unittest (module): a module to create unittests
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """AI is creating summary for test_get_json

        Args:
            test_url (str): url to get json for
            test_payload (Dict): payload for that url
        """
        with patch('requests.get') as mock_read:
            mock_read.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock_read.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
