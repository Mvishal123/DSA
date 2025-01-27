import math


def isPrime_Brute(n):
    for i in range(2, n):
        if n % i == 0:
            print(False)
            return
    print(True)


def isPrime_Optimal(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(False)
            return
    print(True)


isPrime_Brute(14)
isPrime_Optimal(17)