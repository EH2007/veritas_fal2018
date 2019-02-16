"""
ID: oranged1
LANG: PYTHON3
TASK: namenum
"""
import itertools
fin = open('namenum.in', 'r')
fin2 = open('dict.txt', 'r')
fout = open('namenum.out', 'w')

namenum_dict = {2: ["A", "B", "C"], 3: ["D", "E", "F"], 4: ["G", "H", "I"], 5: ["J", "K", "L"], 6: ["M", "N", "O"], 7: ["P", "R", "S"], 8: ["T", "U", "V"], 9: ["W", "X", "Y"]}
accept_name = {}
for name in fin2.readlines():
    accept_name[name.strip()] = None

given_num = fin.readline().strip()  # '4734' 

# https://www.geeksforgeeks.org/iterator-functions-python-set-2islice-starmap-tee/
numname_list = []
for i in given_num:
    numname_list.append(namenum_dict[int(i)])
name_list = list(itertools.product(*numname_list))

for i in range(len(name_list)):
    name_list[i] = ''.join(name_list[i])
result_lst = []
for name in name_list:
    if name in accept_name:
        result_lst.append(name)
result_lst.sort()
if len(result_lst) > 0:
    for i in result_lst:
        fout.write(i + "\n")
    fout.close()
else:
    fout.write("NONE" + "\n")
    fout.close()