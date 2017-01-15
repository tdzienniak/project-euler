i = 1
squaredSum = 0
sumOfSquares = 0

while i <= 100:
    squaredSum += i
    sumOfSquares += i ** 2
    i += 1

squaredSum = squaredSum ** 2
print squaredSum, '\n'
print sumOfSquares
print squaredSum - sumOfSquares

raw_input('Press ENTER to terminate.')