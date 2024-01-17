#!/usr/bin/env python3
'''a coroutine that takes no arguments'''
import asyncio
from typing import Iterator
import random


async def async_generator() -> Generator[float, None, None]:
    '''The coroutine will loop 10 times,
       each time asynchronously wait 1 second'''

    for i in range(10):
        await asyncio.sleep(1)
        y: float = random.uniform(0, 10)
        yield y
