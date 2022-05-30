# Your task is to sum the differences between consecutive pairs in the array in descending order.

# Example
# [2, 1, 10]  -->  9
# In descending order: [10, 2, 1]

# Sum: (10 - 2) + (2 - 1) = 8 + 1 = 9

# If the array is empty or the array has only one element the result should be 0 (Nothing in Haskell, None in Rust).


def sum_of_differences(arr):
    sorted_arr = sorted(arr, reverse= True)
    zip_arr = zip(sorted_arr, sorted_arr[1:])
    sum_arr = 0
    
    for i, j in zip_arr:
        print(i,j)
        sum_arr += i - j
        print(sum_arr)
    return sum_arr
