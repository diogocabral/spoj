def increment(number):
    number_list = list(number) 
    last = len(number) - 1

    while number_list[last] == '9': 
        number_list[last] = '0'
        last -= 1
    
    number_list[last] = str(int(number_list[last]) + 1)

    return "".join(number_list)

def palindrome(number):
	length = len(number)

	left = number[:length/2]
	right = left[::-1]

	if length % 2 == 0:
		center = ''
	else:
		center = number[length/2]

	palindrome = left + center + right

	if palindrome > number:
		return palindrome
	else:
		if center:
			if center < '9':
				center = increment(center)
				return left + center + right
			else:
				center = '0'
		if left == len(left) * '9':
			return '1' + (length - 1) * '0' + '1'
		else:
			left = increment(left)
			return left + center + left[::-1]

total_of_test_cases = int(raw_input())

for t in xrange(total_of_test_cases):
	number = raw_input()
	print palindrome(number)