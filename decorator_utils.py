#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'heianhu'

import time
import collections
import functools


def timer(label='', trace=True):
    """
    显示函数运行时间的装饰器，也可以选择用func.alltime显示总时间
    :param label:前缀字符串
    :param trace:是否显示跟踪函数时间
    :return:
    """

    class Timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0

        def __call__(self, *args, **kargs):
            start = time.clock()

            result = self.func(*args, **kargs)
            elapsed = time.clock() - start
            self.alltime += elapsed
            if trace:
                format = '%s %s: %.5f, %.5f'
                values = (label, self.func.__name__, elapsed, self.alltime)
                print(format % values)
            return result

    return Timer


def Tracer(aClass):
    """
    记录调用类中属性或者方法总次数，通过obj.fetches查看调用字典
    :param aClass: 被装饰的类
    :return:
    """

    class Wrapper:
        def __init__(self, *args, **kargs):
            self.fetches = collections.defaultdict(int)
            self.wrapped = aClass(*args, **kargs)

        def __getattr__(self, attrname):
            # print('Trace: ' + attrname)  # 显示调用的属性名或者方法名
            self.fetches[attrname] += 1
            return getattr(self.wrapped, attrname)

    return Wrapper


def coroutine(func):
    """
    向前执行到第一个yield表达式，预激fun()
    :return:
    """
    @functools.wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer()
