def findNumLen(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10

    return count

def armstrong(n):
    temp = n
    p = findNumLen(n)
    res = 0

    while n > 0:
        ld = n % 10
        res += ld ** p
        n //= 10

    print("Is Armstrong: ", temp == res)

armstrong(153)