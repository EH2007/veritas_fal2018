"""
ID: oranged1
LANG: PYTHON3
TASK: lifeguards
"""


fin = open('lifeguards.in', 'r')
fout = open('lifeguards.out', 'w')

loop = int(fin.readline())

times = {}
times_copy = {}
for i in range(loop):
    given_time = list(map(int, fin.readline().strip().split()))
    for x in range(given_time[0], given_time[1]):
        if x in times:
            times[x].append(i)
            times_copy[x].append(i)
        else:
            times[x] = [i]
            times_copy[x] = [i]
max_time = 0
for cow_number in range(loop):
    shift = [  0 if (cow_number in times[x]) and  (len(times[x]) <= 1) else 1 for x in times] # [ 0, 0, 1, 1, 1]
    max_time = max(sum(shift), max_time)
fout.write(str(max_time) + "\n")
fout.close()