"""
provrdr.py

"""
 
import sys
import csv

def usage_exit(args):
	numargs = len(args)
	if numargs < 2 or numargs > 3:
		sys.exit("usage: provrdr.py infile outfile")


usage_exit(sys.argv)
	
infile = sys.argv[1]
outfile = 'outfile.txt'

if len(sys.argv) == 3:
	outfile = sys.argv[2]

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

