def find_divisors_quantity(number):
    if number == 1:
        return 1

    count = 0
    divisor = 0
    buddy = 0

    while buddy == 0 or buddy - divisor > 1:
        divisor += 1
        if number % divisor == 0:
            buddy = number / divisor

            if buddy == divisor:
                count += 1
                break

            count += 2

    return count

count = 1
triangle_number = 0

while True:
    triangle_number += count

    divisors = find_divisors_quantity(triangle_number)

    if divisors > 500:
        break

    count += 1

print("Triangle number that has more than 500 divisors:", triangle_number)
input('Press ENTER to terminate.')