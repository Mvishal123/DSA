ls = [5, 12, 4, 1, 2, 3, 1, 1]
K = 5


l = 0
r = 1

while r < len(ls):
    while ls[l] < K and l < len(ls) - 1:
        l += 1

    r = l + 1

    while ls[r] >= K and r < len(ls) - 1:
        r += 1

    temp = ls[l]
    ls[l] = ls[r]
    ls[r] = temp

    r += 1
    l += 1


print(ls)


