# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

#First
def count(string):
    # The function code should be here
    dict = {}
    count = 0
    #initialize dict
    for x in string:
        dict[x] = 0
    
    for chars in string:
        if chars in dict:
            dict[chars] += 1
    
    return dict
  
 #second
def count(string):
    # The function code should be here
    result = {}
    
    for chars in string:
        if chars in result:
            result[chars] += 1
        else:
            result[chars] = 1
    return result
