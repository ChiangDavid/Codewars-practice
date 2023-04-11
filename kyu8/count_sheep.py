# If you can't sleep, just count sheep!!

# Task:
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

# Note:
# As a reminder, in Python strings are immutable, thus adding to a string is an expensive operation.
# For large strings, its usually better to create a list of strings and then call join on the list.

# def count_sheep(n):
#     sheeps = " sheep..."
#     result = ""
#     for i in range(1,n+1,1):
#         result += str(i)+sheeps
#     return result
#     # your code
    
    
def count_sheep(n):
    sheeps = " sheep..."
    result = []
    for i in range(1,n+1,1):
        result.append(str(i)+sheeps)
    return "".join(result)
