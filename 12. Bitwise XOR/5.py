# Problem Statement #

# Every non-negative integer N has a binary representation, for example, 8 can be represented as “1000” in binary and 7 as “0111” in binary.

# The complement of a binary representation is the number in binary that we get when we change every 1 to a 0 and every 0 to a 1. For example, the binary complement of “1010” is “0101”.

# For a given positive number N in base-10, return the complement of its binary representation as a base-10 integer.

# Example 1:

# Input: 8
# Output: 7
# Explanation: 8 is 1000 in binary, its complement is 0111 in binary, which is 7 in base-10.

# Example 2:

# Input: 10
# Output: 5
# Explanation: 10 is 1010 in binary, its complement is 0101 in binary, which is 5 in base-10.


def calculate_bitwise_complement(n):

    if n == 0: return 1

    #  count no of bits in n
    num_bits, num = 0, n
    while num > 0:
        num_bits += 1
        num = num >> 1

    # get corresponding number with all bits set to 1
    num_with_bits_set = pow(2, num_bits) - 1

    return n ^ num_with_bits_set 



def main():
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(0)))
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))

main()