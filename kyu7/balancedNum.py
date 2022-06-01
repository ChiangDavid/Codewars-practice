# Balanced Number (Special Numbers Series #1 )
# (balanced-num 295591) ==> return "Not Balanced"
# Explanation:
# Since , The sum of all digits to the left of the middle digits (11)

# and the sum of all digits to the right of the middle digits (10) are Not equal , then It's Not Balanced

# Note : The middle digit(s) are 55 .

def balanced_num(number):
    print(number)
    middle = 0
    left = 0
    right = 0
    str_num = str(number)
    number_len = len(str_num)
    if number < 99:
        return "Balanced"
    elif number_len % 2 != 0:
        middle = number_len//2
        left += sum(map(int, str_num[:middle]))
        right += sum(map(int, str_num[middle+1:]))
        if left == right:
            return "Balanced"
        else:
            return "Not Balanced"
    else:
        middle = number_len//2
        left += sum(map(int, str_num[:middle-1]))
        right += sum(map(int, str_num[middle+1:]))
        if left == right:
            return "Balanced"
        else:
            return "Not Balanced"
