# Implement the function unique_in_order which takes as argument a sequence 
# and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

def unique_in_order(iterable):
    #to store current char
    char = ""
    #need to return 
    result = []
    #looping from beginning to last
    for i in range(len(iterable)):
        #if current char/number not equal char
        if iterable[i] != char:
            #append it to the result list
            result.append(iterable[i])
            #change the char to new one(char)
            char = iterable[i]
            
    return result
    pass
