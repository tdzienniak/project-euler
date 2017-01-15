def countRight(arr, x, y):
    if x > len(arr[y]) - 4:
        return 0

    count = 1
    for i in range(0, 4):
        count *= arr[y][x + i]
    return count

def countBottom(arr, x, y):
    if y > len(arr) - 4:
        return 0

    count = 1
    for i in range(0, 4):
        count *= arr[y + i][x]
    return count

def countDiagonalRight(arr, x, y):
    if x > len(arr[y]) - 4 or y > len(arr) - 4:
        return 0

    count = 1
    for i in range(0, 4):
        count *= arr[y + i][x + i]
    return count

def countDiagonalLeft(arr, x, y):
    if x < 3 or y > len(arr) - 4:
        return 0

    count = 1
    for i in range(0, 4):
        count *= arr[y + i][x - i]
    return count

f = open('11.txt', 'r')
nums = []
biggest = 0


for line in f:
    splitted = line.split(" ");
    nums.append([int(x) for x in splitted])

for y in range(0, len(nums)):
    for x in range(0, len(nums)):
        biggest = max(biggest,
            countRight(nums, x, y), countBottom(nums, x, y),
            countDiagonalLeft(nums, x, y),
            countDiagonalRight(nums, x, y))

print(biggest)

input()