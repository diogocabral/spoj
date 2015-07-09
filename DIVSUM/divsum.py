from math import sqrt

sums = {1 : 0}
def sum(number):
	if number in sums:
		return sums[number]

	sum = 1

	cap = int(sqrt(number)) + 1

	for i in range(2, cap):
		if number % i == 0:
			if i == number / i:
				sum += i
			else:
				sum += i + (number / i)

	sums[number] = sum

	return sum

total_of_test_cases = int(raw_input())

while total_of_test_cases > 0:
	number = int(raw_input())
	print sum(number)
	total_of_test_cases -= 1