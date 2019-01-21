"""
ID: oranged1
LANG: PYTHON3
TASK: billboard
"""



def comp_area(arr):
    length = int(arr[2]) - int(arr[0])
    width = int(arr[3]) - int(arr[1])
    area1 = length * width
    return area1

def is_in_b (arr, tx, ty):
    if arr[0] < tx < arr[2] and arr[1] < tx < arr[3]:
        return True
    else:
        return False

def overlap_area(billboard, truck):
    if (truck[3]) < (billboard[1]) or \
     (truck[2]) < (billboard[0]) or int(truck[1]) > int(billboard[3]) or \
      int(truck[2]) < int(billboard[0]):
        return 0
    else:
        x1 = max(truck[0], billboard[0]) 
        y1 = max(truck[1], billboard[1]) 
        x2 = min(truck[2], billboard[2]) 
        y2 = min(truck[3], billboard[3])                     
        overlap_ca = comp_area([x1, y1, x2, y2])
    return overlap_ca



fin = open('billboard.in', 'r')
fout = open('billboard.out', 'w')

billboard1 = list(map(int, fin.readline().split()))  # ['1', '2', '3', '5']
billboard2 = list(map(int, fin.readline().split()))
truck = list(map(int, fin.readline().split()))

ca = comp_area(billboard1)
ca2 = comp_area(billboard2)
overlap1 = overlap_area(billboard1, truck)
overlap2 = overlap_area(billboard2, truck)

fout.write(str((ca + ca2) - (overlap1 + overlap2)) + '\n')
fout.close()