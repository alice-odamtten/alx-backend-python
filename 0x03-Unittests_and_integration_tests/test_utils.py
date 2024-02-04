#!/usr/bin/env python3
'''the first unit test for utils.access_nested_map'''
import unittest
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


if __name__ == "__main__":
    unittest.main()
