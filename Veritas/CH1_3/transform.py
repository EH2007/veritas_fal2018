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

def rotate_90(array):
    arr90 = array[::-1]
    arr90 = zip(*arr90)
    arr90 = [list(i) for i in arr90]
    return list(arr90)

def reflection(array):
    result = []    
    for i in array:
        a = i[::-1]
        result.append(list(a))
    return result

final_result = None

if not final_result:
    before_rot = array
    for i in range(1,4):
        before_rot = rotate_90(before_rot)
        if before_rot == new_array:
            final_result = i
            break

if not final_result:
    reflected = reflection(array)
    if reflected == new_array:
        final_result = 4

if not final_result:
    before_combo = reflection(array)
    for i in range(3):
        before_combo = rotate_90(before_combo)
        if before_combo == new_array:
            final_result = 5
            break
if not final_result:
    if array == new_array:
        final_result = 6

if not final_result:
    final_result = 7
    
fout.write(str(final_result) + "\n")
fout.close()