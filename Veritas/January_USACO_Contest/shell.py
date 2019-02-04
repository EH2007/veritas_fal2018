"""
ID: oranged1
LANG: PYTHON3
TASK: shell
"""
fin = open('shell.in', 'r')
fout = open('shell.out', 'w')
loop = int(fin.readline())
given_list = []
for i in range(loop):
    given_list.append(fin.readline().strip().split())
counter = [0, 0, 0]
marble = 0
for i in range(loop):
    marble += 1
    shells = [1, 2, 3]
    shells_copy = [1, 2, 3]
    for i in range(loop):
        shells[int(given_list[i][0]) - 1] = shells_copy[int(given_list[i][1]) - 1]
        shells[int(given_list[i][1]) - 1] = shells_copy[int(given_list[i][0]) - 1]
        if marble == shells[int(given_list[i][2]) - 1]:
            counter[marble - 1] += 1
        shells_copy = shells[:]

fout.write(str(max(counter)) + "\n")
fout.close()

# SUCCESS!