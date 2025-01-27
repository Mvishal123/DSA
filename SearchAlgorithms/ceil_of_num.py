def findCeil(ls, target):
    s = 0
    e = len(ls) - 1

    while s <= e:
        mid = (s + e) // 2

        if ls[mid] == target:
            print(ls[mid])
            return

        elif ls[mid] < target:
            s = mid + 1
        else:
            e = mid - 1

    print(ls[s%len(ls)])


ls = [2, 3, 5, 9, 15, 16, 18]
target = 32

findCeil(ls, target)
