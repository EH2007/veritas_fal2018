b = "0100101010100010110100100110110100011100111110101001011001110111110000101011011111011001111100011101"
def beautifulBinaryString(b):
    counter = 0
    for i in range(len(b)):
        bb = b[i:i+3]
        if b[i:i+3] == "010":
            counter += 1
    if counter == 0:
        return 0
    else:
        return counter - 1
print(beautifulBinaryString(b))