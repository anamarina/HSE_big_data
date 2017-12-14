#!/usr/bin/env python
# coding = utf-8

import sys
import ast
main_dict = {}

for line in sys.stdin:
	line = ast.literal_eval(line)
	if line['antiNucleus'] not in main_dict:
		main_dict[line['antiNucleus']] = []
	main_dict[line['antiNucleus']].append({'prodTime': line['prodTime'],
	'eventFile': line['eventFile'],
	'Pt': line['Pt']})
	
for key in main_dict:
	pt_set = set()
	counter = 0
	summ = 0
	for line in main_dict[key]:
		counter += 1
		summ += line['Pt']
		pt_set.add(line['eventFile'])
	print({'antiNucleus': key, 'mean': summ, 'uniq': len(pt_set)})
