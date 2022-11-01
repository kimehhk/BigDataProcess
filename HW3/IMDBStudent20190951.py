import sys

a = sys.argv[1]
b = sys.argv[2]
dic = {}

with open(a, "rt") as f:
	for line in f:
		arr = line.split('::')
		genre = arr[2].split('|')
		for g in genre:
			g = g.strip()
			if g in dic:
				dic[g] += 1
			else:
				dic[g] = 1

with open(b, "wt") as f:
	keylist = dic.keys()
	for key in keylist:
		s = key + " " + str(dic[key]) + "\n"
		f.write(s)
