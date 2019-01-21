"""
ID: oranged1
LANG: PYTHON3
TASK: gift1
"""
fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')

result_dict = {}
result_str = ''
fr = int(fin.readline().strip())
for i in range(fr):
    name = fin.readline().strip()
    result_dict[name] = 0

while True:
    name = fin.readline().strip()  # giver
    num = fin.readline().strip().split()  # [ '200', '3']
    if not name:
        break
    if num[1] == '0':
        continue
    else:
        result1 = int(num[0])//int(num[1])  # money for each receiver.
    remainder = int(num[0])% int(num[1]) # money to giver
    result_dict[name] = result_dict[name] - int(num[0])  # giver borrowed money

    # read each line for receiver and give money

    for i in range(int(num[1])):
        name3 = fin.readline().strip()
        result_dict[name3] = result_dict[name3] + result1

    # add remainder to giver     
    result_dict[name] = result_dict[name] + remainder

# Create a result string to write out
for k in result_dict.keys():
    result_str = result_str + k + ' ' + str(result_dict[k]) + "\n"
fout.write(result_str)
fout.close()
