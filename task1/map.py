#!/usr/bin/env python
# coding=utf-8


# star2002-sample.csv - file

import sys

for line in sys.stdin:
	line = line.split(',')
	out = {'antiNucleus': int(line[0]),
			'eventFile': int(line[1]),
			'prodTime': float(line[10]),
			'Pt': float(line[11])}
	#print(str(out['antiNucleus']),str(out['eventFile']),str(out['prodTime']),str(out['Pt']) )
	print (out)
