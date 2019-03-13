"""
ID: oranged1
LANG: PYTHON3
TASK: dualpal
"""
fin = open('dualpal.in', 'r')
fout = open('dualpal.out', 'w')

finlist = fin.readline().strip().split()
s = int(finlist[0])
n = int(finlist[1])

def baseChange(num, base):
    mapToString = "0123456789ABCDEFGHIJ"
    if num < base:
        return mapToString[num]
    else:
        return baseChange(num // base, base) + mapToString[num % base]

def isPal(num):
    if num[::-1] == num:
        return True
    else:
        return False
i = 0
while i < s:
    n += 1
    counter = 0
    counter2 = 1
    while counter < 2:
        counter2 += 1
        if counter2 == 11:
            break
        else:
            asdf = baseChange(n, counter2)
            if isPal(baseChange(n, counter2)) == True:
                counter += 1
    if counter == 2:
        i += 1
        fout.write(str(n) + "\n")
fout.close()
