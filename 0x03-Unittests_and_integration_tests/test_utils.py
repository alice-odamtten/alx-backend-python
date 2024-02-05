#!/usr/bin/env python3
'''the first unit test for utils.access_nested_map'''
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
utils = __import__('utils')


class TestAccessNestedMap(unittest.TestCase):
    '''class that inherits from unittest.TestCase'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        '''method to test that the method returns what it is supposed to.'''

        result = utils.access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(self, nst_map, path, expected_result):
        if expected_result == KeyError:
            with self.assertRaises(KeyError):
                utils.access_nested_map(nst_map, path)
        else:
            result = utils.access_nested_map(nst_map, path)
            self.assertEqual(result, expected_result)


class TestGetJson(unittest.TestCase):
    '''class and implement the TestGetJson.test_get_json method'''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch("requests.get")
    def test_get_json(self, url, payload, mock_request_get):
        mock_json = MagicMock(return_value=payload)
        response = MagicMock()
        response.json = mock_json
        mock_request_get.return_value = response

        result = utils.get_json(url)

        mock_request_get.assert_called_once_with(url)
        self.assertEqual(result, payload)


if __name__ == "__main__":
    unittest.main()
