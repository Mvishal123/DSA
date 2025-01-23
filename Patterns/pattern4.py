def pattern(n):
    cols = n * 2 + 1

    mid = cols // 2
    print(mid)

    for i in range(n):
        for j in range(cols):
            if mid - i <= j + 1 <= mid + i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def optimised_pattern(n):
    for i in range(n):
        blanks = n - i - 1
        stars = i * 2 + 1

        for j in range(blanks + stars + 1):
            while blanks > 0:
                print(" ", end=" ")
                blanks -= 1
            while stars > 0:
                print("*", end=" ")
                stars -= 1

        print()


# pattern(5)
optimised_pattern(6)

