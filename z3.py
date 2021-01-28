f = open('/home/sezim/zadachi/rabota_s_files/file.txt', 'r')
if "w" in f.read():
	print("Yes")
else:
	print("No")
f.close()