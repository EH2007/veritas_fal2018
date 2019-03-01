"""
ID: oranged1
LANG: PYTHON3
TASK: billboard
"""
fin = open ('billboard.in', 'r')
fout = open ('billboard.out', 'w')

billboard1 = list(map(int, fin.readline().strip().split()))
billboard2 = list(map(int, fin.readline().strip().split()))
truck = list(map(int, fin.readline().strip().split()))

def billboard_area(billboard):
    area = (int(billboard[2]) - int(billboard[0])) * (int(billboard[3]) - int(billboard[1]))
    return area

def overlap_area(billboard1, billboard2):
    billboard1_covered = 0
    billboard2_covered = 0
    if billboard1[0] <= truck[2] <= billboard1[2]:
        if billboard1[1] <= truck[3] <= billboard1[3]:
            if billboard1[1] <= truck[1] <= billboard1[3]:
                billboard1_covered = billboard_area(truck)
            else:
                billboard1_covered = (billboard1[3] - truck[3]) * (billboard1[2] - truck[0])
        elif billboard1[1] <= truck[1] <= billboard1[3]:
            billboard1_covered = (billboard1[3] - truck[1]) * (billboard1[2] - truck[0])
        else:
            billboard1_covered = 0
    elif billboard1[0] <= truck[0] <= billboard1[2]:
        if billboard1[1] <= truck[3] <= billboard1[3]:
            if billboard1[1] < truck[1] < billboard1[3]:
                billboard1_covered = (truck[3] - truck[1]) * (billboard1[2] - truck[0])
            else:
                billboard1_covered = (truck[3] - billboard1[1]) * (billboard1[2] - truck[0])
        elif billboard1[1] <= truck[1] <= billboard1[3]:
            billboard1_covered = (billboard1[3] - truck[1]) * (billboard1[2] - truck[0])
        else:
            billboard1_covered = 0
    elif truck[0] <= billboard1[2] <= truck[2]:
        if truck[1] < billboard1[3] < truck[3]:
            billboard1_covered = billboard_area(billboard1)
        else:
            if truck[1] > 0:
                billboard1_covered = (billboard1[3] - truck[3]) * (billboard1[2] - billboard1[0]) + (truck[0] - billboard1[0])
            else:
                billboard1_covered = billboard_area(billboard1) - (billboard1[3] - truck[3]) * (billboard1[2] - billboard1[0])
    else:
        billboard1_covered = 0

    if billboard2[0] <= truck[2] <= billboard2[2]:
        if billboard2[1] <= truck[3] <= billboard2[3]:
            billboard2_covered = (truck[3] - truck[1]) * (truck[2] - billboard2[0])
        elif billboard2[1] <= truck[1] <= billboard2[3]:
            billboard2_covered = (billboard2[3] - truck[1]) * (billboard2[2] - truck[2])
        else:
            billboard2_covered = 0
    elif billboard2[0] <= truck[0] <= billboard2[2]:
        if billboard2[1] <= truck[3] <= billboard2[3]:
            billboard2_covered = (truck[3] - billboard2[1]) * (billboard2[2] - truck[0])
        elif billboard2[1] <= truck[1] <= billboard2[3]:
            billboard2_covered = (billboard2[3] - truck[1]) * (billboard2[2] - truck[0])
        else:
            billboard2_covered = 0
    elif truck[0] <= billboard2[2] <= truck[2]:
        if truck[1] < billboard2[3] < truck[3]:
            billboard2_covered = billboard_area(billboard2)
        else:
            if truck[1] > 0:
                billboard2_covered = (billboard2[3] - truck[3]) * (billboard2[2] - billboard2[0]) - (truck[0] - billboard2[0])
            else:
                billboard2_covered = billboard_area(billboard2) - (billboard2[3] - truck[3]) * (billboard2[2] - billboard2[0])
    else:
        billboard2_covered = 0
    return billboard1_covered + billboard2_covered

result = billboard_area(billboard1) + billboard_area(billboard2) - overlap_area(billboard1, billboard2)
fout.write(str(result) + "\n")
fout.close()
