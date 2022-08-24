# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.


def expanded_form(num):
    len_num = len(str(num))
    values = 0
    result = []
    while num != 0:
        denomenator = "1" + "0"*(len(str(num))-1)
        divide = num // int(denomenator)
        num %= int(denomenator)
        values = divide * int(denomenator)
        result.append(str(values))
    return " + ".join(result)
    pass
