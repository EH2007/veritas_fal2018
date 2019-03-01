"""
ID: oranged1
LANG: PYTHON3
TASK: herding
"""

fin = open('herding.in', 'r')
fout = open('herding.out', 'w')

positions = list(map(int, fin.readline().strip().split()))
if positions[2] - positions[1] == 1:
    min_time = ((positions[1] - positions[0]) // 2) + (positions[1] - positions[0]) % 2
    max_time = ((positions[1] - positions[0]) // 2) + (positions[1] - positions[0]) % 2
elif positions[1] - positions[0] == 1:
    min_time = ((positions[2] - positions[1]) // 2) + (positions[2] - positions[1]) % 2
    max_time = ((positions[2] - positions[1]) // 2) + (positions[2] - positions[1]) % 2
else:
    min_time = min(((positions[2] - positions[1]) // 2) + (positions[2] - positions[1]) % 2, ((positions[1] - positions[0]) // 2) + (positions[1] - positions[0]) % 2)
    max_time = max(((positions[2] - positions[1]) // 2) + (positions[2] - positions[1]) % 2, ((positions[1] - positions[0]) // 2) + (positions[1] - positions[0]) % 2)
fout.write(str(min_time) + "\n")
fout.write(str(max_time) + "\n")
fout.close()