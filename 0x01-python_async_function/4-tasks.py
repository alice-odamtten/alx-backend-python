#!/usr/bin/env python3
'''code from wait_n and alter it into a new function'''
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''identical to wait_n except task_wait_random is being called.'''
    x: List[float] = [task_wait_random(max_delay) for i in range(n)]
    return [await i for i in asyncio.as_completed(x)]
