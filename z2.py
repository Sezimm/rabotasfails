f = open('/home/sezim/zadachi/rabota_s_files/users.txt', 'w')
name = input("Vedite login: ")
password = input("Vvedite password: ")
f.write(f"login: {name} \nPassword: {password}")
f.close()

