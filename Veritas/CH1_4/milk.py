"""
ID: oranged1
LANG: PYTHON2
TASK: milk
"""
fin = open ('milk.in', 'r')
fout = open ('milk.out', 'w')

mmm = list(map(int, fin.readline().strip().split()))
price_list = []
for i in range(mmm[1]):
    mlk = list(map(int, fin.readline().strip().split()))
    price_list.append(mlk)
price_list = sorted(price_list)
milk_num = mmm[0]
price = 0
for i in price_list:
    if milk_num >= i[1]:
        price += i[1] * i[0]
        milk_num -= i[1]
    elif i[1] > milk_num:
        price += milk_num * i[0]
        milk_num -= milk_num
    if milk_num == 0:
        break
fout.write(str(price) + "\n")
fout.close()