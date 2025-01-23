def patterns(n):
    for i in range(n):
        for j in range(i + 1):
            print("* ", end="")
        print("")


def numbers_1(n):
    for i in range(n):
        for j in range(i + 1):
            print(j + 1, end=" ")
        print()

def numbers_2(n):
    for i in range(n):
        for j in range(i + 1):
            print(i + 1, end=" ")
        print()


n = 5
patterns(n)
numbers_1(n)
numbers_2(n)