def unique_in_order(iterable):
    #to store current char
    char = ""
    #need to return 
    result = []
    #looping from beginning to last
    for i in range(len(iterable)):
        #if current char/number not equal char
        if iterable[i] != char:
            result.append(iterable[i])
            char = iterable[i]
            
    return result
    pass
