# Equal Sides Of An Array
# You are going to be given an array of integers. Your job is to take that array and 
#find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. 
#If there is no index that would make this happen, return -1.

# For example:

# Let's say you are given the array {1,2,3,4,3,2,1}:
# Your function will return the index 3, because at the 3rd position of the array, the sum of left side of the index ({1,2,3}) 
#and the sum of the right side of the index ({3,2,1}) both equal 6.

#Mine solution
def find_even_index(arr):
    #your code here
    left_sum = 0
    right_sum = 0
    for num_idx in range(len(arr)):
        left_sum = sum(arr[0:num_idx])
        right_sum = sum(arr[num_idx+1:len(arr)])
        if left_sum == right_sum:
            return num_idx
    return -1
  
  #Others:
  def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[i:]) == sum(arr[:i+1]):
           return i
    return -1
