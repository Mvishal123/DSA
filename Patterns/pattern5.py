def pattern(n):
    for i in range(n):
        blanks = i
        stars = n * 2 - 2 * i - 1

        for j in range(blanks + stars + 1):
            while blanks > 0:
                print(" ", end=" ")
                blanks -= 1

            while stars > 0:
                print("*", end=" ")
                stars -= 1

        print()



pattern(5)