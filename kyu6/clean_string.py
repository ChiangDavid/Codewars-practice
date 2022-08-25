# Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

# Your task is to process a string with "#" symbols.

# Examples
# "abc#d##c"      ==>  "ac"
# "abc##d######"  ==>  ""
# "#######"       ==>  ""
# ""              ==>  ""

def clean_string(s):
    # your code here
    result = []
    for i in s:
        if i != "#":
            result.append(i)
        else:
            #if empty_list will evaluate as false.
            if result: 
                result.pop(-1)
    return "".join(result)
