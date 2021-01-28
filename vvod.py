f = open('/home/sezim/zadachi/rabota_s_files/vvod.txt', 'a')
n = " "
while n != "":
	n = input()
	f.write(f'{n}\n')

f.close()