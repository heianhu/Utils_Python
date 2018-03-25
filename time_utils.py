#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'heianhu'

import time
import functools


def clock(func):
    """
    用于计算函数运算时间的装饰器
    """
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        print('Spend time:%0.8fs' % elapsed)
        return result
    return clocked
