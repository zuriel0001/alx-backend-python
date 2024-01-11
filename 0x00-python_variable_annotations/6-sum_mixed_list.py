#!/usr/bin/env python3
"""
takes mxd_lst integers and float returns their sum as float
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Computes sum of mixed list
    """
    return sum(mxd_lst)
