"""
provrdr.py

"""
 
import sys
import csv

infile = sys.argv[1]
print(str(infile))

with open(infile, newline='') as f:
	reader = csv.reader(f)
	of = open('outfile.txt', 'w')
	for row in reader:
		of.write(str(row))
		of.write('\n')
	of.close()
f.close()