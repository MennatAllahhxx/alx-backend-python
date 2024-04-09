#!/usr/bin/env python3
"""
Module contains TestGithubOrgClient class
"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """AI is creating summary for TestGithubOrgClient

    Args:
        unittest (module): a module to create unittests
    """
    @parameterized.expand([
        ("google", {"org": "google"}),
        ("abc", {"org": "abc"})
    ])
    @patch('client.get_json')
    def test_org(self, testorg, expected, mock_read):
        """AI is creating summary for test_org

        Args:
            testorg (str): website
            expected (Dict): org of that value
            mock_read (Dict): json
        """
        mock_read.return_value = expected
        self.assertEqual(GithubOrgClient(testorg).org, expected)
        mock_read.assert_called_once()

if __name__ == "__main__":
    unittest.main()
