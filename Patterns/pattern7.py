def pattern(n):
    stars = 1
    mid =

    for i in range(n):
        for _ in range(stars):
            print("*", end=" ")
        print()

        if i < mid:
            stars += 1
        else:
            stars -= 1


pattern(6)
