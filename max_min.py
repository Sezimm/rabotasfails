z = open('/home/sezim/zadachi/rabota_s_files/numlist.txt', 'r')
w = open('/home/sezim/zadachi/rabota_s_files/max_min.txt', 'a')
x = (z.read()).split()
w.write(f'Max: {max(x)} Min: {min(x)}')

z.close()
w.close()
