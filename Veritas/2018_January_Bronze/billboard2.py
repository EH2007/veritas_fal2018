"""
ID: oranged1
LANG: PYTHON3
TASK: billboard2
"""

fin = open('billboard.in', 'r')
fout = open('billboard.out', 'w')

lawnmower = list(map(int, fin.readline().strip().split()))
food = list(map(int, fin.readline().strip().split()))

def area(billboard):
    return (billboard[2] - billboard[0]) * (billboard[3] - billboard[1])

def overlap_area(lawnmower, food):
    if (lawnmower[3]) < (food[1]) or \
     (lawnmower[2]) < (food[0]) or int(lawnmower[1]) > int(food[3]) or \
      int(lawnmower[2]) < int(food[0]):
        return 0
    else:
        x1 = max(lawnmower[0], food[0]) 
        y1 = max(lawnmower[1], food[1]) 
        x2 = min(lawnmower[2], food[2]) 
        y2 = min(lawnmower[3], food[3])              
        overlap_ca = area([x1, y1, x2, y2])
    return overlap_ca

