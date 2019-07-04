"""
ID: oranged1
LANG: PYTHON2
TASK: crypt1
"""
fin = open ('crypt1.in', 'r')
fout = open ('crypt1.out', 'w')
import itertools

"""
5
2 3 4 6 8
"""
dig_num = int(fin.readline()) # 5
nums = list(map(int, fin.readline().strip().split())) # 2 3 4 6 8
first = list(map(list, itertools.product(nums, repeat=3)))
second = list(map(list, itertools.product(nums, repeat=2)))

def numToList(n):
    """
    @param : n : 246
    @return: list : [2, 4, 6]
    """
    return list(map(int, list(str(n))))
    

def listToNum(lst):
    """
    @param lst: [ 2, 3, 4]
    @return: 234
    """
    return int("".join(list(map(str, lst))))

candidate = list(map(list, itertools.product(first, second)))

def isInValue(num):
    num_lst = numToList(num)
    if not (set(num_lst) - set(nums)):
        return True
    return False

result = 0
for i in candidate:
    if isInValue(listToNum(i[0]) * listToNum(i[1])):
        if isInValue(listToNum(i[0]) * (listToNum(i[1])% 10)) and listToNum(i[0]) * (listToNum(i[1])% 10) < 1000 :
            if isInValue(listToNum(i[0]) * (listToNum(i[1]) // 10)) and listToNum(i[0]) * (listToNum(i[1]) // 10) < 1000:
                if len(str(listToNum(i[0]) * listToNum(i[1]))) == 4:
                    result += 1
fout.write(str(result) + "\n")
fout.close()
"""
first = [ 222, 223, 224, 226, 228, 232, 233, 234, 236 ....]

second = [ 22, 23, 24, 26, 28. 32, 33, 34, 36, 38 ....]

candidate = [ [222, 22], [222, 23], [222, 24] ....]

"""