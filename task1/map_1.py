#!/usr/bin/env python
# coding=utf-8

# star2002-full.csv - file

import sys

if __name__ == '__main__':
    for i in sys.stdin:
        line = i.split(',')
        prodTime = float(line[10])
        print('1\t'+str(prodTime))
