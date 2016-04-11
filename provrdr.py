"""
provrdr.py

"""

import argparse
import sys
import csv

#
# Parse command line arguments
#
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

#
# Read .csv file 
#
data = []

try:
	with open(infile, newline='') as f:
		reader = csv.reader(f)	
		for row in reader:
			data.append(list(filter(None, row)))
	f.close()
except IOError:
	sys.exit('Could not read file: {}\n'.format(infile))


print(data)

for line in data[1:]:
	place = line[1].split(None, 2)
	loc = '{} {}'.format(place[0], place[1])
	print(loc)


of = open(outfile, 'w')
#of.write(str(data))
for rw in data[1:]:
	of.write('{} \n'.format(rw))
of.close

