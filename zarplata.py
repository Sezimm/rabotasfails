f = open('/home/sezim/zadachi/rabota_s_files/zar.txt', 'r')
a = (f.read().split())
c = 0
for x in range(int(len(a))):
	if a[x] == "May" or a[x] == "July" or a[x] == "September" or a[x] == "November":
		c = c + int(a[x+1])
print(c)
