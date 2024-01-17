#!/usr/bin/env python3
'''coroutine that will execute async_comprehension
   four times in parallel'''
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''execute async_comprehension four times
       in parallel using asyncio.gather'''
    start: float = time.time()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            )
    end: float = time.time()
    return end - start
