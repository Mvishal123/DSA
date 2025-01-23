def pattern(n):
    for i in range(n):
        for j in range(n - i):
            print("*", end=" ")
        print()


def numbers(n):
    for i in range(n):
        for j in range(n - i):
            print(j + 1, end=" ")
        print()


n = 5
# pattern(5)
numbers(5)