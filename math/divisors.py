import math
def divisors_brute(n):
    d = []
    for i in range(1, n + 1):
        if n % i == 0:
            d.append(i)

    print(d)

def divisors_optimised(n):
    d = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            d.append(i)
            if i != n // i:
                d.append(n//i)
    print(sorted(d))

divisors_brute(36)
divisors_optimised(36)