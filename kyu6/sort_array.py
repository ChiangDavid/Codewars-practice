#Sort the odd
# Task
# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]


def sort_array(source_array):
    odd_number = []
    #looping all the source_array using index
    for num in range(len(source_array)):
      #if the number is odd, we append it to new list
      #and change the origional array to "out" (To show that we remove the number from the original array)
        if source_array[num] % 2 == 1:
            odd_number.append(source_array[num])
            source_array[num] = "Out"
    #Sort the "odd_number" list
    odd_number.sort()
    
    #looping all the "odd_number" list using index
    for num in range(len(odd_number)):
      #replace back the odd_number to the original array that we marked as "Out"
        source_array[source_array.index("Out")] = odd_number[num]
    
    return source_array
