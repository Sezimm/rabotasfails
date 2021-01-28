
f = open('/home/sezim/zadachi/rabota_s_files/foto.jpg', 'rb')
login = input("Vedite login: ")
par = input("Vedite parol: ")
fo = input("put' do foto: ")
k = open(fo, 'rb')

if f.read() == k.read():
	h = open('/home/sezim/zadachi/rabota_s_files/forma.txt', 'w')
	h.write(f"Login: {login}\nPassword: {par}\nPut': {fo}")
	h.close()
f.close()
k.close()