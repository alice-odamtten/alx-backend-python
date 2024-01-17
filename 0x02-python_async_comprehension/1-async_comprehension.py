#!/usr/bin/env python3
'''The coroutine will collect 10 random numbers
   using an async comprehensing'''
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    ''' return the 10 random numbers.'''
    result: List[float] = []
    async for i in async_generator():
        result.append(i)
    return result
