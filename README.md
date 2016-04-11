ProvRdr

Author: Blase Maglaya

Email: blasemaglaya@gmail.com

Built with Python 3.5.1 on Windows 7

provrdr.py reads in a ProvidentCU bank statement and reports total expenses for every vendor.

ProvidentCU has online delivery of monthly statements with the exentsion .cvs file format available 
through download on their website http://www.providentcu.org/.
Using "provrdr.py infile.cvs" on the command line will filter through the statement and output 
vendor -> total expenses paid to this vendor.

TODO:
- Handle transactions made with ProvidentCU
- Total expenses for month

