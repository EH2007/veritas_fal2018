"""
ID: oranged1
LANG: PYTHON3
TASK: traffic
"""

fin = open('traffic.in', 'r')
fout = open('traffic.out', 'w')

loop = int(fin.readline())
highway = []
for i in range(loop):
    given_info = fin.readline().strip().split()
    highway.append(given_info)
none_1 = []
none_2 = []
on = []
off = []
for i in highway:
    if i[0] == "none":
        none_1.append(int(i[1]))
        none_2.append(int(i[2]))
    if i[0] == "on":
        on.append([int(i[1]), int(i[2])])
    if i[0] == "off":
        off.append([int(i[1]), int(i[2])])
mile1 = [max(none_1), min(none_2)]
mileN = [max(none_1), min(none_2)]
for i in on:
    mile1[0] = mile1[0] - i[0]
    mile1[1] = mile1[1] - i[0]
for i in off:
    mileN[0] = mileN[0] - i[0] - 1
    mileN[1] = mileN[1] - i[0]
fout.write(str(mile1[0]) + ' ' + str(mile1[1]) + "\n")
fout.write(str(mileN[0]) + ' ' + str(mileN[1]) + "\n")
fout.close()