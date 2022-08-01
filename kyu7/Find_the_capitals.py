# Instructions
# Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.

# Example
# Test.assertSimilar( capitals('CodEWaRs'), [0,3,4,6] );

def capitals(word):
    #your code here
    result = []
    for idx,char in enumerate(word):
        if char.isupper():
            result.append(idx)
    return result
  
  #One line:
  def capitals(word):
    #your code here
    return [idx for idx,char in enumerate(word) if char.isupper()]
