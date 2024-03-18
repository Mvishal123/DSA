arr1 = [1, 3, 3, 3, 3, 4, 5, 7]
arr2 = [2, 3, 5, 6, 7]

# Output
# condition -> arrays should be sorted
# union -> [1, 2, 3, 4, 5, 6, 7]
# intersection -> [3, 5]


def inbuilt(arr1, arr2):
    print(set(arr1).intersection(arr2))


def union_method_1(ls1, ls2):
    final = []
    last = -10000
    i, j = 0, 0

    while i < len(ls1) and j < len(ls2):
        if ls1[i] < ls2[j]:
            if ls1[i] != last:
                final.append(ls1[i])
                last = ls1[i]
            i+=1
        else:
            if ls2[j] != last:
                final.append(ls2[j])
                last = ls2[j]
            j+=1

    while i < len(ls1):
        if ls1[i] != last:
            final.append(ls1[i])
            last = ls1[i]
        i+=1

    while j < len(ls2):
        if ls2[j] != last:
            final.append(ls2[j])
            last = ls2[j]
        j+=1

    return final


print(union_method_1(arr1, arr2))

# s1 = set(arr1).union(arr2)
# s2 = set(arr1).intersection(arr2)
# ls1 = []
# l2 = []
#
# print(list(s1))
# print(list(s2))


