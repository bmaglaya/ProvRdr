"""
provrdr.py

"""

import argparse
import sys
import csv


parser = argparse.ArgumentParser(description="Process ProvidentCU bank statements.")
parser.add_argument("infile", 
					type=str, 
					default=sys.stdin,
					help=".cvs file to be read in")
parser.add_argument("outfile", 
					nargs='?', 
					type=str, 
					default='outfile.txt',
					help="optional output file")
args = parser.parse_args()
	
infile = args.infile
outfile = args.outfile

strarr = []
try:
	with open(infile, newline='') as f:
		reader = csv.reader(f)	
		for row in reader:
			strarr.append(row)
	f.close()
except IOError:
	sys.exit('Could not read file: {}\n'.format(infile))


print(strarr)
"""
list2 = []
for r in strarr:
	list2.append(list(filter(None, r)))
print(list2)

"""
of = open(outfile, 'w')
of.write(str(strarr))
#for rw in list2:
#	of.write('{} \n'.format(rw))
of.close

