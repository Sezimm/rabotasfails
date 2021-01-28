f = open('/home/sezim/zadachi/rabota_s_files/python.txt', 'r')
c = (f.read()).split()
t_words = []
for x in c:
	if "t" in x:
		t_words.append(x)
	if "T" in x:
		t_words.append(x)	
print(t_words)
f.close()