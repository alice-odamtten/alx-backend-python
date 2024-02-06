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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_url):
        '''to test get_json with public repos'''
        mock_payload = [{'name': 'repo1'}, {'name': 'repo2'}]
        mock_get_url.return_value = mock_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_property:
            mock_property.return_value = 'test url'
            test_list = GithubOrgClient('random name').public_repos()

        self.assertEqual(['repo1', 'repo2'], test_list)
        mock_get_url.assert_called_once_with('test url')

    @parameterized.expand([
         ({"name": "repo1", "license": {"key": "my_license"}},
          "my_license", True),
         ({"name": "repo2", "license": {"key": "other_license"}},
          "my_license", False)
         ])
    def test_has_license(self, repo, lincense, res):
        '''test license'''
        self.assertEqual(GithubOrgClient.has_license(repo, lincense), res)


if __name__ == '__main__':
    unittest.main()
