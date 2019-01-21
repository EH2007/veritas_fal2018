"""
ID: oranged1
LANG: PYTHON2
TASK: ride
"""
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
fin_read = fin.readline().strip()
fin_read2 = fin.readline().strip()
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_dict = {}
counter = 0
for i in letters: 
    counter += 1
    letter_dict[i] = counter

counter2 = 1
for i in fin_read:
    getK = letter_dict.get(i)
    counter2 = counter2 * int(getK)

counter3 = 1
for i in fin_read2:
    getK2 = letter_dict.get(i)
    counter3 = counter3 * int(getK2)

if counter2 % 47 == counter3 % 47:
    fout.write("GO" + "\n")
else:
    fout.write("STAY" + "\n")

