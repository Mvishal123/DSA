n1 = 20
n2 = 24


def gcd1(n1, n2):
    gcd = 0
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i

    print(gcd)

def gcd2(n1, n2):
    for i in range(min(n1, n2), 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            print(i)
            break

def euclidean_gcd(n1, n2):
    while n1 > 0 and n2 > 0:
        if n1 > n2:
            n1 = n1 - n2
        else:
            n2 = n2 - n1

    if n1 == 0:
        print(n2)
    else:
        print(n1)

gcd1(n1, n2)
gcd2(n1, n2)
euclidean_gcd(n1, n2)