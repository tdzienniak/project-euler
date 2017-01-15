numbers = []
i = 1
n = 2000000
suma = 0
while i <= n + 1:
	numbers.extend([True])
	i += 1

numbers[0] = False
numbers[1] = False

for index, value in enumerate(numbers):
	if value:
		suma += index
		i = 2
		multiple = index
		while True:
			multiple = index * i
			if multiple > n:
				break
			numbers[multiple] = False
			i += 1

print("The sum of primes below", n, "is:", suma)

input("Press ENTER to terminate.")
