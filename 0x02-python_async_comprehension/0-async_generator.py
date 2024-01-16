#!/usr/bin/env python3
"""Scripts that act as generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asynchronously waits 1 second,
       then yield a random num between 0 and 10
    """
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
