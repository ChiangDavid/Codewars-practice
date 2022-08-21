# Your task, is to create NxN multiplication table, of size provided in parameter.

# for example, when given size is 3:

# 1 2 3
# 2 4 6
# 3 6 9
# for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]

#Mine
def multiplication_table(size):
    column = []
    for i in range(1,size+1):
        row = []
        for j in range(1,size+1):
            multiply = i*j
            row.append(multiply)
        column.append(row)
            
    
    return column
     # good luck
    
#Others:
#List comprehension 
def multiplication_table(size):
#     print([[0 for i in range(3)] for j in range(3)])
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return [[i*j for i in range(1,1+size)]for j in range(1,1+size)]
