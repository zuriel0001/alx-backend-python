#!/usr/bin/env python3
"""
Module that creates asyncio tasks that run asynchronous functions.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    generate asyncio task that waits for a random amount of time
    up to `max_delay` seconds when run

    Return: the created Task object
    """
    return asyncio.create_task(wait_random(max_delay))
