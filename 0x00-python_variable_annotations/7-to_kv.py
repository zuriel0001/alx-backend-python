#!/usr/bin/env python3
"""
function to_kv that takes str k and an int OR float v
and returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Typed-annotated function
    """
    return (k, v * v)
