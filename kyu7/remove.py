# Exclamation marks series #7: Remove words from the sentence if it contains one exclamation mark

# Description:
# Remove words from the sentence if they contain exactly one exclamation mark. Words are separated by a single space, without leading/trailing spaces.

# Examples
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove(string):
    result = []
    for i in string.split(' '):
        if i.count('!') != 1:
            result.append(i)
    return ' '.join(result)
