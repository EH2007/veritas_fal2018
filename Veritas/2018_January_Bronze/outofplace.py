"""
ID: oranged1
LANG: PYTHON3
TASK: outofplace
"""

fin = open('outofplace.in', 'r')
fout = open('outofplace.out', 'w')

loop = int(fin.readline())
cows = []
for i in range(loop):
    cow = int(fin.readline())
    cows.append(cow)
counter = 0
for i in range(len(cows)-1, 0, -1):
    if max(cows[:i]) > cows[i]:
        cows[i], cows[cows.index(max(cows[:i]))] = cows[cows.index(max(cows[:i]))], cows[i]
        counter += 1
fout.write(str(counter) + "\n")
fout.close()