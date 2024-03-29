#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-10 19:02
# @Author  : xlryan
# @Site    : lesstk.com
# @File    : remove_files.py
# @IDE    : PyCharm


import time
import os

path = "/Users/ryan/Downloads/"

def method():
    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1] == ".jpg":
                os.remove(os.path.join(root, file))
    return 0


if __name__ == '__main__':
    startTime = time.time()
    result = method()

    print('Result:', result)
    print('\nThe time elapsed:', time.time() - startTime, 'seconds !')