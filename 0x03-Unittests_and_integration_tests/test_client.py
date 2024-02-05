#!/usr/bin/env python3
"""test cases for the client module"""

from unittest import TestCase
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, Mock, MagicMock,  PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    '''implement the test_org method.'''

    @parameterized.expand(["google", "abc"])
    @patch("client.get_json")
    def test_org(self, url, mock_get_json):
        """to test org"""
        res = GithubOrgClient(url)
        res.org
        mock_get_json.assert_called_once_with(
                res.ORG_URL.format(org=url)
                )

    @patch('client.GithubOrgClient.org', return_value={"repos_url": 'url'})
    def test_public_repos_url(self, mock_org):
        '''test with context'''
        git_org = GithubOrgClient('test_org_url')
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_property:
            mock_property.return_value = mock_org.return_value["repos_url"]
            test_url = git_org._public_repos_url

        self.assertEqual('url', test_url)
