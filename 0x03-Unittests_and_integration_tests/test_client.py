#!/usr/bin/env python3
"""test cases for the client module"""

from unittest import TestCase
import unittest
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, MagicMock,  PropertyMock
from fixtures import TEST_PAYLOAD


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


@parameterized_class(
        ('org_payload', 'repos_payload',
         'expected_repos', 'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test cases for the GithubOrgClient class."""

    @classmethod
    def setUpClass(cls):
        """Set up the class"""

        def side(url):
            """Side effect function"""
            repo = []
            mock_response = Mock()
            for payload in TEST_PAYLOAD:
                if url == payload[0]["repos_url"]:
                    repo = payload[1]
                    break
            mock_response.json.return_value = repo
            return mock_response
        cls.get_patcher = patch('requests.get', side_effect=side)
        cls.org_patcher = patch(
                'client.GithubOrgClient.org',
                new_callable=PropertyMock,
                return_value=cls.org_payload)
        cls.org_patcher.start()
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down the class"""
        cls.get_patcher.stop()
        cls.org_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos"""
        test_inst = GithubOrgClient('google/repos')
        self.assertEqual(test_inst.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test the public_repos"""
        test_inst = GithubOrgClient('google/repos')
        self.assertEqual(test_inst.public_repos(license="apache-2.0"),
                         self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
