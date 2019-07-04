"""
ID: oranged1
LANG: PYTHON2
TASK: barn1
"""
fin = open ('barn1.in', 'r')
fout = open ('barn1.out', 'w')

msc = list(map(int, fin.readline().strip().split()))
cow_stalls = []
for i in range(msc[2]):
    stall = int(fin.readline())
    cow_stalls.append(stall)
cow_stalls.sort()
total_stalls = []
for i in range(cow_stalls[0], cow_stalls[msc[2] -1] + 1):
    total_stalls.append(i)

empty_stalls = []
counter = 0
for i in total_stalls:
    if i not in cow_stalls:
        counter += 1
    if i in cow_stalls:
        if counter >= 1:
            empty_stalls.append(counter)
            counter = 0
result = len(total_stalls)
for i in range(msc[0] - 1):
    empty_stalls.sort()
    result -= empty_stalls[len(empty_stalls) - 1]
    empty_stalls.remove(empty_stalls[len(empty_stalls) - 1])
    if len(empty_stalls) == 0:
        break

fout.write(str(result) + "\n")
fout.close()