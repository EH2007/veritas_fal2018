"""
ID: oranged1
LANG: PYTHON3
TASK: gift
"""
fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')

names = {}
loop = int(fin.readline().strip())
for i in range(loop):
    name = fin.readline().strip()
    names[name] = 0

for i in range(loop):
    giver = fin.readline().strip()
    money = fin.readline().split()
    # for i in range(int(money[1])):
    #     given = fin.readline().strip()
    #     names[given] += int(money[0]) // int(money[1])
    # names[giver] -= int(money[0])
    # names[giver] += 200 % 3
    print(money)

# for i in names.keys():
#     print(i, names[i])