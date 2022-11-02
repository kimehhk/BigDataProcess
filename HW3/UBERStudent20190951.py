import sys, datetime as dt

a = sys.argv[1]
b = sys.argv[2]
dic = {}

def day_is(m, d, y):
	days = ['MON','TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
	day = dt.date(int(y), int(m), int(d)).weekday()
	return days[day]

with open(a, "rt") as a:
        for line in a:
                arr = line.split(',')
                region = arr[0]
                d = arr[1].split('/')
                day = day_is(d[0], d[1], d[2])

                s1 = region + "," + day
                if s1 in dic:
                        ar = dic[s1]
                        h = ar.split(',')
                        veh = int(h[0]) + int(arr[2])
                        tr = int(h[1]) + int(arr[3])
                        dic[s1] = str(veh) + "," + str(tr)
                else:
                        dic[s1] = arr[2] + "," +  arr[3]

with open(b, "wt") as f:
        keylist = dic.keys()
        for key in keylist:
                s = key + " " + dic[key] + "\n"
                f.write(s)




