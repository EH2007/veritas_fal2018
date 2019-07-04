"""
ID: oranged1
LANG: PYTHON2
TASK: combo
"""
fin = open ('combo.in', 'r')
fout = open ('combo.out', 'w')
import itertools

dials = int(fin.readline())
john_code = list(map(int, fin.readline().strip().split()))
master_code = list(map(int, fin.readline().strip().split()))

def makelst(num):
    num2 = num - 2
    result = []
    for i in range(num - 2, num + 3):
        if num2 < 0:
            if num2 == -dials:
                result.append(1)
                num2 += 1   
            else:
                result.append(dials - abs(num2))
                num2 += 1
        elif num2 == dials:
            result.append(num2)
            num2 = 1
        elif num2 == 0:
            result.append(dials)
            num2 += 1
        else:
            result.append(num2)
            num2 += 1
    return result

jcresult = set(map(tuple, itertools.product(makelst(john_code[0]), makelst(john_code[1]), makelst(john_code[2]))))
mcresult = set(map(tuple, itertools.product(makelst(master_code[0]), makelst(master_code[1]), makelst(master_code[2]))))

result = len(jcresult.union(mcresult))
fout.write(str(result) + "\n")
fout.close()