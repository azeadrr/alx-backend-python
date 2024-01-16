#!/usr/bin/env python3
"""async_generator coroutine"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """then yield a random number between 0 and 10"""
    bf = []
    for _ in range(10):
        bf.append(random.uniform(0, 10))
    for i in bf:
        await asyncio.sleep(1)
        yield i
