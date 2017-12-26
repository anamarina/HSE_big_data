#!/usr/bin/env python
# coding=utf-8

import sys

current_key = -1
num_pt = 0
sum_pt = 0
event = set()

for line in sys.stdin:
    columns = line.split("\t")
    key = int(columns[0]) #antiNucleas
    value = columns[1].split(",") #eventFile, prodTime, pt, dict
    if(current_key == -1 or key == current_key):
        current_key = key
        if float(value[1]) >= float(value[3]):
            sum_pt += float(value[2])
            num_pt += 1
            event.add(value[0])
    else:
        print(str(current_key)+"\t"+str(len(event))+","+str(sum_pt/num_pt))
        if float(value[1])>=float(value[3]):
            sum_pt = float(value[2])
            num_pt = 1
            event.clear()
            event.add(value[0])
        current_key = key

print(str(current_key) + "\t" + str(len(event)) + "," + str(sum_pt/num_pt))
