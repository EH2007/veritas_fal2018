"""
ID: oranged1
LANG: PYTHON3
TASK: guess
"""
fin = open('guess.in', 'r')
fout = open('guess.out', 'w')
loop = int(fin.readline().strip())
given_lists = []
given_lists_copy = []
counter = []
for i in range(loop):
    given_list = fin.readline().strip().split()
    given_lists.append(given_list)
    given_lists_copy.append(given_list)
    counter.append(0)
counter_num = -1
for i in given_lists:
    counter_num += 1
    given_lists_copy.remove(i)
    other_lists = given_lists_copy[:]
    for a in i[2:]:
        for b in other_lists:
            if a in b:
                counter[counter_num] += 1
                continue
    given_lists_copy = given_lists[:]

fout.write(str(max(counter)) + "\n")
fout.close()