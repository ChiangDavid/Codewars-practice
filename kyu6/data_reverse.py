# A stream of data is received and needs to be reversed.

# Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

# 11111111  00000000  00001111  10101010
#  (byte1)   (byte2)   (byte3)   (byte4)
# should become:

# 10101010  00001111  00000000  11111111
#  (byte4)   (byte3)   (byte2)   (byte1)


def data_reverse(data):
    result = []
    #chunk the list into segment of 8
    for num in range(0,len(data),8):
        result.append(data[num:num+8])
    #reverse the list
    reverse_result = list(reversed(result))
    #Join back together
    return [j for i in reverse_result for j in i]
    pass
