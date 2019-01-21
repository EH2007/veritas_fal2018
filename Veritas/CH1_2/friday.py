"""
ID: oranged1
LANG: PYTHON3
TASK: friday
"""

# def isleap(yr):
#     if yr % 100 == 0:  # century year
#         if yr % 400 ==0:
#             return True
#         else:
#             return False
#     else:
#         if yr % 4 == 0:
#             return True
#         else:
#             return False

# def getDay(start, no_day):
#     answer = ((start - 1) + 13) % 7 
#     start_next_mth = (start + no_day) % 7

#     return answer, start_next_mth

# ##### 
# fin = open ('friday.in', 'r')
# fout = open ('friday.out', 'w')
# n = fin.readline().strip()
# result_list =[0, 0, 0, 0, 0, 0, 0]
# # jan -> 1, feb -> 2, mar->3 .....
# thirty = [4, 6, 9, 1]
# thirtyone = [1, 3, 4, 5, 7, 8, 10, 12]
# feb_day = 0
# initial_idx = 2
# for i in range(int(n)):
#     # 1. compute year
#     yr = 1900 + n
#     # 2. is leap year?
#     result = isleap(n)
#     # 3. for loop month 
#     for i in range(1, 13):
        
#         if i == 2:  # when feb
#             if result == True:
#                 feb_day = 29
#             else:
#                 feb_day = 28
#         else:  # all other months

from collections import OrderedDict

result_dict = OrderedDict()
# initianlize  0--> sunday, 6 --> Saturday
for day_num in range(7):
    result_dict[day_num] = 0  

def days_in_year(start, year):
    """
    @param start : index of Jan,1 - 1 
    @return : last day of this year
    """
    thirty = [9, 4, 6, 11]
    thirtyone = [1,3,5,7,8,9,10,12]
    if year % 100 == 0:  # century year
        if year % 400 == 0:  # leap year
            feb = 29
        else:
            feb = 28
    else:  # not century year
        if year % 4 == 0 :
            feb = 29
        else: 
            feb = 28

    for month in range(1, 13, 1):
        idx_13 = (start + 13) % 7
        if month in thirty:
            no_of_days_in_month = 30
        elif month in thirtyone:
            no_of_days_in_month = 31
        else:  # 
            no_of_days_in_month = feb 
        idx_lastday_of_month = (start + no_of_days_in_month) % 7

        result_dict[idx_13] += 1
        start =idx_lastday_of_month  # update the start (for 1st day - 1) 

    return start  # start is last day of this year

def main():
    fin = open ('friday.in', 'r')
    n = int(fin.readline().strip())
    y = 1900
    # start getting 13th friday
    # first year
    start = days_in_year(0, y)
    for i in range(1, n, 1):
        y = y + 1
        start = days_in_year(start, y)

    with open('friday.out', 'w') as fout:
        result_lst = []
        for elem in result_dict.values():
            result_lst.append(elem)

        result_lst = [ str(x) for x in result_lst]
        fout.write(result_lst[-1] + ' ' + ' '.join(result_lst[:-1]) + '\n')

    fin.close()

if __name__ == "__main__":

    main()