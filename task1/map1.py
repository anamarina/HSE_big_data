#!/usr/bin/env python
# coding=utf-8

# star2002-full.csv - file

import sys
       
for line in sys.stdin:
    column = line.split(",")   
    print(column[0]+"\t"+column[10])
