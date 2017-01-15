def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print("All possible ways in 20x20 grid:", factorial(40) / (factorial(20) * factorial(20)))
input("Press ENTER to terminate.")