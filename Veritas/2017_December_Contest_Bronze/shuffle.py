"""
ID: oranged1
LANG: PYTHON3
TASK: shuffle
"""
fin = open ('shuffle.in', 'r')
fout = open ('shuffle.out', 'w')
num = int(fin.readline())
pos = list(map(int, fin.readline().strip().split()))
after_cows = list(map(int, fin.readline().strip().split()))

copy_cows = after_cows[:]
for i in range(3):
    first_cows = []
    copy_cows2 = []
    for i in range(len(pos)):
        copy_cows2.insert(i, copy_cows[pos[i] - 1])
    copy_cows = copy_cows2[:]
    first_cows = copy_cows[:]
for i in first_cows:
    fout.write(str(i) + "\n")
fout.close()