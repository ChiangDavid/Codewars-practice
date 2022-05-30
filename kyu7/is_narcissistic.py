# A Narcissistic Number is a number of length l in which the sum of its digits to the power of l is equal to the original number. If this seems confusing, refer to the example below.

# Ex: 153, where l = 3 ( the number of digits in 153 )
# 13 + 53 + 33 = 153

# Write a function that, given n, returns whether or not n is a Narcissistic Number.


def is_narcissistic(i):
    str_i = str(i)
    l_num = len(str_i)
    sum = 0
    for single in str_i:
        sum +=  int(single)**l_num
        print(sum)
        if sum == i:
            return True
    return False
    pass
