#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'heianhu'

import unicodedata
import string


def nfc_equal(str1, str2):
    """
    判断两Unicode在使用最少码位构成等价的字符换是否相等
    :param str1:
    :param str2:
    :return:
    """
    return unicodedata.normalize('NFC', str1) == unicodedata.normalize('NFC', str2)


def fold_equal(str1, str2):
    """
    判断两Unicode在使用最少码位构成等价的字符串且将大小写折叠后是否相等
    :param str1:
    :param str2:
    :return:
    """
    return unicodedata.normalize('NFC', str1).casefold == unicodedata.normalize('NFC', str2).casefold


def shave_marks(txt):
    """
    去掉所有组合记号，即去掉变音符号(但会修改非拉丁字符，如希腊字母)
    :param txt:
    :return:
    """
    norm_txt = unicodedata.normalize('NFD', txt)  # 把所有字符分解成基字符和组合记号
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))  # 过滤掉所有组合符号
    return unicodedata.normalize('NFC', shaved)  # 重组所有字符


def shave_marks_latin(txt):
    norm_txt = unicodedata.normalize('NFD', txt)  # 把所有字符分解成基字符和组合记号
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:  # 基字符为拉丁字母时，跳过组合记号
            continue
        keepers.append(c)  # 否则保存当前字符
        # 如果不是组合字符，则是新的基字符
        if not unicodedata.combining(c):  # 监测新的基字符，判断是不是拉丁字母
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved)  # 重组所有字符


if __name__ == '__main__':
    print(str.maketrans("""asdf""", """ASDF"""))
