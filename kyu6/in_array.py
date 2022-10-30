# DESCRIPTION:
# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

# Example 1:
# a1 = ["arp", "live", "strong"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns ["arp", "live", "strong"]

# Example 2:
# a1 = ["tarp", "mice", "bull"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns []

# Notes:
# Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
# In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
# Beware: In some languages r must be without duplicates.

#Mine:
def in_array(array1, array2):
    result = []
    for i in array1:
        for j in array2:
            if i in j and not i in result:
                result.append(i)
    return sorted(result)
    # your code
    #return []
    
#Not efficient because it will loop the dulipcate. Instead:
def in_array(array1, array2):
    s = set()
    for x in array1:
        if x not in s:
            for i in array2:
                if x in i:
                    s.add(x)
    return sorted(s)
