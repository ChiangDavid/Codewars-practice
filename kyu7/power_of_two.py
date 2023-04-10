# Complete the function power_of_two/powerOfTwo (or equivalent, depending on your language) that determines if a given non-negative integer is a power of two. 
# From the corresponding Wikipedia entry:

# a power of two is a number of the form 2n where n is an integer, i.e. the result of exponentiation with number two as the base and integer n as the exponent.

# You may assume the input is always valid.

# Examples
# power_of_two(1024) ==> True
# power_of_two(4096) ==> True
# power_of_two(333)  ==> False
# Beware of certain edge cases - for example, 1 is a power of 2 since 2^0 = 1 and 0 is not a power of 2.

def power_of_two(x):
    if x == 0:
        return False
    else:
        while x > 1 and x % 2 == 0:
            x //= 2
    if x == 1:
        return True
    return False
  # your code here
