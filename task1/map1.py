#!/usr/bin/env python
# coding=utf-8

# star2002-full.csv - file

import sys
       
for line in sys.stdin:
    columns = line.split(",")   
    print(columns[0]+"\t"+columns[10])

# bash: cat star2002-sample.csv | python map1.py |sort | python reduce1.py > output1.txt |
