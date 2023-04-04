# Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

# For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

# The input will always be valid (numbers will be an array of length 2  
# or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

# Based on: http://oj.leetcode.com/problems/two-sum/

#Brute force O(n^2)
def two_sum(numbers, target):
    result = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] + numbers[j] == target and i != j:
                return [i, j]
              
              
#More optimal O(n)
def two_sum(numbers, target):
  #Create dictionary
  dict={}
  for index, ele in enumerate(numbers):
    #Will find if different between tartget and element is in dict or not
    diff = target - ele
    #If have same diff in dict
    if diff in dict:
      #just return already in dict and current index
      return dict[diff], index
    #Otherwise, add to dict
    dict[ele]= index
