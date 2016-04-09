"""
provrdr.py

"""
 
import sys
import csv

infile = sys.argv[1]
outfile = 'outfile.txt'

print(str(infile))

strarr = []
with open(infile, newline='') as f:
	reader = csv.reader(f)	
	for row in reader:
		strarr.append(row)
f.close()


list2 = []
for r in strarr:
	list2.append(list(filter(None, r)))
print(list2)

"""
of = open(outfile, 'w')
of.write(str(list2))
#for rw in list2:
#	of.write('{} \n'.format(rw))
of.close
"""