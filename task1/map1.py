#!/usr/bin/env python
# coding=utf-8

# star2002-full.csv - file

import sys
       
for line in sys.stdin:
    columns = line.split(",")   
    print(columns[0]+"\t"+columns[10])
