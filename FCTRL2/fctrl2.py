def factorial(number):
	if number == 1:
		return 1
	return number * factorial(number - 1)

total_of_test_cases = int(raw_input())

for t in xrange(total_of_test_cases):
	print factorial(int(raw_input()))
