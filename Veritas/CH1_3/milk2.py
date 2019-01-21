"""
ID: oranged1
LANG: PYTHON3
TASK: milk2
"""
import itertools
fin = open('milk2.in', 'r')
fout = open('milk2.out', 'w')
loop = int(fin.readline())
myset = set()
for i in range(loop):
    input_list = fin.readline().split()  # [2, 5] --> [ 2, 3, 4, 5]  <--
    myset.update(range(int(input_list[0]), int(input_list[1])))
list1_0 = [1 if i in myset else 0 for i in range(min(myset), max(myset) + 1)]
max_milking = 0
max_idle = 0
for (key, group) in itertools.groupby(list1_0):
    if key == 1:
        
        max_milking = max(max_milking, len(list(group)))
    elif key == 0:
        max_idle = max(max_idle, len(list(group)))

fout.write(str(max_milking) + " " + str(max_idle) + "\n")
fout.close()

# def listsum(list1_0):
#     if len(list1_0) == 1:
#         return list1_0[0]
#     else:
#         return list1_0[0] + listsum(list1_0[1:])

# print(listsum(list1_0))


# http://interactivepython.org/runestone/static/pythonds/Recursion/pythondsConvertinganIntegertoaStringinAnyBase.html