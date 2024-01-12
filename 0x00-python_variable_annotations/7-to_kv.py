#!/usr/bin/env python3
''' a type-annotated function to_kv that takes a
    string k and an int OR float v as arguments'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' returns a tuple.'''
    tup: Tuple[str, float] = ()
    tup1 = tup + (k,)
    tup2: Tuple[str, float] = tup1 + (float(v * v),)
    return tup2
