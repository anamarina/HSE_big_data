import sys

file = open('output1.txt', 'r')
dict_val = dict()

for line in file:
    line = line.rstrip('\n') #remove the trailing newline
    value = line.split("\t")
    dict_val[value[0]] = value[1]
file.close()

dict_val
for line in sys.stdin:
    columns = line.split(",")   
    print(columns[0] + "\t" + columns[1] + "," + columns[10] + "," + columns[11] + ',' + dict_val[columns[0]])
         #antiNucleous        #eventFile         #prodTime           #Pt                 # value of antiNucleous
