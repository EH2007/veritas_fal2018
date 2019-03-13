"""
ID: oranged1
LANG: PYTHON3
TASK: palsquare
"""
fin = open('palsquare.in', 'r')
fout = open('palsquare.out', 'w')

base = int(fin.readline())

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
while i < 300:
    i += 1
    a = baseChange(i ** 2, base)
    if isPal(a) == True:
        fout.write(str(baseChange(i, base)) + str(" ") + str(a) + "\n")
fout.close()
