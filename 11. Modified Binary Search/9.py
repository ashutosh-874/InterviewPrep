# Search in Rotated Array (medium)#

# Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, find if a given ‘key’ is present in it.

# Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present, return -1. You can assume that the given array does not have any duplicates.

# Example 1:

# Input: [10, 15, 1, 3, 8], key = 15
# Output: 1
# Explanation: '15' is present in the array at index '1'.


# Example 2:

# Input: [4, 5, 7, 9, 10, -1, 2], key = 10
# Output: 4
# Explanation: '10' is present in the array at index '4'.



def search_rotated_array(arr, key):
    l, r = 0, len(arr) - 1

    while l  <= r:
        m = (l+r) // 2
        if key > arr[m]:
            if key > arr[r]:
                r = m - 1
            else:
                l = m + 1
        elif key < arr[m]:
            if key < arr[l]:
                l = m + 1
            else:
                r = m - 1
        else:
            return m
    
    

def main():
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))


main()
