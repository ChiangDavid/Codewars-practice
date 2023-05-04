# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

# Notes:

# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

#Solution 1 using dictionary:
def scramble(s1, s2):
    dict = {}
    for char in s1:
        if not char in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    
    for char in s2:
        if not char in dict or dict[char] < 1:
            return False
        else:
            dict[char] -= 1
    return True


#Solution 2 using count:
def scramble(s1, s2):
  #Using set to get the same character
    for c in set(s2):
      #To check if count of s1's chars less or greater than s2's
        if s1.count(c) < s2.count(c):
            return False
    return True
