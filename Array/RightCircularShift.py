def first_method(ls):
    temp = ls[0]
    for i in range(1, len(ls) + 1):
        toReplace = ls[i%len(ls)]
        ls[i%len(ls)] = temp
        temp = toReplace

    return ls


ls = [1, 2, 3, 4, 5]
print(first_method(ls))

