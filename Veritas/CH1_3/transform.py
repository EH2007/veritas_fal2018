"""
ID: oranged1
LANG: PYTHON3
TASK: transform
"""
fin = open('transform.in', 'r')
fout = open('transform.out', 'w')

array_len = int(fin.readline().strip())
array = []
for i in range(array_len):
    row = list(fin.readline().strip())
    array.append(row)
new_array = []
for i in range(array_len):
    row = list(fin.readline().strip())
    new_array.append(row)

def rotate_90():
    global array
    arr90 = array[::-1]
    arr90 = zip(*arr90)
    return list(arr90)

print(rotate_90())
print(new_array)