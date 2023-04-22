# Everyone knows passphrases. One can choose passphrases from poems, songs, movies names and so on but frequently they can be guessed due to common cultural references.
#You can get your passphrases stronger by different means. One is the following:

# choose a text in capital letters including or not digits and non alphabetic characters,

# shift each letter by a given number but the transformed letter must be a letter (circular shift),
# replace each digit by its complement to 9,
# keep such as non alphabetic and non digit characters,
# downcase each letter in odd position, upcase each letter in even position (the first character is in position 0),
# reverse the whole result.
# Example:
# your text: "BORN IN 2015!", shift 1

# 1 + 2 + 3 -> "CPSO JO 7984!"

# 4 "CpSo jO 7984!"

# 5 "!4897 Oj oSpC"


def play_pass(s, n):
    # your code
    result = []
    complement = 9
    new_s = s.lower()
    for char in range(len(new_s)):
        if new_s[char].isalpha():
            new_char = chr((ord(new_s[char]) - 97 + n) % 26 + 97)
            if char % 2 == 0:
                result.append(new_char.upper())
            else:
                result.append(new_char.lower())
        elif s[char].isdigit():
            result.append(str(complement - int(new_s[char])))
        else:
            result.append(new_s[char])
            
    return "".join(list(reversed(result)))
    pass
