# Task
# Write a function that accepts str string and key number and returns an array of integers representing encoded str.

# Input / Output
# The str input string consists of lowercase characters only.
# The key input number is a positive integer.

# Example
# Encode("scout",1939);  ==>  [ 20, 12, 18, 30, 21]
# Encode("masterpiece",1939);  ==>  [ 14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]

def encode(message, key):
    letter_num = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, 
                  "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12,
                  "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, 
                  "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24,
                  "y": 25, "z": 26}
    
    message_num = []
    key_str = str(key)
    result_list = []
    count = 0
    #Looping the letter in message
    for letter in message:
        #Append the calculated number to list
        result_list.append(letter_num[letter] + int(key_str[count]))
        count += 1
        if count >= len(key_str):
            count = 0
    
    return result_list
        
    # Code here
