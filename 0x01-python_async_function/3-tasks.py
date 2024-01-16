#!/usr/bin/env python3
''' takes an integer max_delay and returns a asyncio.Task'''
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''eturns a asyncio.Task.'''
    return asyncio.ensure_future(wait_random(max_delay))
