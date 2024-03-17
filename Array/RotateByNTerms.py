def brute_force(ls, d):
    temp = []
    for i in range(d):
        temp.append(ls[i])

    for i in range(d, len(ls)):
        ls[i - d] = ls[i]

    for i in range(len(temp)):
        ls[len(ls) - (d - i)] = temp[i]

    return ls

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
d = 3

print(brute_force(ls, d))
