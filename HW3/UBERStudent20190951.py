import sys, datetime as dt

a = sys.argv[1]
b = sys.argv[2]

def day_is(m, d, y):
	days = ['MON','TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
	day = dt.date(int(y), int(m), int(d)).weekday()
	return days[day]

with open(a, "rt") as a, open(b, "wt") as b:
	for line in a:
		arr = line.split(',')
		region = arr[0]
		d = arr[1].split('/')
		day = day_is(d[0], d[1], d[2])
		vehicles = arr[2]
		trips = arr[3]	
		s = region + "," + day + " " + vehicles + "," + trips
		b.write(s)

