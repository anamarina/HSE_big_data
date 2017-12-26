import sys

current_key = -1
current_prodTime = []
mean_value = 0

for line in sys.stdin:
    columns = line.split("\t")
    key = columns[0] #antiNucleas
    value = columns[1] #prodTime
    
    if(current_key == -1 or key == current_key):
        current_key = key
        current_prodTime.append(float(value)) #pick prodTime
    else:
        mean = sum(current_prodTime)/len(current_prodTime)
                     
        print(current_key +'\t'+ str(mean))

        current_prodTime = []
        current_key = key
        current_prodTime.append(float(value))
                          
mean = sum(current_prodTime)/len(current_prodTime)
print(str(current_key) +'\t'+ str(mean))
current_prodTime = []
