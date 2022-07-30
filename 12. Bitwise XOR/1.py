
#     Given an array of n−1n-1n−1 integers in the range from 111 to nnn, find the one number that is missing from the array.

# Example:

# Input: 1, 5, 2, 6, 4
# Answer: 3

def find_missing_number(array):
    '''
    The idea here is to xor every number in the array with every number in the range given, 
        so in the end we will be left with the missing number.
    e.g. say array is [1, 2, 4], we XOR the array with [1, 2, 3, 4]. 
        After doing the XOR operation, same numbers will cancel out and wee will be left with the missing number.
    '''

    n = len(array) + 1
    x1 = 1
    for i in range(2, n+1):
        x1= x1 ^ i
    
    x2 = array[0]
    for i in array[1:]:
        x2 = x2 ^ i
    
    return x1 ^ x2

    
print(find_missing_number([1, 2, 3, 5, 6]))