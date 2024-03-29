# Problem Statement (hard)#

# Given a binary matrix representing an image, we want to flip the image horizontally, then invert it.

# To flip an image horizontally means that each row of the image is reversed. For example, flipping [0, 1, 1] horizontally results in [1, 1, 0].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [1, 1, 0] results in [0, 0, 1].

# Example 1:

# Input: [
#   [1,0,1],
#   [1,1,1],
#   [0,1,1]
# ]
# Output: [
#   [0,1,0],
#   [0,0,0],
#   [0,0,1]
# ]

# Explanation: First reverse each row: [[1,0,1],[1,1,1],[1,1,0]]. Then, invert the image: [[0,1,0],[0,0,0],[0,0,1]]

# Example 2:

# Input: [
#   [1,1,0,0],
#   [1,0,0,1],
#   [0,1,1,1], 
#   [1,0,1,0]
# ]
# Output: [
#   [1,1,0,0],
#   [0,1,1,0],
#   [0,0,0,1],
#   [1,0,1,0]
# ]

# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]. Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]


def flip_and_invert_image(matrix):

    for i in matrix:
        l, r = 0, len(i) - 1
        while l <= r:
            i[l], i[r] = i[r] ^ 1, i[l] ^ 1
            l, r = l + 1, r - 1
            
    return matrix

def main():
    print(flip_and_invert_image([[1,0,1], [1,1,1], [0,1,1]]))
    print(flip_and_invert_image([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
    print(flip_and_invert_image([[1,1,0],[1,0,1],[0,0,0]]))
main()