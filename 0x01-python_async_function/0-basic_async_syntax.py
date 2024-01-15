#!/usr/bin/env python3
"""basics of async"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine
    returns included and float value
    """
    dly = random.uniform(0, max_delay)
    await asyncio.sleep(dly)
    return dly
