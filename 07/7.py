def getPrimeFactors(num):
    i = 2
    count = 0
    while num != 1:
        if num % i == 0:
            num /= i
            #print i
            count += 1
        else:
            i += 1
    return count

i = 1
count = 0

while count <= 10:
	if getPrimeFactors(i) == 1:
		print i
		count += 1
	i += 1
	

raw_input('Press ENTER to terminate.')