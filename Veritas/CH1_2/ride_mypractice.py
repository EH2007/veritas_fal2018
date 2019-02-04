"""
ID: oranged1
LANG: PYTHON3
TASK: ride
"""
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')


alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_dict = {}
counter = 0
for letter in alpha:
    counter += 1
    alpha_dict[letter] = counter

fr = fin.readline().strip()
fr2 = fin.readline().strip()

v = 1
for letter in fr:
    l = alpha_dict[letter]
    v = v * l

v2 = 1
for letter in fr2:
    l = alpha_dict[letter]
    v2 = v2 * l



if v % 47 == v2 % 47:
    result = "GO"
else:
    result = "STAY"


fout.write(result + '\n')
fout.close()