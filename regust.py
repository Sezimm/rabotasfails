f = open('/home/sezim/zadachi/rabota_s_files/database.txt', 'r')
x = (f.read()).split()
n = input("Voidite ili zaregaites'\n Vedite login: ")

for i in range(int(len(x))):
	if x[i] == n:
		print("Takoi login est'!")
		log = input("Pridumayte i vvedite login: ")
		pas = input("Pridumayte i vvedite parol: ")
		pas2 = input("Povtorite parol: ")
		if pas == pas2:
			print("registracia proshla uspeshno!")
			l = open('/home/sezim/zadachi/rabota_s_files/database.txt', 'a')
			l.write(f"{log} {pas}\n")
			l.close()
	else:
		log = input("Pridumayte i vvedite login: ")
		pas = input("Pridumayte i vvedite parol: ")
		pas2 = input("Povtorite parol: ")
		if pas == pas2:
			print("registracia proshla uspeshno!")
			l = open('/home/sezim/zadachi/rabota_s_files/database.txt', 'a')
			l.write(f"{log} {pas}\n")
			l.close()
			break

f.close()


