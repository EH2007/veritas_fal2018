"""
ID: oranged1
LANG: PYTHON3
TASK: mixmilk
"""

fin = open('mixmilk.in', 'r')
fout = open('mixmilk.out', 'w')

bucket1 = fin.readline().split()
bucket2 = fin.readline().split()
bucket3 = fin.readline().split()
bucket_ca= [[int(bucket1[0]), int(bucket1[1])], [int(bucket2[0]), int(bucket2[1])], [int(bucket3[0]), int(bucket3[1])]]


counter = 0
for i in range(101):
    if counter == 0:
        bucket_ca[counter][1] += bucket_ca[counter + 2][1] 
        bucket_ca[counter + 2][1] = 0
    else:
        bucket_ca[counter][1] += bucket_ca[counter - 1][1]
        bucket_ca[counter - 1][1] = 0
    if bucket_ca[counter][1] > bucket_ca[counter][0]:
        if counter == 0:
            bucket_ca[counter + 2][1] += bucket_ca[counter][1] - bucket_ca[counter][0]
            bucket_ca[counter][1] = bucket_ca[counter][0]
        else:
            bucket_ca[counter - 1][1] += bucket_ca[counter][1] - bucket_ca[counter][0]
            bucket_ca[counter][1] = bucket_ca[counter][0]
    else:
        pass
    counter += 1
    if counter > 2:
        counter = 0



fout.write(str(bucket_ca[0][1]) + "\n" + str(bucket_ca[1][1]) + "\n" + str(bucket_ca[2][1]))
fout.close()
