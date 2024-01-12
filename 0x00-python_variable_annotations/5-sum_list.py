#!/usr/bin/env python3
'''a type-annotated function sum_list which takes
   a list input_list of floats as argument'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''returns their sum as a float.'''
    total: float = 0.0
    for num in input_list:
        total += num
    return total
