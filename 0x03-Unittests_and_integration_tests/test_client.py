#!/usr/bin/env python3
"""test cases for the client module"""

from unittest import TestCase
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, Mock, MagicMock


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
