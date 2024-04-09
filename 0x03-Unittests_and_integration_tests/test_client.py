#!/usr/bin/env python3
"""
Module contains TestGithubOrgClient class
"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock


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

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_read):
        """AI is creating summary for test_public_repos_url

        Args:
            mock_read (Dict): mocked output
        """
        test_payload = {'repos_url':
                        'https://api.github.com/orgs/example/repos'}
        mock_read.return_value = test_payload
        self.assertEqual(GithubOrgClient("google")._public_repos_url,
                         test_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """AI is creating summary for test_public_repos

        Args:
            mock_json (Dict): output
        """
        with patch('client.GithubOrgClient._public_repos_url') as mock_url:
            mock_json.return_value = [{"name": "google"}]
            mock_url.return_value = 'https://api.github.com/orgs/example/repos'
            self.assertEqual(GithubOrgClient("google").public_repos(),
                             ["google"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, test_repo, test_license_key, expected):
        """AI is creating summary for test_has_license

        Args:
            test_repo (Dict[str, Dict]): specifying repo
            test_license_key (str): specifying license key
            expected (bool): True if correct license
        """
        self.assertEqual(GithubOrgClient.has_license(test_repo,
                                                     test_license_key),
                         expected)


if __name__ == "__main__":
    unittest.main()
