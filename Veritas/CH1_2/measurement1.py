fin = open('measurement.in','r')
fout = open('measurement.out', 'w')

cow_dict = {"Bessie" : 7, "Elsie" : 7, "Mildred" : 7}
display = ["Bessie", "Elsie", "Mildred"]
counter = 0
n = int(fin.readline())
measure_list = []
for i in range(n):
    measure_list.append(fin.readline().split())

measure_list = [ [int(x[0]), x[1], int(x[2])] for x in measure_list]
measure_list = sorted(measure_list)


for i in measure_list:
    cow_dict[i[1]] += i[2]
    to_be_compared_with_display_later = []
    maxi = 0
    for cow in cow_dict:
        if maxi < cow_dict[cow]:
            maxi = cow_dict[cow]
        else:
            pass
    for cow in cow_dict:
        if maxi == cow_dict[cow]:
            to_be_compared_with_display_later.append(cow)
        else:
            pass
    if to_be_compared_with_display_later != display:
        counter += 1
        display = to_be_compared_with_display_later

fout.write(str(counter) + "\n")
fout.close()
