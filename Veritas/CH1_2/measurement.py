"""
ID: oranged1
LANG: PYTHON3
TASK: measurement
"""



fin = open('measurement.in', 'r')
fout = open('measurement.out', 'w') 

n = int(fin.readline())
measure_list = []
for i in range(n):
    measure_list.append(fin.readline().split())

# measure_lst = [ ['7',  'Mildred', '+3'], ['4',  "Elsie ", '-1' ]

measure_list = [ [int(x[0]), x[1], int(x[2])] for x in measure_list]
measure_list = sorted(measure_list)
cow_dict = {"Bessie" : 7, "Elsie" : 7, "Mildred" : 7}
display = ["Bessie" , "Elsie" , "Mildred"]
counter = 0
for i in measure_list:
    cow_dict[i[1]] += i[2]
    to_be_compared_with_display_later = []
    maxi = 0 
    for cow in cow_dict:
        if maxi < cow_dict[cow]:
            maxi = cow_dict[cow]
    for cow in cow_dict:
        if cow_dict[cow] == maxi:
            to_be_compared_with_display_later.append(cow)
        else:
            pass
    if to_be_compared_with_display_later != display:
        counter += 1
        display = to_be_compared_with_display_later

fout.write(str(counter) + "\n")
fout.close()