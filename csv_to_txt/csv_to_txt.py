import csv

infile = './France.csv'
outfile = './out.txt'
with open(infile) as inf:
	with open(outfile, 'w') as outf:
		reader = csv.reader(inf)
		rows = [row for row in reader]
		for row in rows:
			outf.write(str(row[0]) + ' ' + str(row[1]) + '\n')

