# DESCRIPTION:
# Let us consider this example (array written in general format):

# ls = [0, 1, 3, 6, 10]

# Its following parts:

# ls = [0, 1, 3, 6, 10]
# ls = [1, 3, 6, 10]
# ls = [3, 6, 10]
# ls = [6, 10]
# ls = [10]
# ls = []
# The corresponding sums are (put together in a list): [20, 20, 19, 16, 10, 0]

# The function parts_sums (or its variants in other languages) will take as parameter a list ls and return a list of the sums of its parts as defined above.



def parts_sums(ls):
    result = []
    total = sum(ls)
    #Append first number which is sum of the list
    result.append(total)
    if len(ls) == 0:
        return [0]
    else:
      #Minus the first num in array and append to the list
        for num in ls:
            total -= num
            result.append(total)
    return result
