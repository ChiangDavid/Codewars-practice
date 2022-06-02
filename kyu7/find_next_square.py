# Find the next perfect square!
# You might know some pretty large perfect squares. But what about the NEXT one?

# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

# If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

# Examples:(Input --> Output)

# 121 --> 144
# 625 --> 676
# 114 --> -1 since 114 is not a perfect square

def find_next_square(sq):
    squareroot_sq = int(sq ** 0.5)
    square_sq = squareroot_sq  **2
    number = 0
    result = 0

    if  square_sq  == sq:
        number = squareroot_sq + 1
        result = number ** 2
        return result
    else:
        return -1
