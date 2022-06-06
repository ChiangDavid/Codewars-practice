# Extra Perfect Numbers (Special Numbers Series #7)
# extraPerfect(3)  ==>  return {1,3}
# Explanation:
# (1)10 =(1)2
# First and last bits as set bits.

# (3)10 = (11)2
# First and last bits as set bits.

def extra_perfect(n):
    count = 1
    result = []
    while count <= n:
        binary_n = bin(count)[2::]
        if binary_n[0] == binary_n[-1]:
            result.append(count)
        count += 1
    return result
    #your code here
