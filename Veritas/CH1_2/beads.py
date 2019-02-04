"""
ID: oranged1
LANG: PYTHON3
TASK: beads
"""
fin = open('beads.in', 'r')
fout = open('beads.out', 'w')

necklace_len = int(fin.readline())
necklace = fin.readline()
print_counter = 1
for i in range(necklace_len):
    # cw
    cw_s = necklace[i:]+ necklace[:i]
    # ccw
    ccw_s = cw_s[::-1]
    counter = 0
    prev = 'w'
    for curr in cw_s:
        if curr == 'w':
            counter += 1
        elif prev == 'w':  # prev is w but curr is not w
            counter += 1
            prev = curr
        elif prev == curr:
            counter += 1
        elif prev != curr:
            prev = curr
            break

    prev2 = 'w'
    ccw_s = ccw_s[:necklace_len - counter]
    for curr in ccw_s:
        if curr == 'w':
            counter += 1
        elif prev2 == 'w':
            counter += 1
        elif prev2 == curr:
            counter += 1
        else:
            break
        if curr == 'w':
            pass
        elif curr != 'w':
            prev2 = curr      
    if print_counter < counter:
        print_counter = counter
    # print(i, print_counter)

fout.write(str(print_counter) + '\n')
fout.close()


"""
------- test 1 [length 33 bytes] ----
29
wwwbbrwrbrbrrbrbrwrwwrbwrwrrb
------- test 2 [length 6 bytes] ----
3
rrr
------- test 3 [length 81 bytes] ----
77
rwrwrwrwrwrwrwrwrwrwrwrwbwrwbwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwr
ans: 74
------- test 4 [length 21 bytes] ----
17
wwwwwwwwwwwwwwwww
ans: 17
------- test 5 [length 54 bytes] ----
50
bbrrrbrrrrrrrrbrbbbrbrrbrrrrbbbrbrbbbbbrbrrrbbrbbb
ans: 9
------- test 6 [length 11 bytes] ----
8
rrwwwwbb
ans: 8
------- test 7 [length 205 bytes] ----
200
rrrrrrrrrrrrrrrrrrrrbbbbbbbbbbbbbbbbbbbbrrrrrrrrrrrrrrrrrrrrbbbbbbbbbbbbbbbbbbbbrrrrrrrrrrrrrrrrrrrrbbbbbbbbbbbbbbbbbbbbrrrrrrrrrrrrrrrrrrrrbbbbbbbbbbbbbbbbbbbbrrrrrrrrrrrrrrrrrrrrbbbbbbbbbbbbbbbbbbbb
ans: 40
------- test 8 [length 355 bytes] ----
350
rrbbrbbbwbwwbwbbbbwwrrbbwbrwbrwbbbrbrwrwbrwwwrrbbrrwrbbrwbwrwwwrbrwwwwwrwbwwwrrbrrbbbrbrbbbrbbbrbbwbbbbbrbrrbrwwbrrrrwbwrwrbbwbwrbrbrwwbrrbwbrwwbwwwbrbwrwbwbrbbbwrbwwrrrbwbwbbbbbrrwwwrbrwwrbbwrbbrbbrbwrrwwbrrrbrwbrwwrbwbwrrrbwrwrrbrbbwrwrbrwwwrwbwrrwwwwrrrwrrwbbwrwwrwrbwwbwrrrrbbwrbbrbwwwwwbrbbrbbrbrwbbwbwwbbbbbwwwrbwwbbbwrwwbbrrwrwbwrrwwwrrrwrrwww
ans: 19
------- test 9 [length 338 bytes] ----
333
rwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwb
ans: 4
"""

def rotRight(arr, n):
    res = arr[n:] + arr[:n]
    return res
    
def rotLeftInv(arr, n):
    res = arr[n-1::-1] + arr[:n-1:-1]
    return res

fin = open ('beads.in', 'r')
fout = open ('beads.out', 'w')
n = int(fin.readline().strip())
array = list(fin.readline().strip())

max_length = 0
for a_index in range(len(array)):

    if a_index==n-1:
        print('here')
    a_prev = 'w'
    b_prev = 'w'
    # a_locs = list(range(a_index, len(array))) + list(range(0, a_index))
    # b_locs = list(range(a_index-1, -(len(array)-(a_index-1)), -1))
    a_values = rotRight(array, a_index)
    b_values = rotLeftInv(array, a_index)
    a_len = 0
    b_len = 0
    # for i in a_locs:
    for elem in a_values:
        a_current = elem
        if a_current=='w' or a_prev=='w':
            a_len+= 1
            if a_prev!='w':
                a_current = a_prev
            a_prev = a_current
        elif a_current == a_prev:
            a_len += 1

        # if  (array[i]=='w') or ((a_prev == 'w') or (a_prev == array[i])) : 
        #     a_len += 1
        #     a_prev = array[i]
        else:
            break                   
    #for j in b_locs[:n-a_len]:  # b_locs should be go up to where a_locs stops.
    for elem in b_values[:n-a_len]:
        b_current = elem
        if b_current == 'w' or b_prev =='w':
            b_len += 1
            if b_prev != 'w':
                b_current = b_prev
            b_prev = b_current
        elif b_current == b_prev:
            b_len += 1

        # if  (array[j]=='w') or ((b_prev == 'w') or (b_prev == array[j])):
        #     b_len += 1 
        #     b_prev = array[j]
        else:
            break
    max_length = max(max_length, a_len + b_len)
        


with open('beads.out', 'w') as fout:
    fout.write(str(max_length) + '\n')

fin.close()