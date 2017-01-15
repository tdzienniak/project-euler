numbers = []
summa = []
rest = 0

f = open('13.txt', 'r')

for line in f:
    numbers.append(list(line[:-1]))

for i in range(1, 51):
    temp_summa = rest

    for j in range(0, 100):
        temp_summa += int(numbers[j][-i])

    rest = str(temp_summa)
    summa.append(rest[-1])
    rest = int(rest[:-1])


rest = list(str(rest))
rest.reverse()
summa.extend(rest)
summa.reverse()
summa = "".join(summa)

print(summa[:10])
input("Press ENTER to terminate.")