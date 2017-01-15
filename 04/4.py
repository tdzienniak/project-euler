import math

def is_palindrome(number):
    """Checks whether given number is palindrome or not.
    """

    number = str(number)
    half = math.floor((len(number) / 2))
    i = 0

    while i < half:
        if number[i] != number[-(i + 1)]:
            return False
        i += 1

    return True

largest_palindrome = 0

for a in range(100, 999):
    for b in range(100, 999):
        candidate = a * b

        if is_palindrome(candidate) and candidate > largest_palindrome:
            largest_palindrome = candidate

print("Largest palindrome: ", largest_palindrome)
input("Press ENTER to terminate.")