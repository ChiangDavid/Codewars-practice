def get_count(sentence):
    count_vowels = 0
    vowels = "aeiou"
    for i in sentence:
        if i in vowels:
            count_vowels += 1
    return count_vowels