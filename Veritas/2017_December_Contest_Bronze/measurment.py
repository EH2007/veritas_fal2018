"""
ID: oranged1
LANG: PYTHON3
TASK: measurement
"""
fin = open ('measurement.in', 'r')
fout = open ('measurement.out', 'w')

cows = {"Bessie" : 7, "Elsie" : 7, "Mildred" : 7}

given_cows = [] # [ [ 7, "Mildred",  3]  ]
loop = int(fin.readline())
for i in range(loop):
    given_info = fin.readline().strip().split()  # ["7", "Mildred",  "+3" ]
    given_info = [int(given_info[0]), given_info[1], int(given_info[2])]
    given_cows.append(given_info)
given_cows.sort()
counter = 0
prev_leaders = []
for i in given_cows:
    cows[i[1]] += i[2]
    max_value = max(cows.values())
    leaders = [k for (k, v) in cows.items() if v == max_value]
    if prev_leaders != leaders:
        counter += 1
    prev_leaders = leaders[:]

fout.write(str(counter) + "\n")
fout.close()