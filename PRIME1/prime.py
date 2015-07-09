primes = [2]

def is_prime(number):
	if number <= 1:
		return False

	for prime in primes:		
		if prime * prime > number:
			break
		if number % prime == 0:
			return False

	return True

for number in xrange(1, 31623, 2):
	if is_prime(number):
		primes.append(number)

total_of_test_cases = input()

for t in xrange(total_of_test_cases):
	m,n = raw_input().split(" ")
	
	m = int(m)
	n = int(n)

	for number in xrange(m, n + 1):
		if (is_prime(number)):
			print number
	print