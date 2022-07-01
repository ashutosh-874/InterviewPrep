# Problem Statement#

# Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

# Example 1:

# Input: 23   
# Output: true (23 is a happy number)  
# Explanations: Here are the steps to find out that 23 is a happy number:

#     22+322^2 + 3 ^222+32 = 4 + 9 = 13
#     12+321^2 + 3^212+32 = 1 + 9 = 10
#     12+021^2 + 0^212+02 = 1 + 0 = 1

# Example 2:

# Input: 12   
# Output: false (12 is not a happy number)  
# Explanations: Here are the steps to find out that 12 is not a happy number:

#     12+221^2 + 2 ^212+22 = 1 + 4 = 5
#     525^252 = 25
#     22+522^2 + 5^222+52 = 4 + 25 = 29
#     22+922^2 + 9^222+92 = 4 + 81 = 85
#     82+528^2 + 5^282+52 = 64 + 25 = 89
#     82+928^2 + 9^282+92 = 64 + 81 = 145
#     12+42+521^2 + 4^2 + 5^212+42+52 = 1 + 16 + 25 = 42
#     42+224^2 + 2^242+22 = 16 + 4 = 20
#     22+022^2 + 0^222+02 = 4 + 0 = 4
#     424^242 = 16
#     12+621^2 + 6^212+62 = 1 + 36 = 37
#     32+723^2 + 7^232+72 = 9 + 49 = 58
#     52+825^2 + 8^252+82 = 25 + 64 = 89

# Step ‘13’ leads us back to step ‘5’ as the number becomes equal to ‘89’, this means that we can never reach ‘1’, therefore, ‘12’ is not a happy number.


def find_square(num):
	r = 0
	while num > 0:
		r += (num % 10) ** 2
		num //= 10
	return r


def find_happy_number(num):
	
	sv, fv = num, num

	while fv != 1:
		sv = find_square(sv)
		fv = find_square(find_square(fv))

		if sv == fv:
			return False
	
	return True


def main():
	print(find_happy_number(23))
	print(find_happy_number(12))


main()