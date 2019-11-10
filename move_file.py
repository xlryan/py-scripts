#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-10 19:00
# @Author  : xlryan
# @Site    : lesstk.com
# @File    : move_file.py
# @IDE    : PyCharm


import time
import os
import shutil

path = "/Users/ryan/Downloads/"
newpath = "/Users/ryan/Downloads/mp4"

def method():
    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1] == ".mp4":
                shutil.move(os.path.join(root, file), os.path.join(newpath, file))
    return 0


if __name__ == '__main__':
    startTime = time.time()
    result = method()

    print('Result:', result)
    print('\nThe time elapsed:', time.time() - startTime, 'seconds !')